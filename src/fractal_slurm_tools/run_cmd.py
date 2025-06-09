import shlex
import subprocess  # nosec


def run_cmd(cmd: str) -> str:
    res = subprocess.run(  # nosec
        shlex.split(cmd),
        capture_output=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise ValueError(res.stderr)
    return res.stdout
