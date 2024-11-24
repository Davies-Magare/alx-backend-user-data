#!/usr/bin/env python3

"""
Obfuscate a log message string
"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Obfuscate a log message
    Args:
        fields (list): list of fields to obfuscate
        redaction (str): what to obfuscate field values to
        message (str): the log line to obfuscate
        separator (str): The character separating the fields
    Return:
        The obfuscated message
    """
    for field in fields:
        result = re.sub(
            field + '=.*?' + separator,
            field + '=' + redaction + separator,
            message)
    return result
