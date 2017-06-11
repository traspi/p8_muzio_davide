#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Modulo che contiene la classe RquirementDef
che gestisce il singolo requisito
"""

from SyntacticTreeList import SyntacticTreeList
from Statement import Statement
from Word import Word
from ValueType import ValueType
from SignalName import SignalName
from IDRequirement import IDRequirement

__author__ = "Davide Muzio"
__version__ = "1.0.0"

class RequirementDef(Statement):
    """Class RequirementDef
    rappresenta l'insieme dei token di un requisito
    """
    # Attributes:
    __requirement = None  # (String)
    __valido = None  # (boolean)
    __indexKeyWord = []  # ([0_*] int)

    # Operations
    def __init__(self, id, req):
        self.__valido = True
        self.__indexKeyWord = []
        self.setId(id)
        for t in req:
            self.__indexKeyWord.append(t)
        self.syntacticCheck()
        self.__tokenList = self.__createToken(req)

    def __createToken(self, reqLine):
        """function createToken
        crea i token partendo da una lista
        che contiene i token e i tag

        returns Token[]
        """
        tokenList = []
        # creazione del tipo di token per ogni token
        for token in reqLine:
            if token[1] == "REQ":
                temp = IDRequirement(token[0], token[1])
            elif token[1] == "SIG":
                temp = SignalName(token[0], token[1])
            elif token[1] == "VT":
                temp = ValueType(token[0], token[1])
            else:
                temp = Word(token[0], token[1])
            tokenList.append(temp)
        return tokenList

    def getIndexWord(self):
        """function getIndexWord
        ritorna le indexKeyWord

        returns String[]
        """
        return self.__indexKeyWord

    def getToken(self):
        """function getToken
        funzione non implementata visto che i token
        sono stati passati come paramentro della chiamata
        di createTreee
        returns Token
        """
        return None # should raise NotImplementedError()

    def createTreeList(self, cfg):
        """function createTreeList
        ritorna il parseTree sottoforma di stringa
        returns String
        """
        tree = SyntacticTreeList(self.getId())
        parseTree = tree.createTree(cfg, self.__tokenList, self.getId())
        return parseTree # should raise NotImplementedError()

    def __syntacticRules(self):
        """function syntacticRules
        inizializza le regole sintattiche da rispettare

        returns String[]
        """
        rules = []
        rules.append(["MD", "REQ"])
        rules.append(["JJR", "IN"])
        return rules

    def syntacticCheck(self):
        """function syntacticCheck
        contralla che siano rispettate le regole sintatiche
        chiedendo all'utente di intervenire in caso di problemi
        rispettare le regole consente una migliore trasformazione
        del requisito in ParseTree
        """
        string = ""
        for word in self.__indexKeyWord:
            string = string + word[0] + " "
        rules = self.__syntacticRules()
        # scorro le regole e controllo che venga rispettata
        for rule in rules:
            for index, token in enumerate(self.__indexKeyWord):
                if len(rule) == 2:
                    if rule[0] == token[1] and rule[1] != self.__indexKeyWord[index+1][1]:
                        for i, t in enumerate(self.__indexKeyWord):
                            if rule[1] == self.__indexKeyWord[i][1]:
                                print("Errore : '"+self.__indexKeyWord[index+1][0], end=" ")
                                print("' al posto di '"+self.__indexKeyWord[i][0]+"'")
                                print("Nella frase :  "+string)
                                resp = input("Se desidera modificare il requisito premere y : ")
                                if resp == "y" or resp == "Y":
                                    self.__modifyPosTag(index+1, i)
                                else:
                                    print("Il requisito non verrà modificato", end=" ")
                                    print("e potrebbe esserci un errore")
        return None # should raise NotImplementedError()

    def __modifyPosTag(self, first, second):
        """function modifyPosTag
        modiica dei token per la risoluzione
        """
        swap = []
        swap = self.__indexKeyWord[first]
        self.__indexKeyWord[first] = self.__indexKeyWord[second]
        self.__indexKeyWord[second] = swap
        return None # should raise NotImplementedError()
