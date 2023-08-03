#!/usr/bin/env python3
"""
This file contains a function that takes a float as argument
and returns a function.
"""
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float as argument
and returns a function."""
    def func(x: float) -> float:
        return x * multiplier
    return func
