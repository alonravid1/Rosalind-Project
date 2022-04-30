# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:49:42 2021

@author: Aputer

Rosalind project ID: LIA
"""
import math

def probability(k,n):
    #given k<=7, n=2^k, calculates the probability of there being at least n
    #offsprings at the kth generation with Aa Bb genotype given that the
    #parent at generation 0 has Aa Bb genotype and 2 children, and each
    #offspring mates with a dihybrid as well to produce 2 offsprings.
    #the probability is calculated by adding the binomial distribution 
    #probability of all possibilites up to n, and then taking the complement.
    
    offsprings = pow(2,k)
    p = 0
    for i in range(n):
        p += math.comb(offsprings,i)*pow(0.25,i)*pow(0.75,offsprings-i)
    return(1-p)

print(probability(6,17))