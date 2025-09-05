# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/fractal-analytics-platform/fractal-slurm-tools/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                     |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|--------------------------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/fractal\_slurm\_tools/\_\_init\_\_.py                |        1 |        0 |        0 |        0 |    100% |           |
| src/fractal\_slurm\_tools/aggregate\_user\_statistics.py |       21 |       21 |        6 |        0 |      0% |      1-41 |
| src/fractal\_slurm\_tools/cli.py                         |       22 |       22 |        4 |        0 |      0% |      1-62 |
| src/fractal\_slurm\_tools/cli\_2.py                      |       26 |       26 |        4 |        0 |      0% |      1-81 |
| src/fractal\_slurm\_tools/cli\_aggregate.py              |       28 |       28 |        4 |        0 |      0% |      1-57 |
| src/fractal\_slurm\_tools/parse\_job\_folders.py         |       24 |       24 |        4 |        0 |      0% |      1-50 |
| src/fractal\_slurm\_tools/parse\_sacct\_info.py          |       79 |       34 |       16 |        2 |     49% |53->exit, 75-76, 114-176 |
| src/fractal\_slurm\_tools/process\_fractal\_job.py       |       34 |       34 |        8 |        0 |      0% |      1-66 |
| src/fractal\_slurm\_tools/query\_user\_interval.py       |      106 |      106 |       30 |        0 |      0% |     1-267 |
| src/fractal\_slurm\_tools/run\_sacct\_command.py         |       14 |        8 |        2 |        0 |     38% |     21-41 |
| src/fractal\_slurm\_tools/sacct\_fields.py               |       17 |        3 |        8 |        1 |     84% |     43-45 |
| src/fractal\_slurm\_tools/sacct\_parser\_functions.py    |       29 |       17 |        8 |        0 |     32% |10, 14-16, 23-31, 35, 39-41, 45 |
| src/fractal\_slurm\_tools/sacct\_parsers.py              |       16 |        0 |        8 |        0 |    100% |           |
|                                                **TOTAL** |  **417** |  **323** |  **102** |    **3** | **21%** |           |


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