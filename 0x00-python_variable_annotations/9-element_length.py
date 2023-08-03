#!/usr/bin/env python3
"""
This file contains a function that returns a list of tuples
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function returns a list of tuples"""
    return [(i, len(i)) for i in lst]
