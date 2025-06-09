import logging
from typing import Any

from fractal_slurm_tools.run_cmd import run_cmd
from fractal_slurm_tools.sacct_fields import DELIMITER
from fractal_slurm_tools.sacct_fields import SACCT_FIELDS
from fractal_slurm_tools.sacct_fields import SACCT_FMT
from fractal_slurm_tools.sacct_parsers import SACCT_FIELD_PARSERS

logger = logging.getLogger(__name__)


def parse_sacct_info(
    slurm_job_id: int,
    task_subfolder_name: str,
) -> list[dict[str, Any]]:
    logging.debug(f"Process {slurm_job_id=}.")
    cmd = (
        "sacct "
        f"-j {slurm_job_id} "
        "--noheader "
        "--parsable2 "
        f'--format "{SACCT_FMT}" '
        f'--delimiter "{DELIMITER}" '
    )
    stdout = run_cmd(cmd)
    lines = stdout.splitlines()

    index_job_name = SACCT_FIELDS.index("JobName")
    job_name = lines[0].split(DELIMITER)[index_job_name]
    python_lines = [
        line
        for line in lines
        if line.split(DELIMITER)[index_job_name] in ["python", "python3"]
    ]
    output_rows = []
    for python_line in python_lines:
        python_line_items = python_line.split(DELIMITER)
        output_row = {
            SACCT_FIELDS[ind]: SACCT_FIELD_PARSERS[SACCT_FIELDS[ind]](item)
            for ind, item in enumerate(python_line_items)
        }
        output_row["JobName"] = job_name
        output_row["task_subfolder"] = task_subfolder_name
        output_rows.append(output_row)
    return output_rows
