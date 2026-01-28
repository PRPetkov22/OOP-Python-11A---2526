from cache import Cache
import time

class SimpleCache(Cache):
    def __init__(self):
        self._data = {}

    def set(self, key, value, ttl=None):
        expires_at = None
        if ttl is not None:
            expires_at = time.time() + ttl

        self._data[key] = {
            "value": value,
            "expires_at": expires_at
        }

    def get(self, key):
        item = self._data.get(key)
        if not item:
            return None

        return item["value"]