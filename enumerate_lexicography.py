# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:15:59 2021

@author: Aputer
Rosalind Project problem ID: LEXF
"""

def permutate(alphabet, permutation, n):
    #prints all permutations of a given length n, according to a given
    #alphabet, ordered lexicographically according to standard english alphabet
    
    if(len(permutation) == n-1):
        
        for char in alphabet:
            
            print(permutation+char)
            
    else:
        
        for char in alphabet:
            
            permutate(alphabet, permutation+char, n)
    
    
    
sample = "A T C G".split()
sample.sort()
print(sample)
permutate(sample, '', 2)