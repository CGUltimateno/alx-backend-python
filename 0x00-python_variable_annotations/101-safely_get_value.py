#!/usr/bin/env python3
"""Type-annotated function safely_get_value
that takes a dict and a key as
arguments and returns the value."""
from typing import Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of the key if it exists, otherwise the default."""
    if key in dct:
        return dct[key]
    else:
        return default
