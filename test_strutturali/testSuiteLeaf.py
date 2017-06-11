import os
import sys
sys.path.insert(0, "../src/")
from Leaf import Leaf
from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetTag():
    print("Test per getTag")
    token = Token()
    listExpectedValue = "S"
    token.setPosTag(listExpectedValue)
    # test
    leaf = Leaf()
    leaf.setToken(token)
    value = leaf.getTag()
    assert value == listExpectedValue, "Errore test"

def testSetToken():
    print("Test per setToken")
    token = Token()
    listExpectedValue = token
    # test
    leaf = Leaf()
    leaf.setToken(listExpectedValue)
    assert leaf.getToken() == listExpectedValue, "Errore test"

def testGetToken():
    print("Test per getToken")
    token = Token()
    listExpectedValue = token
    # test
    leaf = Leaf()
    leaf.setToken(listExpectedValue)
    value = leaf.getToken()
    assert value == listExpectedValue, "Errore test"

def testNumBranch():
    print("Test per numBranch")
    listExpectedValue = 0
    # test
    leaf = Leaf()
    value = leaf.numBranch()
    assert value == listExpectedValue, "Errore test"

def main():
    print("Test per la classe Leaf")
    testGetTag()
    testSetToken()
    testGetToken()
    testNumBranch()

if __name__ == "__main__":
    main()
