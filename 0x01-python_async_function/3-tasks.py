#!/usr/bin/env python3
"""
This file contains a regular function that returns
asyncio.Task
"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function returns
asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
