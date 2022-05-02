# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:08:55 2022

@author: Aputer

Rosalind project ID: KMER

There were several similar premutation problems of all sorts,
their solutions were quite specific and simply printed their output, limiting their use.
Here i have wrote a function which appends each solution and returns them as a list,
allowing a more general use in the future.
"""

import bio

def get_kmers(k, permutation = "", output = [], alphabet = ['A', 'C', 'G', 'T']):
    #appends ot the output list all k-mers of a given alphabet, the default being the 4 nucleotide bases,
    #ordered lexicographically according to standard english alphabet.
    
    if(len(permutation) == k-1):
        
        for char in alphabet:
            
            output.append(permutation+char)

    else:
        
        for char in alphabet:
            
            get_kmers(k, permutation+char, output, alphabet)
    
    return(output)

def k_mer_composition(k, s):
    k_mers = get_kmers(k)
    composition = []
    for k_mer in k_mers:
        composition.append(len(bio.rabin_karp_search(k_mer, s)))
    return(composition)
        
s = """CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG""".replace("\n","")

print(str(k_mer_composition(4, s))[1:-1].replace(',', ''))
