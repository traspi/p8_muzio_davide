import os
import sys
from unittest.mock import patch
sys.path.insert(0, "../src/")
from RequirementDef import RequirementDef

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def testRisoluzioneAmbiguitaSintattica():
    print("Test per la Risoluzione Ambiguita' Sintattica")
    def inputMy(prompt):
        return next(inserimento)
    # leggo la lista di token corretta
    reqLine = []
    fileReq = open("resources/requisito1.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    listExpectedValue = reqLine
    # leggo la lista di token da analizzare
    reqLine = []
    fileReq = open("resources/requisito3.txt", "r")
    for line in fileReq.readlines():
        newLine = line.strip("\n")
        splitLine = newLine.split()
        reqLine.append(splitLine)
    # test
    # creo un requisito con la lista di token
    inserimento = (ri for ri in ["y"])
    with patch('builtins.input', inputMy):
        requirement = RequirementDef(1, reqLine)
    value = requirement.getIndexWord()
    assert any(i in value for i in listExpectedValue), "Errore test 1"

def main():
    print("Test per lo use case Risoluzione Segnalazioni")
    testRisoluzioneAmbiguitaSintattica()

if __name__ == "__main__":
    main()
