from pathlib import Path


def find_job_folder(
    *,
    jobs_base_folder: Path,
    fractal_job_id: int,
) -> Path:
    fractal_job_folders = list(
        item
        for item in jobs_base_folder.glob(
            f"proj_v2_*_job_{fractal_job_id:07d}_*"
        )
        if item.is_dir()
    )
    if len(fractal_job_folders) > 1:
        raise ValueError(f"Found more than one {fractal_job_folders=}.")
    fractal_job_folder = fractal_job_folders[0]
    print(f"Fractal-job folder: {fractal_job_folder.as_posix()}")
    return fractal_job_folder


def find_task_subfolders(fractal_job_folder: Path) -> list[Path]:
    task_subfolders = sorted(
        list(item for item in fractal_job_folder.glob("*") if item.is_dir())
    )
    return task_subfolders


def find_slurm_job_ids(task_subfolder: Path) -> list[int]:
    slurm_job_ids = set()
    for f in task_subfolder.glob("*.out"):
        # Split both using `_` and `-`, to cover conventions for fractal-server
        # below/above 2.14.0.
        jobid_str = f.with_suffix("").name.split("_")[-1].split("_")[-1]
        jobid = int(jobid_str)
        slurm_job_ids.add(jobid)
    slurm_job_ids = sorted(list(slurm_job_ids))
    print(f">> SLURM-job IDs: {slurm_job_ids}")
