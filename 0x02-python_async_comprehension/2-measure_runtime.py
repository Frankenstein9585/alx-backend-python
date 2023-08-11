#!/usr/bin/env python3
"""This file creates a  coroutine that will execute async_comprehension
four times in parallel using asyncio.gather() and compute its runtime
"""
import asyncio
import random
import time
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function will collect 10 random
    numbers using an async comprehension over
    async_generator, then return the 10 random numbers."""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s
