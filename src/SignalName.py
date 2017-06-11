#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe SignalName
"""

from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class SignalName(Token):
    """Class SignalName
    reppresenta il nome dei segnali nei requesiti
    specializzazione della classe Token
    """
    # Attributes:
    __validName = None  # (boolean)

    # Operations
    def __init__(self, value=None, tag=None):
        self.__validName = True
        self.setValue(value)
        self.setPosTag(tag)

    def getType(self):
        """function getType
        ritorna il tipo di token

        returns String
        """
        return "Signal" # should raise NotImplementedError()


