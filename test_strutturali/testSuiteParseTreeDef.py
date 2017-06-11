import os
import sys
sys.path.insert(0, "../src/")
from ParseTreeDef import ParseTreeDef
from Node import Node
from NonLeaf import NonLeaf
from Leaf import Leaf
from Token import Token

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testSetId():
    print("Test per setId")
    listExpectedValue = [1, 2]
    tree = ParseTreeDef()
    # test 1
    tree.setId(listExpectedValue[0])
    assert tree.getId() == listExpectedValue[0], "Errore test 1"
    # test 2
    tree.setId(listExpectedValue[1])
    assert tree.getId() == listExpectedValue[1], "Errore test 2"

def testGetId():
    print("Test per getId")
    listExpectedValue = [11, 12]
    tree = ParseTreeDef()
    # test 1
    tree.setId(listExpectedValue[0])
    value1 = tree.getId()
    assert value1 == listExpectedValue[0], "Errore test 1"
    # test 2
    tree.setId(listExpectedValue[1])
    value2 = tree.getId()
    assert value2 == listExpectedValue[1], "Errore test 2"

def testSetString():
    print("Test per setString")
    treeString = "(ROOT(NP(SIG Signal))(VP(MD shall)(PRN(NP(REQ Req1)))(VP(VB be)(VP(VBN set)(PP(TO to)(ADJP(VT 0)))))))"
    listExpectedValue = treeString
    tree = ParseTreeDef()
    # test
    tree.setString(treeString)
    assert tree.getString() == listExpectedValue, "Errore test"

def testGetString():
    print("Test per getString")
    treeString = "(ROOT(NP(SIG Signal))(VP(MD shall)(PRN(NP(REQ Req1)))(VP(VB be)(VP(VBN set)(PP(TO to)(ADJP(VT 0)))))))"
    listExpectedValue = treeString
    tree = ParseTreeDef()
    # test
    tree.setString(treeString)
    value = tree.getString()
    assert value == listExpectedValue, "Errore test"

def testGetRoot():
    print("Test per getRoot")
    listExpectedValue = "ROOT"
    # test
    treeString ="(ROOT(NP(SIG Signal))(VP(VBZ becomes)(ADJP(VT 1))))"
    tokenList = []
    tree = ParseTreeDef(treeString, tokenList)
    value = tree.getRoot().getTag()
    assert value == listExpectedValue, "Errore test"

def TestDoNonLeaf():
    print("Test per NonLeaf")
    id1 = 1
    tag1 = "ROOT"
    node1 = NonLeaf()
    id2 = 2
    tag2 = "S"
    node2 = NonLeaf()
    listExpectedValueTag = [tag1, tag2]
    tree = ParseTreeDef()
    # test 1
    newNode1 = tree.doNonLeaf(id1, tag1, node1)
    valueTag1 = newNode1.getTag()
    assert valueTag1 == listExpectedValueTag[0], "Errore test 1"
    # test 2
    newNode2 = tree.doNonLeaf(id2, tag2, node2)
    valueTag2 = newNode2.getTag()
    assert valueTag2 == listExpectedValueTag[1], "Errore test 2"

def testDoLeaf():
    print("Test per doLeaf")
    id = 1
    token = Token()
    token.setPosTag("NN")
    node = NonLeaf()
    listExpectedValue = token.getPosTag()
    # test
    tree = ParseTreeDef()
    tree.doLeaf(id, token, node)
    value = node.getChildren()[0].getTag()
    assert value == listExpectedValue, "Errore test"

def main():
    print("Test per la classe ParseTreeDef")
    testSetId()
    testGetId()
    testSetString()
    testGetString()
    testGetRoot()
    TestDoNonLeaf()
    testDoLeaf()

if __name__ == "__main__":
    main()