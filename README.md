# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/fractal-analytics-platform/fractal-slurm-tools/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                   |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|------------------------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/fractal\_slurm\_tools/\_\_init\_\_.py              |        1 |        0 |        0 |        0 |    100% |           |
| src/fractal\_slurm\_tools/errors.py                    |       45 |        4 |       16 |        1 |     85% |     66-69 |
| src/fractal\_slurm\_tools/parse\_bulk/\_parse\_bulk.py |      112 |       79 |       24 |        0 |     29% |87-136, 148-228, 238-256 |
| src/fractal\_slurm\_tools/parse\_job\_folders.py       |       24 |       24 |        4 |        0 |      0% |      1-50 |
| src/fractal\_slurm\_tools/parse\_sacct\_info.py        |       79 |        4 |       22 |        4 |     92% |147, 151, 166, 173 |
| src/fractal\_slurm\_tools/run\_sacct\_command.py       |       14 |        8 |        2 |        0 |     38% |     22-42 |
| src/fractal\_slurm\_tools/sacct\_fields.py             |       19 |        4 |       10 |        2 |     79% | 43-45, 63 |
| src/fractal\_slurm\_tools/sacct\_parser\_functions.py  |       37 |        1 |        8 |        1 |     96% |        35 |
| src/fractal\_slurm\_tools/sacct\_parsers.py            |       16 |        0 |        8 |        0 |    100% |           |
| **TOTAL**                                              |  **347** |  **124** |   **94** |    **8** | **64%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/fractal-analytics-platform/fractal-slurm-tools/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/fractal-analytics-platform/fractal-slurm-tools/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/fractal-analytics-platform/fractal-slurm-tools/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/fractal-analytics-platform/fractal-slurm-tools/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Ffractal-analytics-platform%2Ffractal-slurm-tools%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/fractal-analytics-platform/fractal-slurm-tools/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.