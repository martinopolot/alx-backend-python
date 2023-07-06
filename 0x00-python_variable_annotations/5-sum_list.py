#!/usr/bin/env python3
""" A list of input of floats, returns sum """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Totals list of floats """
    total: float = 0
    for x in input_list:
        total += x
    return total
