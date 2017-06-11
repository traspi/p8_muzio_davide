#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo della classe ValueType
"""

from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class ValueType(Token):
    """Class ValueType
    rappresenta i valori contenuti nei requisiti
    specilizzazione della classe Token
    """
    # Attributes:
    __type = None  # (String)

    # Operations
    def __init__(self, value=None, tag=None):
        self.setValue(value)
        self.setPosTag(tag)

    def getType(self):
        """function getType
        ritorna il tipo di token

        returns String
        """
        return "Value" # should raise NotImplementedError()
