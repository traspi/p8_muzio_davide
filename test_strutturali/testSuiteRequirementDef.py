import os
import sys
from unittest.mock import patch
sys.path.insert(0, "../src/")
from RequirementDef import RequirementDef
from Grammar import Grammar

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetIndexWord(req):
    print("Test per getIndexWord")
    id = 0
    listExpectedValue = req
    # test
    requirement1 = RequirementDef(id, req)
    value = requirement1.getIndexWord()
    assert value == listExpectedValue, "Errore test"

def testCreateTreeList(req):
    print("Test per createTreeList")
    id = 0
    fileTree = open("resources/pattern1.txt", "r")
    treeString = fileTree.readline()
    fileTree.close()
    listExpectedValue = treeString
    # test
    grammar = Grammar()
    cfg = grammar.loadGrammar("resources/grammarReq.cfg")
    requirement2 = RequirementDef(id, req)
    value = requirement2.createTreeList(cfg)
    assert value == listExpectedValue, "Errore test"

def testGetToken(req):
    print("Test per getToken")
    listExpectedValue = None
    # test
    requirement = RequirementDef(0, req)
    value = requirement.getToken()
    assert value == listExpectedValue, "Errore test"

def testSyntacticCheck(req):
    print("Test per syntacticCheck")
    id = 0
    def inputMy(prompt):
        return next(inserimento)
    fileReq = open("resources/requisito2.txt", "r")
    reqLine = []
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    fileReq.close() 
    listExpectedValue = [req, reqLine]
    # test 1
    inserimento = (ri for ri in ["y"])
    with patch('builtins.input', inputMy):
        requirement3 = RequirementDef(id, reqLine)
    assert any(i in requirement3.getIndexWord() for i in listExpectedValue[0]), "Errore test 1"
    # test 2
    inserimento = (ri for ri in ["n"])
    with patch('builtins.input', inputMy):
        requirement3 = RequirementDef(id, reqLine)
    assert any(i in requirement3.getIndexWord() for i in listExpectedValue[1]), "Errore test 2"

def main():
    print("Test per la classe RequirementDef")
    fileReq = open("resources/requisito1.txt", "r")
    reqLine = []
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    fileReq.close()
    testGetIndexWord(reqLine)
    testCreateTreeList(reqLine)
    testGetToken(reqLine)
    testSyntacticCheck(reqLine)

if __name__ == "__main__":
    main()
