import os
import sys
sys.path.insert(0, "../src/")
from Statement import Statement

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testSetId():
    print("Test per setId")
    listValueExpected = [1, 2]
    stmt = Statement()
    # test 1
    stmt.setId(listValueExpected[0])
    assert stmt.getId() == listValueExpected[0], "Errore test 1"
    # test 2
    stmt.setId(listValueExpected[1])
    assert stmt.getId() == listValueExpected[1], "Errore test 2"

def testGetId():
    print("Test per getId")
    listValueExpected = [3, 4]
    stmt = Statement()
    # test 1
    stmt.setId(listValueExpected[0])
    value1 = stmt.getId()
    assert value1 == listValueExpected[0], "Errore test 1"
    # test 2
    stmt.setId(listValueExpected[1])
    value1 = stmt.getId()
    assert value1 == listValueExpected[1], "Errore test 2"

def main():
    print("TestSuite della classe Statement")
    testSetId()
    testGetId()

if __name__ == "__main__":
    main()
