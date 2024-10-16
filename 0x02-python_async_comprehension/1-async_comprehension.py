#!/usr/bin/env python3
"""
Python module to returns 10 random numbers using async comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async_comprehension function to return 10 random numbers
    Args:
        No arguments
    Returns:
        10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
