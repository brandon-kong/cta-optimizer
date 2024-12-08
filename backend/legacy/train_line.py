"""
train_line.py

This module contains Enums that represent
different train lines that the software will model.
"""

from enum import StrEnum, auto


class CTATrainLine(StrEnum):
    """
    The CTATrainLine Enum is used to represent the different
    train lines in the Chicago Transit Authority (CTA) train system.
    """

    RED = auto()
    BLUE = auto()
    BROWN = auto()
    PURPLE = auto()
    GREEN = auto()
    ORANGE = auto()
    YELLOW = auto()
    PINK = auto()
