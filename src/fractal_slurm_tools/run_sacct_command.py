import shlex
import subprocess  # nosec

from fractal_slurm_tools.sacct_fields import DELIMITER
from fractal_slurm_tools.sacct_fields import SACCT_FMT


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
    )
    if res.returncode != 0:
        raise ValueError(res.stderr)
    return res.stdout
