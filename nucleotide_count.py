# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:11:19 2019

@author: Aputer
Rosalind Project problem ID: DNA
"""
def nucleotide_count(sequence):
    bases={'A':0,'T':0,'G':0,'C':0}
    for nucleotide in sequence:
        if(nucleotide=='A'):
            bases['A']+=1
        elif(nucleotide=='T'):
            bases['T']+=1
        elif(nucleotide=='G'):
            bases['G']+=1
        elif(nucleotide=='C'):
            bases['C']+=1
    return(bases)

