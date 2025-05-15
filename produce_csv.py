# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pandas",
#   "humanfriendly",
# ]
# ///
import json
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import humanfriendly
import pandas as pd

SACCT_FIELDS = [
    "JobID",
    "JobName",
    "NodeList",
    "NTasks",
    "SubmitLine",
    "WorkDir",
    "Submit",
    "Start",
    "End",
    "Elapsed",
    "ElapsedRaw",
    "CPUTime",
    "TotalCPU",
    "NCPUS",
    "MaxDiskRead",
    "AveDiskRead",
    "MaxDiskReadTask",
    "MaxDiskWrite",
    "AveDiskWrite",
    "MaxDiskWriteTask",
    "MaxRSS",
    "MaxRSSTask",
    "AveRSS",
    "MaxVMSize",
    "AveVMSize",
    "MaxVMSizeTask",
    "AveCPU",
    "MinCPU",
    "MinCPUTask",
    "ReqTRES",
    "AllocTRES",
    # "MaxPages",
    # "MaxPagesTask",
    # "Partition",
    # "QOS",
]
SACCT_FIELDS_PERCENT = []
for field in SACCT_FIELDS:
    mod_field = field
    if field == "JobName":
        mod_field = f"{field}%30"
    if "TRES" in field:
        mod_field = f"{field}%40"
    SACCT_FIELDS_PERCENT.append(mod_field)

SACCT_FIELDS = [item.split("%")[0] for item in SACCT_FIELDS_PERCENT]
SACCT_FMT = ",".join(SACCT_FIELDS_PERCENT)
DELIMITER = "|"


def _identity(arg: str) -> str:
    return arg


def _str_to_float_to_int(arg: str) -> int:
    return int(float(arg))


def _hhmmss_to_seconds(arg: str) -> int:
    hh, mm, ss = arg.split(":")[:]
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def _str_to_datetime(arg: str) -> datetime:
    return datetime.fromisoformat(arg).isoformat()


def _str_to_bytes(arg: str) -> int:
    return humanfriendly.parse_size(arg)


def _str_to_bytes_to_friendly(arg: str) -> str:
    return humanfriendly.format_size(_str_to_bytes(arg))


SACCT_FIELD_PARSERS = {field: _identity for field in SACCT_FIELDS}

for field in [
    "JobID",
    "NCPUS",
    "NTasks",
    "MinCPUTask",
    "MaxDiskReadTask",
    "MaxDiskWriteTask",
    "MaxPagesTask",
    "MaxRSSTask",
    "MaxVMSizeTask",
]:
    SACCT_FIELD_PARSERS[field] = _str_to_float_to_int

for field in ["Elapsed", "CPUTime", "MinCPU", "AveCPU"]:
    SACCT_FIELD_PARSERS[field] = _hhmmss_to_seconds

for field in ["Submit", "Start", "End"]:
    SACCT_FIELD_PARSERS[field] = _str_to_datetime

for field in [
    "MaxDiskWrite",
    "MaxDiskRead",
    "MaxRSS",
    "MaxVMSize",
    "AveDiskWrite",
    "AveDiskRead",
    "AveRSS",
    "AveVMSize",
]:
    SACCT_FIELD_PARSERS[field] = _str_to_bytes_to_friendly


def run_cmd(cmd: str) -> str:
    res = subprocess.run(
        shlex.split(cmd),
        capture_output=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise ValueError(res.stderr)
    return res.stdout


USAGE = (
    "ERROR: this script requires the three following CLI arguments:\n"
    "   FRACTAL_JOB_ID,\n"
    "   JOBS_FOLDER,\n"
    "   OUTPUT_CSV_FOLDER,\n"
)

if __name__ == "__main__":
    # Parse/validate CLI arguments
    cli_args = sys.argv[1:]
    if len(cli_args) != 3:
        sys.exit(USAGE)

    fractal_job_id = int(cli_args[0])
    jobs_base_folder = Path(cli_args[1])
    if not jobs_base_folder.exists():
        sys.exit(f"ERROR: missing folder {jobs_base_folder}")
    output_folder = Path(cli_args[2])
    if not output_folder.exists():
        output_folder.mkdir()

    # Find Fractal job folder
    fractal_job_folders = list(
        item
        for item in jobs_base_folder.glob(
            f"proj_v2_*job_{fractal_job_id:07d}_*"
        )
        if item.is_dir()
    )
    if len(fractal_job_folders) > 1:
        raise ValueError(f"Found more than one {fractal_job_folders=}.")
    fractal_job_folder = fractal_job_folders[0]
    print(f"Fractal-job folder: {fractal_job_folder.as_posix()}")

    # Find fractal task subfolders
    task_subfolders = sorted(
        list(item for item in fractal_job_folder.glob("*") if item.is_dir())
    )

    # Find SLURM job IDs
    info_rows = []
    for task_subfolder in task_subfolders:
        print(f">> Fractal-task subfolder: {task_subfolder.as_posix()}")

        slurm_job_ids = set()
        print(task_subfolder.as_posix())
        for f in task_subfolder.glob("*.out"):
            jobid = int(f.with_suffix("").name.split("_")[-1])
            slurm_job_ids.add(jobid)
        print(f">> SLURM-job IDs: {slurm_job_ids}")

        for slurm_job_id in sorted(slurm_job_ids):
            print(f">> >> Processing SLURM job with ID {slurm_job_id}")

            cmd = f'sacct -j {slurm_job_id} --format "{SACCT_FMT}"'
            stdout_non_formatted = run_cmd(cmd)
            print(cmd)
            cmd = f'{cmd} --noheader --parsable2 --delimiter "{DELIMITER}"'
            print(cmd)

            stdout = run_cmd(cmd)
            lines = stdout.splitlines()

            index_job_name = SACCT_FIELDS.index("JobName")
            job_name = lines[0].split(DELIMITER)[index_job_name]
            python_lines = [
                line
                for line in lines
                if line.split(DELIMITER)[index_job_name]
                in ["python", "python3"]
            ]
            for python_line in python_lines:
                python_line_items = python_line.split(DELIMITER)
                sacct_info = {
                    SACCT_FIELDS[ind]: SACCT_FIELD_PARSERS[SACCT_FIELDS[ind]](
                        item
                    )
                    for ind, item in enumerate(python_line_items)
                }
                sacct_info["JobName"] = job_name
                info_rows.append(
                    dict(task_subfolder=task_subfolder.name, **sacct_info)
                )

    json_output_file = output_folder / f"out_{fractal_job_id}.json"
    csv_output_file = output_folder / f"out_{fractal_job_id}.csv"
    with json_output_file.open("w") as f:
        json.dump(info_rows, f, indent=2)
    print(f"Written JSON output to {json_output_file.as_posix()}")

    df = pd.read_json(json_output_file)
    df.to_csv(csv_output_file)
    print(f"Written CSV output to {csv_output_file.as_posix()}")
