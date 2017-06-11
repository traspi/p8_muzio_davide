#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe Node
la quale rappresenta un generico nodo del ParseTree
"""

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Node:
    """Class Node
    rappresenta la generalizzazione di un singolo nodo
    del ParseTree che rappresenta un requisito
    """
    # Attributes:
    __id = None  # (int)

    # Operations
    def __init__(self):
        self.__id = None
        self.__node = None

    def setId(self, id):
        """function setId
        imposta l'id del nodo
        """
        self.__id = id
        return None # should raise NotImplementedError()

    def getId(self):
        """function getId
        ritorna l'id del nodo

        returns int
        """
        return self.__id

    def setNode(self, node):
        """function setNode
        imposta il nodo
        """
        self.__node = node
        return None # should raise NotImplementedError()

    def getNode(self):
        """function getNode
        ritorna il nodo

        returns Node
        """
        return self.__node
