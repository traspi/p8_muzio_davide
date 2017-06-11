#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe Token
la quale identifica una singola parola di un requisito
"""

from Leaf import Leaf

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Token:
    """Class Token
    rappresenta una singola parola del requisito iniziale
    ogni Token puo' essere ID, Value, Signal o Word
    """
    # Attributes:
    __value = None  # (String)
    __posTag = None # (String)
    __id = None  # (int)
    __idRequirements = None  # (int)
    __erroreGrammaticale = None  # (boolean)

    # Operations
    def __init__(self):
        self.__id = None
        self.__posTag = None

    def getType(self):
        """function getType

        returns String
        """
        return None # should raise NotImplementedError()

    def getValue(self):
        """function getValue
        ritorna il valore

        returns String
        """
        return self.__value

    def setValue(self, value):
        """function setValue
        imposta il valore del token
        """
        self.__value = value
        return None # should raise NotImplementedError()
    
    def getPosTag(self):
        """function getPosTag
        ritorna il valore del postag

        returns String
        """
        return self.__posTag

    def setPosTag(self, tag):
        """function setPosTag
        imposta il postag del token
        """
        self.__posTag = tag
        return None # should raise NotImplementedError()
