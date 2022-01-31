class UnknownCommand(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class KeyLong(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ValueLong(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PayloadLong(Exception):
    def __init__(self, message: str):
        super().__init__(message)
