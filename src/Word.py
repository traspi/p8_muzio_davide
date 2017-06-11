#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo contente la classe Word
"""

from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Word(Token):
    """Class Word
    rappresenta solo le parole contenute nei requisiti
    specializzazione della classe Token
    """
    # Attributes:
    __tagPos = None  # (String)
    __ambiguitaLessicale = None  # (boolean)
    __stopWord = None  # (boolean)
    __contenutoConcettuale = None  # (String)
    __parolaChiave = None  # (boolean)

    # Operations
    def __init__(self, value=None, tag=None):
        self.setValue(value)
        self.setPosTag(tag)

    def getType(self):
        """function getType
        ritorna il tipo di token

        returns String
        """
        return "Word" # should raise NotImplementedError()
