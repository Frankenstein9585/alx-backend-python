#!/usr/bin/env python3
"""
This file contains an asynchronous function that computes
the total execution time of the wait_n function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function computes the time it takes to run
    an async function"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
