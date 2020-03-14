class OkexObject:

    __slots__ = {
        # Used to mark the object status in specific time
        'timestamp',
    }

    def __init__(
            self,
            timestamp: int,
    ):
        self.timestamp = timestamp


class AccountInfo(OkexObject):
    __slots__ = {
        'currency',
        'balance',
        'id',
        'hold',
        'available',
    }

    def __init__(
        self,
        currency: str,
        balance: str,
        id: str,
        hold: str,
        available: str,
        timestamp: int,
    ):
        self.currency = currency
        self.balance = balance
        self.id = id
        self.hold = hold
        self.available = available
        super().__init__(timestamp=timestamp)
