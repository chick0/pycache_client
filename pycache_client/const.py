PAYLOAD_LENGTH = 3

KEY_LENGTH = 1

#
MAX_KEY_LENGTH = int.from_bytes(b"\xff" * KEY_LENGTH, "little")
MAX_PAYLOAD_LENGTH = int.from_bytes(b"\xff" * PAYLOAD_LENGTH, "little")
