# fractal-slurm-tools

For the moment, you can run the CLI for a given version as in
```console
# Current main
$ pipx run --python 3.11 --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git fractal-slurm-tools
[...]

# Specific commit
$ pipx run --python 3.11 --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@3faeefd0eac0f53c6c73d2e3179b10ff2a111793 fractal-slurm-tools
[...]

# Specific branch
$ pipx run --python 3.11 --spec git+https://github.com/fractal-analytics-platform/fractal-slurm-tools.git@main fractal-slurm-tools
[...]
```

As soon as this will be on PyPI, the expected command will be e.g.
```console
# Latest
$ pipx run --python 3.11 fractal-slurm-tools
[...]

# Specific version
$ pipx run --python 3.11 fractal-slurm-tools==1.2.3
[...]
```

TBD: add `uv` example?


# Development

```console
$ python -m venv venv

$ source venv/bin/activate

$ python -m pip install -e .[dev]
[...]

$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## How to make a release
From the development environment:
```
bumpver update --patch --dry
```


## Contributors and license

Fractal was conceived in the Liberali Lab at the Friedrich Miescher Institute for Biomedical Research and in the Pelkmans Lab at the University of Zurich by [@jluethi](https://github.com/jluethi) and [@gusqgm](https://github.com/gusqgm). The Fractal project is now developed at the [BioVisionCenter](https://www.biovisioncenter.uzh.ch/en.html) at the University of Zurich and the project lead is with [@jluethi](https://github.com/jluethi). The core development is done under contract by [eXact lab S.r.l.](https://www.exact-lab.it).

Unless otherwise specified, Fractal components are released under the BSD 3-Clause License, and copyright is with the BioVisionCenter at the University of Zurich.
