#!/usr/bin/env python3
"""
Augment code with the correct duck-typed annotations
that returns the first element in a list.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list if it exists."""
    if lst:
        return lst[0]
    else:
        return None
