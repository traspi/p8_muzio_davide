import os
import sys
sys.path.insert(0, "../src/")
from SyntacticTreeList import SyntacticTreeList
from Grammar import Grammar
from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testCreateTree1():
    print("Test per createTree")
    fileTree = open("resources/pattern1.txt", "r")
    treeString = fileTree.readline()
    fileTree.close()
    listExpectedValue = treeString
    # test
    id = 0
    grammar = Grammar()
    cfg = grammar.loadGrammar("resources/grammarReq.cfg")
    tokenList = []
    fileReq = open("resources/requisito1.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        token = Token()
        token.setValue(splitLine[0])
        tokenList.append(token)
    treeList = SyntacticTreeList()
    value = treeList.createTree(cfg, tokenList, id)
    assert value == listExpectedValue, "Errore test"

def testCreateTree2():
    print("Test per createTree")
    fileTree = open("resources/pattern1.txt", "r")
    treeString = fileTree.readline()
    fileTree.close()
    listExpectedValue = treeString
    # test
    id = 0
    grammar2 = Grammar()
    cfg2 = grammar2.loadGrammar("resources/grammarReq2.cfg")
    tokenList = []
    fileReq = open("resources/requisito1.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        token = Token()
        token.setValue(splitLine[0])
        tokenList.append(token)
    treeList = SyntacticTreeList()
    value = treeList.createTree(cfg2, tokenList, id)
    assert value == listExpectedValue, "Errore test"

def main():
    print("Test per la classe SyntacticTreeList")
    testCreateTree1()
    testCreateTree2()

if __name__ == "__main__":
    main()