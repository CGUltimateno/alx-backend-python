#!/usr/bin/env python3
"""Type-annotated function element_length
that takes a list input_list of strings as argument and returns a list."""
from typing import Tuple, List,Iterable,Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the string and its length."""
    return [(i, len(i)) for i in lst]
