class Errors:
    def __init__(self):
        self._current_user = None
        self._current_month = None
        self._errors = {}

    def set_user(self, *, email: str):
        self._current_user = email
        self._errors.setdefault(self._current_user, {})

    def set_month(self, *, year: int, month: int):
        self._current_month = (year, month)
        self._errors[self._current_user].setdefault(self._current_month, [])

    def add_error(self, error_msg: str):
        self._errors[self._current_user][self._current_month].append(error_msg)


ERRORS = Errors()
