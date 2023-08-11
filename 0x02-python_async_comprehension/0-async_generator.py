#!/usr/bin/env python3
"""This file creates a coroutine called async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This function generates 10 random numbers
    waiting one second between each number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
