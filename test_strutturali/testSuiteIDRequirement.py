import os
import sys
sys.path.insert(0, "../src/")
from IDRequirement import IDRequirement

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetType():
    print("Test per getType")
    listExpectedValue = "ID Requirement"
    # test
    id = IDRequirement()
    value = id.getType()
    assert value == listExpectedValue, "Errore test"

def main():
    print("TestSuite per la classe IDRequirement")
    testGetType()

if __name__ == "__main__":
    main()