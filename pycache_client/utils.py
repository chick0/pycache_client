from .const import PAYLOAD_LENGTH
from .const import KEY_LENGTH
from .const import MAX_KEY_LENGTH
from .const import MAX_PAYLOAD_LENGTH
from .error import UnknownCommand
from .error import KeyLong
from .error import ValueLong


def check_commands(command: str) -> bool:
    return command in [
        'SET',
        'GET', 'DEL', 'MD5'
    ]


def get_key_length(key: str) -> bytes:
    length = len(key)

    if length > MAX_KEY_LENGTH:
        raise KeyLong(f"Key is so long ({length} <= {MAX_KEY_LENGTH})")

    length = length.to_bytes(KEY_LENGTH, "little")

    return length


def payload_builder(command: str, key: str, value: bytes = b"") -> bytes:
    command = command.upper()[:3]

    if not check_commands(command=command):
        raise UnknownCommand(f"use SET, GET, DEL, MD5.")

    now_max = MAX_PAYLOAD_LENGTH - 3 - 1 - len(key)
    value_length = len(value)

    if now_max < value_length:
        raise ValueLong(f"value is so long ({value_length} <= {now_max})")

    return command.encode() + get_key_length(key=key) + key.encode() + value


def get_payload_size(payload: bytes) -> bytes:
    length = len(payload)
    length = length.to_bytes(PAYLOAD_LENGTH, "little")

    return length
