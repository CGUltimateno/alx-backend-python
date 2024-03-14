#!/usr/bin/env python3
"""
Type-annotated function type_checking that returns
a list of numbers multiplied by the givenfactor.
"""
from typing import Union, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list of numbers multiplied by the given factor."""
    return [i * factor for i in lst]
