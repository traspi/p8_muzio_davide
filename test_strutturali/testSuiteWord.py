import os
import sys
sys.path.insert(0, "../src/")
from Word import Word

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetType():
    print("Test per getType")
    listExpectedValue = "Word"
    # test
    word = Word()
    value = word.getType()
    assert value == listExpectedValue, "Errore test"

def main():
    print("TestSuite per la classe Word")
    testGetType()

if __name__ == "__main__":
    main()