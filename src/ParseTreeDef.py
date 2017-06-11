#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe ParseTreeDef
"""

from Node import Node
from Leaf import Leaf
from NonLeaf import NonLeaf

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class ParseTreeDef:
    """Class ParseTreeDef
    """
    # Attributes:
    __id = 0  # (int)
    __root = None  # (Node)
    __numBranch = None  # (int)

    # Operations
    def __init__(self, treeString=None, tokenList=None):
        self.setId(self.__id+1)
        if treeString != None and tokenList != None:
            idNode = 0
            self.__tempNode = None
            self.__tokenList = tokenList
            self.setString(treeString)
            string = self.__treeString
            # scorro treeString per costruire l'albero
            for index in range(0, len(string)):
                if string[index] == "(":
                    word = self.__findWord(string, index+1)
                    #doNonLeaf
                    self.__tempNode = self.doNonLeaf(idNode, word, self.__tempNode)
                    idNode = idNode + 1
                    if word == "ROOT":
                        self.__root = self.__tempNode
                    index = index + len(word)
                elif string[index] == " ":
                    token = self.__findWord(string, index+1)
                    #doLeaf
                    self.doLeaf(idNode, token, self.__tempNode)
                    idNode = idNode + 1
                    index = index + len(token)
                elif string[index] == ")":
                    #goBack
                    self.__tempNode = self.__tempNode.getNode()
            self.__idNode = idNode

    def __findWord(self, string, index):
        """function findWord
        ricerca una parola all'interno della stringa
        ritorna la parola trovata

        returns String
        """
        word = ""
        for i in range(index, len(string)):
            if string[i] != "(" and string[i] != " " and string[i] != ")":
                word = word + string[i]
            else:
                break
        return word

    def setId(self, id):
        """function setId
        imposta il valore dell'id
        """
        self.__id = id
        return None # should raise NotImplementedError()

    def setString(self, treeString):
        """function setId
        imposta il valore dell'id
        """
        self.__treeString = ' '.join(str(treeString).split())
        self.__treeString = self.__treeString.replace(" (", "(")
        self.__treeString = self.__treeString.replace(" )", ")")
        return None # should raise NotImplementedError()

    def getId(self):
        """function detId
        ritorna l'id del ParseTree

        returns int
        """
        return self.__id

    def getString(self):
        """function getString
        ritorna la stringa dell'albero

        returns String
        """
        return self.__treeString

    def getRoot(self):
        """function getRoot
        ritorna il nodo radice

        returns Node
        """
        return self.__root

    def doNonLeaf(self, id, tag, node):
        """function doNonLeaf
        crea un nodo NonLeaf

        returns Node
        """
        newNode = NonLeaf(id, tag, node)
        if tag != "ROOT":
            node.addChild(newNode)
        return newNode # should raise NotImplementedError()

    def doLeaf(self, id, token, node):
        """function doLeaf
        crea un nodo Leaf

        returns Node
        """
        newLeaf = Leaf(id, token, node)
        node.addChild(newLeaf)
        return None # should raise NotImplementedError()

