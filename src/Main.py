#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Inizializzo i requisiti in ingresso
gli passo i token attravero file txt
"""
from RequirementDef import RequirementDef
from Grammar import Grammar

__author__ = "Davide Muzio"
__version__ = "1.0.0"

def main():
    start = 1 # numero requisito iniziale
    numReq = 12 # numero requisito finale
    requirements = []
    grammar = Grammar() # inizialiazzaione grammatica
    if not grammar.getGrammar():
        exit(1)
    # apertura file on requisiti e memorizzazione token
    for req in range(start, numReq+1):
        fileReq = open("../resources/req/requisito"+str(req)+".txt", "r")
        reqLine = []
        for line in fileReq.readlines():
            newLine = line.strip("\n")
            splitLine = newLine.split()
            reqLine.append(splitLine)
        requirement = RequirementDef(req, reqLine)
        requirements.append(requirement)
        grammar.addReq2Grammar(reqLine)
    cfg = grammar.loadGrammar() # caricamento grammatica
    # creazione ParseTree per ogni requisito
    i = start
    for req in requirements:
        parseTree = req.createTreeList(cfg)
        print(parseTree)
        print("\n")
        fileOut = open("../resources/tree/pattern"+ str(i) +".txt", "w")
        fileOut.write(parseTree)
        fileOut.close()
        i = i + 1

main()
