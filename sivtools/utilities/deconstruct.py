"""Implementing JavaScript object deconstruct functionality in Python"""

from collections import abc
import itertools
from typing import Union


def deconstruct(mapping: dict, extract: Union[str, list]) -> tuple:
    """Return deconstructed dictionary"""
    _mapping = dict(mapping)

    if isinstance(extract, abc.Hashable):
        extracted_value = _mapping.pop(extract)
        return (extracted_value, _mapping)

    if isinstance(extract, abc.Sequence):
        extracted_values = []
        for value in extract:
            extracted_values.append(_mapping.pop(value))

        return itertools.chain(extracted_values, [_mapping])
