#!/usr/bin/env python3
"""
Contains a method that returns a task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a task that waits for a random numbero fsecods
    Args:
        Max_delay: Maximum numberof secodes that the task will wait
    Returns:
        An asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
