import calendar
import json
import logging
import os
import sys
from datetime import datetime
from datetime import timezone
from pathlib import Path

import requests

from .parse_sacct_info import parse_sacct_info


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
        logging.error("Could not get the list of users.")
        logging.error(f"Response status: {resp.status_code}.")
        logging.error(f"Response body: {resp.json()}.")
        sys.exit(1)

    # Find matching user
    try:
        user_id = next(
            user["id"] for user in resp.json() if user["email"] == user_email
        )
    except StopIteration:
        logging.error(f"Could not find user with {user_email=}.")
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
    resp = requests.post(
        f"{fractal_backend_url}/admin/v2/accounting/slurm/",
        headers=headers,
        json=request_body,
    )
    if not resp.ok:
        logging.error("Could not get the IDs of SLURM jobs.")
        logging.error(f"Request body: {request_body}")
        logging.error(f"Response status: {resp.status_code}.")
        logging.error(f"Response body: {resp.json()}.")
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
    slurm_job_ids = get_slurm_job_ids_user_month(
        fractal_backend_url=fractal_backend_url,
        user_email=user_email,
        year=year,
        month=month,
        token=token,
    )
    outdir = Path(base_output_folder, user_email)
    outdir.mkdir(exist_ok=True, parents=True)
    with (outdir / "slurm_job_ids.json").open("w") as f:
        json.dump(slurm_job_ids, f)

    # Parse sacct
    for slurm_job_id in slurm_job_ids:
        out = parse_sacct_info(
            slurm_job_id=slurm_job_id,
            task_subfolder_name=None,
        )
        print(out)
        exit()
