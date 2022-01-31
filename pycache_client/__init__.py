__version__ = "1.0.0"
__author__ = "chick_0"
from socket import create_connection

from . import utils
from . import const


class Client:
    def __init__(self, host: str = "127.0.0.1", port: int = 5521, timeout: float = 1.0):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get_connection(self):
        return create_connection(
            address=(self.host, self.port),
            timeout=self.timeout
        )

    def _send(self, payload: bytes) -> bytes:
        conn = self.get_connection()
        conn.send(utils.get_payload_size(payload=payload))
        conn.send(payload)

        length = conn.recv(const.PAYLOAD_LENGTH)
        length = int.from_bytes(length, "little")

        payload = conn.recv(length)

        need_more = length - len(payload)
        while need_more:
            need_more = length - len(payload)
            payload += conn.recv(need_more)

        return payload

    def set(self, key: str, value: bytes) -> str:
        payload = utils.payload_builder(
            command="SET",
            key=key,
            value=value
        )

        return {
            "63726561746564": "CREATED",
            "75706461746564": "UPDATED"
        }.get(self._send(payload=payload).hex(), "undefined")

    def get(self, key: str) -> bytes:
        payload = utils.payload_builder(
            command="GET",
            key=key
        )

        return self._send(payload=payload)

    def delete(self, key: str) -> None:
        payload = utils.payload_builder(
            command="DEL",
            key=key
        )
        self._send(payload=payload)

    def md5(self, key: str) -> str:
        payload = utils.payload_builder(
            command="MD5",
            key=key
        )

        return self._send(payload=payload).decode()
