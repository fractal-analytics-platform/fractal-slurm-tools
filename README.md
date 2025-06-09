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
