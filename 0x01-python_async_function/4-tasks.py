#!/usr/bin/python3
"""
Take the code from wait_n and
alter it into a new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called.
"""
import asyncio
import typing


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Take the code from wait_n and
    alter it into a new function task_wait_n.
    The code is nearly identical to wait_n
    except task_wait_random is being called.
    """
    task_wait_random: typing.Callable[[int], asyncio.Task] = \
        __import__('3-tasks').task_wait_random
    l = typing.List[float] = []

    for i in range(0, n):
        l.append(await task_wait_random(max_delay))
    return sorted(l)
