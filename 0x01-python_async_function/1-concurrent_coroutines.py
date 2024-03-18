#!/usr/bin/python3
"""
 an async routine that will spawn
another async coroutine for some given
number of times.
"""
import asyncio
from typing import List, Callable, Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine that will spawn
    another async coroutine for some given
    number of times.
    """
    wait_random: Callable[[float], Awaitable[float]] = \
        __import__('0-basic_async_syntax').wait_random
    l: List[float] = []

    for i in range(0, n):
        l.append(await wait_random(max_delay))
    return sorted(l)
