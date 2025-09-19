import pytest
from fractal_slurm_tools.errors import ERRORS


@pytest.fixture(scope="function", autouse=True)
def ERRORS_cleanup():
    # FIXME: add explanation
    yield
    ERRORS._reset_state()
