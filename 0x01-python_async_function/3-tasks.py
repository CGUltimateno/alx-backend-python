#!/usr/bin/env python3
"""
a function that takes an integer
max_delay and returns a asyncio.Task.
"""
from asyncio import create_task, Task


def task_wait_random(max_delay: int) -> Task:
    """
    a function that takes an integer
    max_delay and returns a asyncio.Task.
    """
    return create_task(__import__('0-basic_async_syntax')
                       .wait_random(max_delay))
