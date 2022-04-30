# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 09:42:09 2021

@author: Aputer

Rosalind Project problem ID: LSCM

this algorithm is highly inefficient but was initially used on an extremly
small dataset. After needing to apply it to more problems I had begun
looking into more efficient solutions.
"""
import bio

def find_DNA_motif(path):
    #recieves a path to a fasta file of DNA strands and returns a list of all
    #longest common substrings
    file = open(path, "r")
    fasta = bio.seg_fasta(file)
    file.close()
    top_motifs = [""]
    
    for i in range(1,len(fasta[0])-1):
        
        for j in range(len(fasta[0])-i):
            
            is_motif = 0
            current_motif = fasta[0][j:j+i+1]
                        
            for DNA in fasta:
                
                if(current_motif in DNA == -1):
                    
                    is_motif = -1
                    break
            
            if(is_motif == 0):
                
                if(len(top_motifs[0]) < len(current_motif)):
    
                    top_motifs = []
                    top_motifs.append(current_motif)
                    
                    
                else:
                    
                    top_motifs.append(current_motif)
                
                    
                    
    return(top_motifs)

find_DNA_motif()           
            
                