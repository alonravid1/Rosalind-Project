# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:20:55 2021

@author: Aputer

Rosling Project ID: PROB
"""
import bio
import math

def get_bases_probabilites(GC):  
    
    AT = (1-GC)/2
    GC = GC/2
    return({'A':AT, 'T':AT, 'G':GC, 'C':GC})


def probabilty_common_logarithm(strand, GC_contents):
    
    bases = bio.nucleotide_count(strand)
    
    strand_GC = ((bases['G']+bases['C'])/
                 (bases['G']+bases['C']+bases['A']+bases['T']))
    
    strand_match_probability = []
    
    for GC in GC_contents:
        
        base_probability = get_bases_probabilites(GC)
        probability = 1
        
        for base in strand:
            
            probability = probability * base_probability[base]
            
        strand_match_probability.append(math.log(probability,10))
        
    return(strand_match_probability)
        
        
        

    
contents = "0.093 0.120 0.210 0.237 0.330 0.379 0.416 0.471 0.503 0.598 0.653 0.668 0.731 0.806 0.884 0.904".split(' ')
GC_contents = []
for i in range(len(contents)):
    GC_contents.append((float)(contents[i]))

x = probabilty_common_logarithm("TGTCACCTACCTAGTCTCAGCTTTCTGTTACTCGTTTTGATGGCCCTGAACTGGTCGCTATCTTATTCCTGGTAGCAGAAATTCTTT", GC_contents)

print(str(x)[1:-1].replace(',', ''))