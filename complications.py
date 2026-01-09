import asyncio
import threading
from functools import lru_cache
from typing import Dict, List


class DataFetcher:
    def __init__(self):
        self._lock = threading.Lock()
        self._cache: Dict[str, int] = {}

    @lru_cache(maxsize=5)
    def compute(self, key: str) -> int:
        print(f"Computing value for {key}")
        return sum(ord(c) for c in key)

    async def fetch(self, key: str) -> int:
        await asyncio.sleep(0.1)
        return self.compute(key)

    def store(self, key: str, value: int) -> None:
        with self._lock:
            self._cache[key] = value

    async def process(self, keys: List[str]) -> Dict[str, int]:
        tasks = [self.fetch(key) for key in keys]
        results = await asyncio.gather(*tasks)

        for key, value in zip(keys, results):
            self.store(key, value)

        return self._cache


def run():
    fetcher = DataFetcher()
    keys = ["alpha", "beta", "gamma", "alpha"]

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(fetcher.process(keys))
    print(result)


if __name__ == "__main__":
    run()
# CodeSentinal: created for you by RuchirAdnaik.