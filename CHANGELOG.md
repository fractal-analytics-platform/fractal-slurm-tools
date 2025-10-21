# 0.1.1

* Set placeholder user for single-job parsing.

# 0.1.0

This is the first version tracked in CHANGELOG. Here are some notable changes with respect to 0.0.23:
* Rename CLI entrypoints into
    * `fractal-slurm-parse-single-job`
    * `fractal-slurm-parse-bulk`
    * `fractal-slurm-aggregate`
* Drop `SHOW_MISSING_VALUES` environment variable.
* Improve handling of `--verbose`
* Display a brief/verbose report of errors (if any).
