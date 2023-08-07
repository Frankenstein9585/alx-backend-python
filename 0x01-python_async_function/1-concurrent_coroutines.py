#!/usr/bin/env python3
"""This file contains an asynchronous function that
returns a list of random floats"""
import asyncio
from typing import Any, List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function returns a list of random floats"""
    tasks: list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
