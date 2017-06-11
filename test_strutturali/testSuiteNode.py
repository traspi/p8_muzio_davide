import os
import sys
sys.path.insert(0, "../src/")
from Node import Node

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testSetId():
    print("Test per setId")
    listExpectedValue = [1, 2]
    node = Node()
    # test 1
    node.setId(listExpectedValue[0])
    assert node.getId() == listExpectedValue[0], "Errore test 1"
    # test 2
    node.setId(listExpectedValue[1])
    assert node.getId() == listExpectedValue[1], "Errore test 2"

def testGetId():
    print("Test per getId")
    listExpectedValue = [3, 4]
    node = Node()
    # test 1
    node.setId(listExpectedValue[0])
    value1 = node.getId()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    node.setId(listExpectedValue[1])
    value2 = node.getId()
    assert value2 == listExpectedValue[1], "Errore test 2"

def testSetNode():
    print("Test per setNode")
    node1 = Node()
    node2 = Node()
    listExpectedValue = [node1, node2]
    node = Node()
    # test 1
    node.setNode(listExpectedValue[0])
    assert node.getNode() == listExpectedValue[0], "Errore test 1"
    # test 2
    node.setNode(listExpectedValue[1])
    assert node.getNode() == listExpectedValue[1], "Errore test 2"

def testGetNode():
    print("Test per getNode")
    node1 = Node()
    node2 = Node()
    listExpectedValue = [node1, node2]
    node = Node()
    # test 1
    node.setNode(listExpectedValue[0])
    value1 = node.getNode()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    node.setNode(listExpectedValue[1])
    value2 = node.getNode()
    assert value2 == listExpectedValue[1], "Errore test 2"

def main():
    print("TestSuite per la classe Node")
    testSetId()
    testGetId()
    testSetNode()
    testGetNode()

if __name__ == "__main__":
    main()
