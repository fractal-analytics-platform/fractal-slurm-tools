import pytest
from fractal_slurm_tools.errors import ERRORS


@pytest.fixture(scope="function", autouse=True)
def ERRORS_cleanup():
    """
    Reset `ERRORS` after each test, to keep tests stateless.
    """
    yield
    ERRORS._reset_state()
