#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe Grammar
"""

import os
import sys
sys.path.insert(0, "../lib/")

import nltk.data

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class Grammar:
    """Class Grammar
    rappresenta la grmmatica che per trasformare
    un requisito in ParseTree
    la grammatica viene costruita partendo da regole salvate su file cfg
    il lessico della grammatica viene preso dai token in ingresso
    """

    # Attributes:
    __langueage = None # (String)
    __type = "../resources/grammar/grammar.cfg"  # (String)
    __value = "../resources/grammar/grammarReq.cfg"  # (String)

    # Operations

    def __init__(self):
        self.__langueage = "English"

    def getGrammar(self, fileGrammar=None):
        """function getGrammar
        prende le regole delle grammatica da un file

        returns boolean
        """
        if fileGrammar == None:
            fileGrammar = self.__type
        try:
            # leggo il file
            with open(fileGrammar, "r") as ins:
                # copio le regole della grammatica in un nuovo file
                fileOut = open(self.__value, "w")
                for line in ins:
                    fileOut.write(line)
                fileOut.close()
        except:
            print("File non trovato")
            return False
        return True # should raise NotImplementedError()

    def loadGrammar(self, fileGrammar=None):
        """function loadGrammar
        ritorna la grammatica presa da file

        returns CFG
        """
        if fileGrammar == None:
            fileGrammar = self.__value
        # carico la grammatica da file
        return nltk.data.load("file:" + fileGrammar)

    def addReq2Grammar(self, requirement):
        """function addReq2Grammar
        aggiunge i token presi dai requisiti
        al file per formare la grammatica

        returns boolean
        """
        outFile = open(self.__value, "a")
        outFile.write("\n")
        # aggiungo i token nella grammatica
        for token in requirement:
            outFile.write(token[1] + " -> '" + token[0] + "'\n")
        outFile.close()
        return True


