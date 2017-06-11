import os
import sys
sys.path.insert(0, "../src/")
from SignalName import SignalName

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testGetType():
    print("Test per getType")
    listExpectedValue = "Signal"
    # test
    sig = SignalName()
    value = sig.getType()
    assert value == listExpectedValue, "Errore test"

def main():
    print("TestSuite per la classe SignalName")
    testGetType()

if __name__ == "__main__":
    main()