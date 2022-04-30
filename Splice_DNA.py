# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:58:39 2021

@author: Aputer

Rosalind Project problem ID: SPLC
"""
import bio

def splice_DNA(path):
    #receives a path to a fasta file containing a DNA sequence as its
    #first entry and introns as all other entreis. removes the introns from
    #the sequence and returns the protein product
    file = open(path,'r')
    fasta = bio.seg_fasta(file)
    file.close()
    sequence = fasta.pop(0)
    
    for intron in fasta:
        
        sequence = sequence.replace(intron, '')
        
    protein = bio.translate_DNA(sequence)
    return(protein)

#print(splice_DNA(path))
