#!/usr/bin/env python3
"""
This file contains a function that takes a string and an int or float as
arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[float]]:
    """This function takes a string and an int or float as
arguments and returns a tuple."""
    return k, v * v
