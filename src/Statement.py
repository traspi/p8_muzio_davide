#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe Statement
la quale identifica un singolo statement in input
"""

from SyntacticTreeList import SyntacticTreeList

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Statement:
    """Class Statement
    identifica un singolo statement in input
    nello specifico puo' essere solamente un requisito
    """
    # Attributes:
    __id = None  # (int)

    # Operations
    def __init__(self):
        self.__id = 0

    def setId(self, id):
        """function setId
        imposta il valore di id
        """
        self.__id = id
        return None

    def getId(self):
        """function getId
        ritorna il valore di id

        return int
        """
        return self.__id

