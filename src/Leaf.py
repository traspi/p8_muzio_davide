#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe Leaf
la quale rappresenta una foglia del ParseTree
"""

from Node import Node

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Leaf(Node):
    """Class Leaf
    rappresenta una foglia del ParseTree
    a cui e' legato un singolo token
    specilizzazione della classe Node
    """
    # Attributes:
    __token = None #(Token)

    # Operations
    def __init__(self, id=None, token=None, node=None):
        self.setToken(token)
        self.setId(id)
        self.setNode(node)

    def getTag(self):
        """function getTag
        ritorna il tag del token

        returns String
        """
        return self.__token.getPosTag()

    def setToken(self, token):
        """function setToken
        imposta il token
        """
        self.__token = token
        return None # should raise NotImplementedError()

    def getToken(self):
        """function getToken
        ritorna il token

        returns Token
        """
        return self.__token

    def numBranch(self):
        """function numBranch
        ritorna il numero di nodi figli
        nel caso di una foglia 0

        returns int
        """
        return 0
