import os
import sys
if os.name =="nt":
    sys.path.insert(0, "..\src\\")
else:
    sys.path.insert(0, "../src/")
from Grammar import Grammar

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetGrammar():
    print("Test per getGrammar")
    listValueExpected = [True, False]
    # test 1
    grammar = Grammar()
    value = grammar.getGrammar()
    assert value == listValueExpected[0], "Errore"
    # test 2
    grammar = Grammar()
    value = grammar.getGrammar("../fileGrammar.cfg")
    assert value == listValueExpected[1], "Errore"

def testLoadGrammar():
    print("Test per loadGrammar")
    listValueExpected = "<class 'nltk.grammar.CFG'>"
    # test 1
    grammar1 = Grammar()
    value = str(type(grammar1.loadGrammar()))
    assert value == listValueExpected, "Errore"

def testAddReq2Grammar():
    print("Test per addReq2Grammar")
    listValueExpected = True
    fileReq = open("../resources/req/requisito1.txt", "r")
    reqLine = []
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    # test
    grammar = Grammar()
    value = grammar.addReq2Grammar(reqLine)
    assert value == listValueExpected, "Errore"

def main():
    print("TestSuite della classe Grammar")
    # inizializzazione
    testGetGrammar()
    testLoadGrammar()
    testAddReq2Grammar()

if __name__ == "__main__":
    main()
