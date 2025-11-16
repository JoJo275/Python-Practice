#!/usr/bin/env python3
"""common_element.py

Check if two sets have any elements in common.

"""

from typing import Set, Any


def have_common_element(set1: Set[Any], set2: Set[Any]) -> bool:
    """
    Determine if two sets have at least one element in common.

    This function uses set intersection to efficiently check for common elements.

    Args:
        set1: The first set of elements.
        set2: The second set of elements.

    Returns:
        True if there is at least one common element, False otherwise.
    """
