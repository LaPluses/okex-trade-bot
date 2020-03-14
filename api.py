

class _APIProvider:
    __slots__ = {
        'http_address',
        'websocket_address',
        'timestamp',
    }

    def __init__(self, http_address: str, websocket_address: str, timestamp: int):
        self.http_address = http_address
        self.websocket_address = websocket_address
        self.timestamp = timestamp
