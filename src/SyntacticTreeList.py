#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe SyntacticTreeList
"""

import os
import sys
sys.path.insert(0, "../lib/")
from ParseTreeDef import ParseTreeDef
from Token import Token
from Grammar import Grammar
from nltk.parse import ChartParser

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class SyntacticTreeList:
    """Class SyntacticTreeList
    rappresenta la lista di ParseTree
    in cui puo' essere tradotto un requisito
    """
    # Attributes:
    __id = 0  # (int)
    __numTree = 0  # (int)

    # Operations

    def __init__(self, id=0):
        self.__id = id

    def createTree(self, cfg, tokenList, id):
        """function createTree
        crea una lista di parseTree
        partendo della lista dei token del requisito
        ritorna il miglior parseTree in sottoforma di stringa
        returns String
        """
        token = []
        # crea la lista di token del requisito
        for t in tokenList:
            token.append(t.getValue())
        chartParser = ChartParser(cfg)
        treeList = []
        i = 1
        #crea i possibili parseTree usando il chartParser
        for t in chartParser.parse(token):
            treeList.append(t)
        treeString = []
        # normalizza i parseTree per analizzarli
        for singleTree in treeList:
            req = []
            temp = ' '.join(str(singleTree).split())
            treeString.append(temp)
        parseTree = []
        # crea la lista di parseTree
        for sigleTree in treeString:
            tree = ParseTreeDef(singleTree, tokenList)
            parseTree.append(tree)
        # seleziona il miglior parseTree
        bestTree = self.__selectBestTree(parseTree)
        return bestTree.getString() # should raise NotImplementedError()

    def __selectBestTree(self, parseTree):
        """function selectBestTree
        seleziona il miglior parseTree
        selezionando quello che si estende
        maggiormente in profondita'

        returns ParseTree
        """
        tree = []
        tree = parseTree
        childrenRoot = []
        # controllo il numero dei figli del root di ogni albero
        for t in tree:
            childrenRoot.append(len(t.getRoot().getChildren()))
        minNumChildren = min(childrenRoot)
        bestTree = []
        # analizzo gli alberi che hanno il minor numero di figli della radice
        for t in tree:
            if len(t.getRoot().getChildren()) == minNumChildren:
                bestTree.append(t)
        if len(bestTree) == 1:
            return bestTree[0]
        else:
            best = None
            maxNum = 0
            maxList = []
            for t in range(0, len(bestTree)):
                maxList.append(0)
            for i in range(0, minNumChildren):
                for t in range(0, len(bestTree)):
                    branch = bestTree[t].getRoot().getChildren()[i]
                    num = branch.numBranch()
                    maxList[t] = maxList[t] + num
            for t in range(0, len(bestTree)):
                if maxList[t] > maxNum:
                    best = t
            return bestTree[best]

