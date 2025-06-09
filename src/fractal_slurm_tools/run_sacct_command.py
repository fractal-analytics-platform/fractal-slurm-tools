import shlex
import subprocess  # nosec

from .sacct_fields import DELIMITER
from .sacct_fields import SACCT_FMT


def run_sacct_command(slurm_job_id: int) -> str:
    cmd = (
        "sacct "
        f"-j {slurm_job_id} "
        "--noheader "
        "--parsable2 "
        f'--format "{SACCT_FMT}" '
        f'--delimiter "{DELIMITER}" '
    )

    res = subprocess.run(  # nosec
        shlex.split(cmd),
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    return res.stdout
