# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:01:56 2019

@author: Aputer

Rosalind Project problem ID: ORF
"""

import bio

        
def find_ORF(strand):
    #function receives a DNA or an RNA sequence, returns a set of all possible proteins
    #encoded by the sequence
    
    proteins = []
    strand = bio.transcribe_DNA(strand)
    reversed_strand = bio.reverse_compliment_RNA(strand)
    

    for pos in range(len(strand)-1):
        
        if(strand[(pos):(pos+3)] == 'AUG'):
            
            proteins.append(bio.translate_RNA(strand[(pos):]))
                
        if(reversed_strand[(pos):(pos+3)] == 'AUG'):
            
            proteins.append(bio.translate_RNA(reversed_strand[(pos):]))
                
    proteins = set(proteins)
    
    if(None in proteins):
    
        proteins.remove(None)
        
    return(proteins)

#==============================================================================
# Inputs  
#bio.get_fasta_file(removed path since it was for a file on my computer)
#with open() as file:
    #dna=biolib.seg_fasta(file)[0]  
sample = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
#==============================================================================
#main

pro=find_ORF(sample)
for line in pro:
    print(line)

#bio.archive()

