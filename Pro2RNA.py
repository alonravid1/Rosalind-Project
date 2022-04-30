# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:24:40 2019

@author: Aputer

Rosalind Project problem ID: MRNA
"""
def RNA_pos(protein):
    amino_acids={"F":2,"L":6,"S":6,"Y":2,"C":2,
                 "W":1,"P":4,"H":2,"Q":2,"R":6,
                 "I":3,"M":1,"T":4,"N":2,"K":2,
                 "V":4,"A":4,"D":2,"E":2,"G":4}
    combo=1
    for char in protein:
        combo=combo*amino_acids[char]
    combo=combo*3
    return(combo%1000000)
print(RNA_pos("MA"))
