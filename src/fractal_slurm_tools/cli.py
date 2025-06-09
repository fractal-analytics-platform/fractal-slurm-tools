import argparse as ap
import sys

from .process_fractal_job import cli_entrypoint


main_parser = ap.ArgumentParser(
    description="`fractal-slurm-tools` command-line interface",
    allow_abbrev=False,
)

main_parser.add_argument(
    "--fractal-job-id",
    type=int,
    help="Example: '1234'.",
    required=True,
)
main_parser.add_argument(
    "--jobs-folder",
    type=str,
    help="Base folder for job-log subfolders.",
    required=True,
)
main_parser.add_argument(
    "--output-folder",
    type=str,
    help="Folder for CSV/JSON output files.",
    required=True,
)


def _parse_arguments(sys_argv: list[str] | None = None) -> ap.Namespace:
    """
    Parse `sys.argv` or custom CLI arguments.

    Arguments:
        sys_argv: If set, overrides `sys.argv` (useful for testing).
    """
    if sys_argv is None:
        sys_argv = sys.argv[:]
    args = main_parser.parse_args(sys_argv[1:])
    return args


def main():
    args = _parse_arguments()
    cli_entrypoint(
        fractal_job_id=args.fractal_job_id,
        output_folder=args.output_folder,
        jobs_base_folder=args.jobs_folder,
    )
