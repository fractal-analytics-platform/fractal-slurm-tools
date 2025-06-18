import logging
from typing import Any

from .run_sacct_command import run_sacct_command
from .sacct_fields import DELIMITER
from .sacct_fields import SACCT_FIELDS
from .sacct_parsers import SACCT_FIELD_PARSERS

logger = logging.getLogger(__name__)

INDEX_JOB_NAME = SACCT_FIELDS.index("JobName")
INDEX_STATE = SACCT_FIELDS.index("State")


def parse_sacct_info(
    slurm_job_id: str,
    task_subfolder_name: str,
    parser_overrides: dict | None = None,
) -> list[dict[str, Any]]:
    """
    FIXME: document slurm_job_id arg.
    """

    actual_parsers = SACCT_FIELD_PARSERS
    actual_parsers.update(parser_overrides)

    logger.debug(f"Process {slurm_job_id=}.")

    # Run `sacct` command
    stdout = run_sacct_command(slurm_job_id_str=slurm_job_id)

    lines = stdout.splitlines()
    job_name = lines[0].split(DELIMITER)[INDEX_JOB_NAME]
    python_lines = [
        line
        for line in lines
        if line.split(DELIMITER)[INDEX_JOB_NAME] in ["python", "python3"]
    ]
    output_rows = []
    for python_line in python_lines:
        python_line_items = python_line.split(DELIMITER)
        if python_line_items[INDEX_STATE] == "RUNNING":
            logger.debug("Skip RUNNING task")
            continue
        try:
            output_row = {
                SACCT_FIELDS[ind]: actual_parsers[SACCT_FIELDS[ind]](item)
                for ind, item in enumerate(python_line_items)
            }
        except Exception as e:
            logger.error("Error while parsing the following line")
            logger.error(f"{python_line}")
            for ind, item in enumerate(python_line_items):
                logger.error(f"{ind:3d}, {SACCT_FIELDS[ind]}, {item}")
            logger.error(f"{python_line_items}")
            raise e
        output_row.update(
            dict(
                JobName=job_name,
                task_subfolder=task_subfolder_name,
            )
        )
        output_rows.append(output_row)
    return output_rows
