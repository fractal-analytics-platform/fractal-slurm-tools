# 0.2.0

* Fix `USE_LEGACY_SLURM_FIELDS/USE_LEGACY_FIELDS` inconsistent usage.

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
