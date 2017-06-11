import os
import sys
sys.path.insert(0, "../src/")
from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetType():
    print("Test per getType")
    listExpectedValue = None
    token = Token()
    # test
    value = token.getType()
    assert value == listExpectedValue, "Errore test"

def testGetValue():
    print("Test per getValue")
    listExpectedValue = ["word", "token"]
    token = Token()
    # test 1
    token.setValue(listExpectedValue[0])
    value1 = token.getValue()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    token.setValue(listExpectedValue[1])
    value2 = token.getValue()
    assert value2 == listExpectedValue[1], "Errore test 2"

def testSetValue():
    print("Test per setValue")
    listExpectedValue = ["words", "tokens"]
    token = Token()
    # test 1
    token.setValue(listExpectedValue[0])
    assert token.getValue() == listExpectedValue[0], "Errore test 1"
    # test2
    token.setValue(listExpectedValue[1])
    assert token.getValue() == listExpectedValue[1], "Errore test 2"

def testGetPosTag():
    print("Test per getPosTag")
    listExpectedValue = ["S", "SBAR"]
    token = Token()
    # test 1
    token.setPosTag(listExpectedValue[0])
    value1 = token.getPosTag()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    token.setPosTag(listExpectedValue[1])
    value2 = token.getPosTag()
    assert value2 == listExpectedValue[1], "Errore test 2"

def testSetPosTag():
    print("Test per setPosTag")
    listExpectedValue = ["NP", "VP"]
    token = Token()
    # test 1
    token.setPosTag(listExpectedValue[0])
    assert token.getPosTag() == listExpectedValue[0], "Errore test 1"
    # test2
    token.setPosTag(listExpectedValue[1])
    assert token.getPosTag() == listExpectedValue[1], "Errore test 2"

def main():
    print("TestSuite per la classe Token")
    testGetType()
    testGetValue()
    testSetValue()
    testGetPosTag()
    testSetPosTag()

if __name__ == "__main__":
    main()
