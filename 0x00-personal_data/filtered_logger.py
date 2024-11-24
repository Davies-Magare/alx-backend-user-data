#!/usr/bin/env python3

"""
Obfuscate a log message string
"""
import re


def filter_datum(
        fields: str,
        redaction: str,
        message: str,
        separator: str) -> str:
    """Obfuscate a log message"""
    for field in fields:
        result = re.sub(
            f'({field}=)[^{separator}]*',
            f'{field}={redaction}',
            message)
    return result
