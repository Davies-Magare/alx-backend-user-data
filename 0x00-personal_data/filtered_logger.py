#!/usr/bin/env python3

"""
Obfuscate a log message string
"""
import logging
import re
from typing import List


PII_FIELDS = ('name', 'phone', 'password', 'ip', 'ssn')


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
        message = re.sub(
            field + '=.*?' + separator,
            field + '=' + redaction + separator,
            message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the object"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter the log string and redact the given fields
        Args:
            record (logging.LogRecord):
               A logging object with all the information pertaining
               the event being logged
        """
        result = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            result,
            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Create a logger object."""

    logger = logging.getLogger('user_data')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = RedactingFormatter()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
