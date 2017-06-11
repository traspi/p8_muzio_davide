import os
import sys
sys.path.insert(0, "../src/")
from NonLeaf import NonLeaf
from Leaf import Leaf

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testAddChild():
    print("Test per addChild")
    nonLeaf1 = NonLeaf()
    nonLeaf2 = NonLeaf()
    listExpectedValue = [nonLeaf1, nonLeaf2]
    # test
    nonLeaf = NonLeaf()
    nonLeaf.addChild(nonLeaf1)
    nonLeaf.addChild(nonLeaf2)
    assert nonLeaf.getChildren()[0] == listExpectedValue[0], "Errore test 1"
    assert nonLeaf.getChildren()[1] == listExpectedValue[1], "Errore test 2"

def testGetChildren():
    print("Test per getChildren")
    nonLeaf1 = NonLeaf()
    nonLeaf2 = NonLeaf()
    listExpectedValue = [nonLeaf1, nonLeaf2]
    # test
    nonLeaf = NonLeaf()
    nonLeaf.addChild(listExpectedValue[0])
    nonLeaf.addChild(listExpectedValue[1])
    value1 = nonLeaf.getChildren()[0]
    value2 = nonLeaf.getChildren()[1]
    assert value1 == listExpectedValue[0], "Errore test 1"
    assert value2 == listExpectedValue[1], "Errore test 2"

def testPrintChildren():
    print("Test per printChildren")
    listExpectedValue = None
    # test
    nonLeaf = NonLeaf()
    nonLeaf1 = NonLeaf()
    nonLeaf2 = NonLeaf()
    nonLeaf1.addChild(nonLeaf2)
    nonLeaf.addChild(nonLeaf1)
    value = nonLeaf.printChildren()
    assert value == listExpectedValue, "Errore test"

def testNumBranch():
    print("Test per numBranch")
    listExpectedValue = [0, 1]
    # test 1
    nonLeaf = NonLeaf()
    value1 = nonLeaf.numBranch()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    leaf = Leaf()
    nonLeaf = NonLeaf()
    nonLeaf.addChild(leaf)
    value2 = nonLeaf.numBranch()
    assert value2 == listExpectedValue[1], "Errore test 2"

def testsetTag():
    print("Test per setTag")
    listExpectedValue = ["S", "SBAR"]
    nonLeaf = NonLeaf()
    # test 1
    nonLeaf.setTag(listExpectedValue[0])
    assert nonLeaf.getTag() == listExpectedValue[0], "Errore test 1"
    # test 2
    nonLeaf.setTag(listExpectedValue[1])
    assert nonLeaf.getTag() == listExpectedValue[1], "Errore test 2"

def testGetTag():
    print("Test per getTag")
    listExpectedValue = ["NP", "VP"]
    nonLeaf = NonLeaf()
    # test 1
    nonLeaf.setTag(listExpectedValue[0])
    value1 = nonLeaf.getTag()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    nonLeaf.setTag(listExpectedValue[1])
    value2 = nonLeaf.getTag()
    assert value2 == listExpectedValue[1], "Errore test 2"

def main():
    print("TestSuite per la classe NonLeaf")
    testAddChild()
    testGetChildren()
    testPrintChildren()
    testNumBranch()
    testsetTag()
    testGetTag()

if __name__ == "__main__":
    main()
