#!/usr/bin/env python3
"""This file contains an asynchronous function that
returns a list of random floats"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> tuple[Any]:
    """This function returns a list of random floats"""
    tasks: list = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
