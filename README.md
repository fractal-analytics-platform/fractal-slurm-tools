# fractal-slurm-tools

[![PyPI version](https://img.shields.io/pypi/v/fractal-slurm-tools?color=gree)](https://pypi.org/project/fractal-slurm-tools/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


You can run a version of this tool from PyPI or GitHub, either via
[pipx](https://pipx.pypa.io/stable/examples/#pipx-run-examples) or
[uvx](https://docs.astral.sh/uv/guides/tools).

Examples (the CLI entrypoint <entrypoint> must be one of `fractal-slurm-aggregate` `fractal-slurm-parse-bulk` or `fractal-slurm-parse-single-job`):
```console
# Latest PyPI release
$ pipx run --spec fractal-slurm-tools <entrypoint>
$ uvx --from fractal-slurm-tools <entrypoint>

# Specific PyPI release
$ pipx run --spec fractal-slurm-tools==0.4.0 <entrypoint>
$ uvx --from fractal-slurm-tools==0.4.0 <entrypoint>

# Latest git commit on the default branch
$ pipx run --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git <entrypoint>
$ uvx --from git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git <entrypoint>

# Specific git commit
$ pipx run --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@3faeefd0eac0f53c6c73d2e3179b10ff2a111793 <entrypoint>
$ uvx --from git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@3faeefd0eac0f53c6c73d2e3179b10ff2a111793 <entrypoint>

# Specific git branch
$ pipx run --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@main <entrypoint>
$ uvx --from git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@main <entrypoint>
```

# Environment variables

```bash
# Enable compatibility with legacy SLURM (e.g. v15.08.7)
USE_LEGACY_FIELDS=1

# Modify batch size
SACCT_BATCH_SIZE=50

# Token to connect to the Fractal backend
FRACTAL_TOKEN=...
```

# A useful `sacct` command
```console
sacct --format='JobID%18,JobName%18,State,ReqMem,MaxRSS,AveRSS,Elapsed,NCPUS,CPUTimeRaw,MaxDiskRead,MaxDiskWrite' -j XXXX
```

# Development


### `uv`

We use [uv](https://docs.astral.sh/uv/) to manage the development environment and the dependencies - see https://docs.astral.sh/uv/getting-started/installation/ for methods to install it. From the root folder, you can get started through
```bash
# Create a new virtual environment in `.venv`
uv venv

# Install both the required dependencies and the optional dev/docs dependencies
uv sync --frozen --group dev

# Run a command from within this environment without updating the `uv.lock` file
uv run --frozen fractal-slurm-parse-single-job
```

### Make a release

```console
# Make a release
uv run --frozen bumpver update --patch --dry
```


## Contributors and license

The Fractal project is developed by the [BioVisionCenter](https://www.biovisioncenter.uzh.ch/en.html) at the University of Zurich, who contracts [eXact lab s.r.l.](https://www.exact-lab.it/en/) for software engineering and development support.

Unless otherwise specified, Fractal components are released under the BSD 3-Clause License, and copyright is with the BioVisionCenter at the University of Zurich.
