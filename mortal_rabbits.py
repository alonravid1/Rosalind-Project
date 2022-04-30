# -*- coding: utf-8 -*-
"""
@author: Aputer

Rosalind Project problem ID: FIBD
"""
def Mortal_Rabits(n,m):
    generation_sizes = [1]
    adult_rabbits = 1
    
    for i in range(1, m):
        generation_sizes.append(adult_rabbits - generation_sizes[i - 1])
        adult_rabbits += generation_sizes[i]
        
    for j in range(m, n):
        generation_sizes.append(adult_rabbits - generation_sizes[j - 1])
        adult_rabbits += generation_sizes[j]  - generation_sizes[j - m]
        
    print(generation_sizes)
    print(adult_rabbits)
    
Mortal_Rabits(96,19)