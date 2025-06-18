import calendar
import json
import logging
import os
import sys
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any

import requests

from .parse_sacct_info import parse_sacct_info
from .sacct_parsers import _str_to_bytes

logger = logging.getLogger(__name__)


PARSERS = {
    field: _str_to_bytes
    for field in (
        "MaxDiskWrite",
        "MaxDiskRead",
        "AveDiskWrite",
        "AveDiskRead",
        # "MaxRSS",
        # "MaxVMSize",
        # "AveRSS",
        # "AveVMSize",
    )
}


AVE_MAX_LABELS = ("DiskRead", "DiskWrite", "RSS", "VMSize")


def _verify_max_same_as_ave(outputs: list[dict[str, Any]]) -> None:
    """
    Since each relevant `srun` line in `sacct` is made by a single
    task, its maximum and average values must be identical.

    """
    for out in outputs:
        for label in AVE_MAX_LABELS:
            if out[f"Ave{label}"] != out[f"Max{label}"]:
                logger.error(json.dumps(out, indent=2))
                raise ValueError(f"Ave{label} differs from Max{label}.")


def get_slurm_job_ids_user_month(
    *,
    fractal_backend_url: str,
    user_email: str,
    token: str,
    year: int,
    month: int,
) -> list[int]:
    headers = dict(Authorization=f"Bearer {token}")
    fractal_backend_url = fractal_backend_url.rstrip("/")

    # Get list of users
    resp = requests.get(
        f"{fractal_backend_url}/auth/users/",
        headers=headers,
    )
    if not resp.ok:
        logger.error("Could not get the list of users.")
        logger.error(f"Response status: {resp.status_code}.")
        logger.error(f"Response body: {resp.json()}.")
        sys.exit(1)

    # Find matching user
    try:
        user_id = next(
            user["id"] for user in resp.json() if user["email"] == user_email
        )
    except StopIteration:
        logger.error(f"Could not find user with {user_email=}.")
        sys.exit(1)

    # Get IDs for SLURM jobs
    _, num_days = calendar.monthrange(year=year, month=month)
    timestamp_min = datetime(year, month, 1, tzinfo=timezone.utc).isoformat()
    timestamp_max = datetime(
        year, month, num_days, 23, 59, 59, tzinfo=timezone.utc
    ).isoformat()
    request_body = dict(
        user_id=user_id,
        timestamp_min=timestamp_min,
        timestamp_max=timestamp_max,
    )
    logger.debug(f"{request_body=}")
    resp = requests.post(
        f"{fractal_backend_url}/admin/v2/accounting/slurm/",
        headers=headers,
        json=request_body,
    )
    if not resp.ok:
        logger.error("Could not get the IDs of SLURM jobs.")
        logger.error(f"Response status: {resp.status_code}.")
        logger.error(f"Request body: {request_body}")
        logger.error(f"Response body: {resp.json()}.")
        sys.exit(1)
    slurm_job_ids = resp.json()
    return slurm_job_ids


def cli_entrypoint(
    fractal_backend_url: str,
    user_email: str,
    year: int,
    month: int,
    base_output_folder: str,
) -> None:
    token = os.getenv("FRACTAL_TOKEN", None)
    if token is None:
        sys.exit("Missing env variable FRACTAL_TOKEN")

    # Get IDs of SLURM jobs
    logger.info(
        f"Find SLURM jobs for {user_email=} (month {year:4d}/{month:02d})."
    )
    slurm_job_ids = get_slurm_job_ids_user_month(
        fractal_backend_url=fractal_backend_url,
        user_email=user_email,
        year=year,
        month=month,
        token=token,
    )
    logger.info(
        f"Found {len(slurm_job_ids)} SLURM jobs "
        f"for {user_email=} (month {year:4d}/{month:02d})."
    )

    outdir = Path(base_output_folder, user_email)
    outdir.mkdir(exist_ok=True, parents=True)
    with (outdir / f"{year:4d}_{month:02d}_slurm_jobs.json").open("w") as f:
        json.dump(slurm_job_ids, f, indent=2)

    # Parse sacct

    tot_num_jobs = len(slurm_job_ids)
    batch_size = 10
    logger.info(
        f"Start processing {tot_num_jobs} SLURM jobs, with {batch_size=}."
    )

    tot_cputime_hours = 0.0
    tot_diskread_GB = 0.0
    tot_diskwrite_GB = 0.0
    tot_num_tasks = 0
    for starting_ind in range(0, tot_num_jobs, batch_size):
        slurm_job_ids_batch = ",".join(
            list(
                map(
                    str,
                    slurm_job_ids[starting_ind : starting_ind + batch_size],
                )
            )
        )
        logger.debug(f">> {slurm_job_ids_batch=}")
        outputs = parse_sacct_info(
            slurm_job_id=slurm_job_ids_batch,
            task_subfolder_name=None,
            parser_overrides=PARSERS,
        )
        _verify_max_same_as_ave(outputs)

        num_tasks = len(outputs)
        tot_num_tasks += num_tasks
        logger.debug(f">> {slurm_job_ids_batch=} has {num_tasks=}.")

        for out in outputs:
            cputime_hours = out["CPUTimeRaw"] / 3600
            diskread_GB = out["AveDiskRead"] / 1e9
            diskwrite_GB = out["AveDiskWrite"] / 1e9
            tot_cputime_hours += cputime_hours
            tot_diskread_GB += diskread_GB
            tot_diskwrite_GB += diskwrite_GB

    logger.info(f"{tot_cputime_hours=}")
    logger.info(f"{tot_diskread_GB=}")
    logger.info(f"{tot_diskwrite_GB=}")

    stats = dict(
        user_email=user_email,
        year=year,
        month=month,
        tot_number_jobs=len(slurm_job_ids),
        tot_number_tasks=tot_num_tasks,
        tot_cpu_hours=tot_cputime_hours,
        tot_diskread_GB=tot_diskread_GB,
        tot_diskwrite_GB=tot_diskwrite_GB,
    )
    with (outdir / f"{year:4d}_{month:02d}_stats.json").open("w") as f:
        json.dump(
            stats,
            f,
            indent=2,
        )
