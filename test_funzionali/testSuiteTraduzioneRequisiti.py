import os
import sys
from unittest.mock import patch
sys.path.insert(0, "../src/")
from RequirementDef import RequirementDef
from Grammar import Grammar

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testCreazioneAlbero():
    print("Test per Creazione Albero Sintattico")
    # 2 casi
    # prendo in ingresso gli alberi che mi aspetto come output
    fileTree = open("resources/tree1.txt", "r")
    treeString1 = fileTree.readline()
    fileTree.close()
    fileTree = open("resources/tree2.txt", "r")
    treeString2 = fileTree.readline()
    fileTree.close()
    listExpectedValue =[treeString1, treeString2]
    # carico la grammatica
    grammar = Grammar()
    grammar.getGrammar()
    # leggo la i token del req 1
    reqLine = []
    fileReq = open("resources/requisito1.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    # li passo alla RequirementDef
    requirement1 = RequirementDef(1, reqLine)
    # aggiorno la grammatica
    grammar.addReq2Grammar(reqLine)
    # leggo la i token del req 2
    reqLine = []
    fileReq = open("resources/requisito2.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    # li passo alla RequirementDef
    requirement2 = RequirementDef(2, reqLine)
    # aggiorno la grammatica
    grammar.addReq2Grammar(reqLine)
    cfg = grammar.loadGrammar()

    # test 1
    parseTree1 = requirement1.createTreeList(cfg)
    assert parseTree1 == listExpectedValue[0], "Errore test 1"
    
    # test 2
    parseTree2 = requirement2.createTreeList(cfg)
    assert parseTree2 == listExpectedValue[1], "Errore test 2"

def main():
    print("Test per lo use case Traduzione Requisito")
    testCreazioneAlbero()

if __name__ == "__main__":
    main()
