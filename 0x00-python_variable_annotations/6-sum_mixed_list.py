#!/usr/bin/env python3
""" Holds list input of floats and ints, returns sum """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Totals list, returns float """
    total: float = 0
    for x in mxd_lst:
        total += x
    return total
