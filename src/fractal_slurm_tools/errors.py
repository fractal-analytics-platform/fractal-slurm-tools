from enum import Enum


class ErrorType(str, Enum):
    JOB_NOT_FOUND = "Job not found"
    JOB_ONGOING = "Job never ended"
    JOB_NEVER_STARTED = "Job never started"
    MISSING_VALUE = "Missing value"


class Errors:
    def __init__(self):
        self._current_user: str | None = None
        self._errors: dict[tuple[str, ErrorType], int] = {}

    def _reset_state(self):
        """
        This is needed for tests, to avoid propagating ERRORS state.
        """
        self._current_user = None
        self._errors = {}

    @property
    def _users(self) -> set[str]:
        return set(key[0] for key in self._errors)

    def set_user(self, *, email: str):
        self._current_user = email

    def add_error(self, error_type: ErrorType):
        self._errors.setdefault((self._current_user, error_type), 0)
        if error_type not in ErrorType:
            raise ValueError(f"Unknown error type: {error_type}")
        self._errors[(self._current_user, error_type)] += 1

    def report(self, verbose: bool = False) -> str:
        """
        Some errors took place:
        - 19 Job Ongoing
        - 98 Job Failed
        - 21 Missing Value

        # VERBOSE
        Some errors took place:
        - 19 Job Ongoing
              * 10 for foo@fractal.xy
              * 9 for bar@fractal.xy
        - 98 Job Failed
              ...
        - 21 Missing Value
              ....
        """
        print("🔥" * 5, self._errors)
        msg = "Some errors took place:\n"
        for err_type in ErrorType:
            total = sum(
                (self._errors[(user, err_type)] for user in self._users)
            )
            msg += f"- {total} {err_type.value}\n"
            if verbose:
                for user in self._users:
                    count = self._errors[(user, err_type)]
                    if count > 0:
                        msg += f"      * {count} for {user}\n"
        return msg


ERRORS = Errors()
