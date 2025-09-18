from enum import Enum


class ErrorType(str, Enum):
    JOB_ONGOING = "job_ongoing"
    JOB_FAILED = "job_failed"
    MISSING_VALUE = "missing_value"


class ErrorCounter(dict):
    def __init__(self):
        super().__init__({error: 0 for error in ErrorType})


class Errors:
    def __init__(self):
        self._current_user = None
        self._errors = {}

    def set_user(self, *, email: str):
        self._current_user = email
        self._errors.setdefault(self._current_user, ErrorCounter())

    def add_error(self, error_type: ErrorType):
        self._errors[self._current_user][error_type] += 1

    def show(self) -> str:
        return self._errors


ERRORS = Errors()
