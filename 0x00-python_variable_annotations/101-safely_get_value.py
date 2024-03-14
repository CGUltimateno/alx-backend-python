#!/usr/bin/env python3
"""Type-annotated function safely_get_value
that takes a dict and a key as
arguments and returns the value."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return the value of the key if it exists, otherwise the default."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
