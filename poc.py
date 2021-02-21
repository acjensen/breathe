from typing import *
import datetime
from datetime import timezone


class Ping():
    timestamp: float


class Storage():
    pings: List[Ping]

    def clean_pings():
        now = datetime.now(timezone.utc)
        # eventually need a better algo here... bisect or similar
        for p in pings:
            if p < now

    def get_ping_count():
        return len(pings)


class Stateless():
    pass


class Client():

    return datetime.now(timezone.utc)


def count_storage(s: Storage):
    for
