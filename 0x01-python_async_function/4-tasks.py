#!/usr/bin/env python3
"""
Take the code from wait_n and
alter it into a new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called.
"""
from typing import (
    List,
    Callable,
    Awaitable
)
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and
    alter it into a new function task_wait_n.
    The code is nearly identical to wait_n
    except task_wait_random is being called.
    """
    task_wait_random: Callable[[float], Awaitable[float]] = \
        __import__('3-tasks').task_wait_random
    my_lis = List[float] = []

    for i in range(0, n):
        my_lis.append(await task_wait_random(max_delay))
    return sorted(my_lis)
