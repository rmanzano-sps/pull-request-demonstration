#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains globals for new_file and a simple function."""

BOOL_VAL = False

def is_boolean(checkval):
    """Function that checks if the entered value is a boolean.

    Args:
        checkval (bool): A value to check that should have a boolean value.

    Returns:
        boolean: A boolean value for checkval.


    Examples:
        >>> is_boolean(1)
        True
    """
    is_bool = True
    try:
        bool(checkval)
    except TypeError:
        is_bool = False

    return is_bool
