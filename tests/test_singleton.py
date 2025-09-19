"""
Test the autoused fixture to reset `ERRORS`.
"""
from fractal_slurm_tools.errors import ERRORS


def test_ERRORS_cleanup_1():
    assert ERRORS._current_user is None
    ERRORS.set_user(email="asd")
    assert ERRORS._current_user == "asd"


def test_ERRORS_cleanup_2():
    assert ERRORS._current_user is None
