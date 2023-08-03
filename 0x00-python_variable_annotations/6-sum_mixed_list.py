#!/usr/bin/env python3
"""
This file contains a function that takes a list of floats and integers
and returns their sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns the sum of a list of integers and floats"""
    return sum(mxd_lst)
