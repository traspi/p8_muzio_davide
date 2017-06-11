import os
import sys
sys.path.insert(0, "../src/")
from ValueType import ValueType

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetType():
    print("Test per getType")
    listExpectedValue = "Value"
    # test
    valType = ValueType()
    value = valType.getType()
    assert value == listExpectedValue, "Errore test"

def main():
    print("TestSuite per la classe ValueType")
    testGetType()

if __name__ == "__main__":
    main()