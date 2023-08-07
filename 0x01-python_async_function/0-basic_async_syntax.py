#!/usr/bin/env python3
"""This file contains an asynchronous function that returns a random float"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function returns a random float"""
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
