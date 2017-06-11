#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe NonLeaf
la quale rappresenta un nodo non foglia
"""

from Node import Node

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class NonLeaf(Node):
    """Class NonLeaf
    rappresenta un nodo non foglia del ParseTree
    specialzzazione della classe Node
    """
    # Attributes:
    __value = None  # (String)

    # Operations
    def __init__(self, id=None, tag=None, node=None):
        self.setTag(tag)
        self.setId(id)
        self.__children = []
        self.setNode(node)

    def addChild(self, child):
        """function addChild
        aggiunge un figlio al nodo non foglia
        """
        self.__children.append(child)
        return None # should raise NotImplementedError()

    def getChildren(self):
        """function getChildren
        ritorna la lista di figli del nodo

        returns Node[]
        """
        return self.__children

    def printChildren(self):
        """function printChildren
        stampa i figli del nodo non foglia
        """
        for c in self.__children:
            print(c.getTag())
            if isinstance(c, NonLeaf):
                c.printChildren()
        return None # should raise NotImplementedError()

    def numBranch(self):
        """function numBranch
        calcola l'altezza massima a cui si trova il nodo
        rispetto un nodo foglio

        returns int
        """
        num = 0
        numChildren = []
        if self.__children != []:
            for c in self.__children:
                numChildren.append(c.numBranch())
            num = max(numChildren) + 1
            return num
        else:
            return num

    def setTag(self, tag):
        """function setTag
        imposta il tag del nodo non foglia
        """
        self.__value = tag
        return None # should raise NotImplementedError()

    def getTag(self):
        """function getTag
        ritorna il tag del nodo non foglia

        returns String
        """
        return self.__value

