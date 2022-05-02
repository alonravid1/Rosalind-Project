# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:19:47 2021

@author: Aputer
Rosalind project ID: LGIS

A slow solution utilizing dynamic programming with a running time of
O(n^2). This was my intial solution, but since it was so slow i had decided to
wirte a better one after seeing that there is a faster non DP approach
for this problem. It can be found in the ELIS file.
"""
import numpy as np
import time
start_time = time.time()

def increasing_sequence(perm, n):
    #receives a permutation of numbers from 1 to n, returns the longest
    #increasing subsequence
    
    sequences = np.ones(n, dtype = int)
    
    for i in range(n):
        #goes through each elemnt in the permutation
    
            for j in range(i):
              #checks for each previous element in the permutation if its
              #smaller and if it's subsequence length is greater than
              #its current length. if so, it takes it as it's own and adds 1
            
                if(perm[i] > perm[j] and sequences[i] < sequences[j]+1):
                    
                    sequences[i] = sequences[j]+1
                    
    maximum = 1
    
    for i in range(n):
        #sets maximum to the longest increasing subsequence's length    
        maximum = max(maximum, sequences[i])
    
    longest_seq = np.zeros(maximum+1, dtype=int)
    longest_seq[maximum] = n+1
    
    for i in range(n-1, 0, -1):
        #goes through the resulting lengths array, finds the largest element
        #with a subsequence length equal to the current maximum, adds it to
        #resulting sequence and removes one from the maximum, thus recreating
        #a valid longest subsequence
        
        if(sequences[i] == maximum and perm[i].astype(int) <
           longest_seq[maximum]):
            
            longest_seq[maximum-1] = perm[i].astype(int)
            maximum -= 1
            
        if(maximum == 0):
            break
        
    return(longest_seq[0:-1])
            
def decreasing_sequence(perm, n):
    
    sequences = np.ones(n, dtype = int)
    
    for i in range(n):
        #goes through each elemnt in the permutation    
            for j in range(i):
                #checks for each previous element in the permutation if its
                #larger and if it's subsequence length is greater than
                #its current length. if so, it takes it as it's own and adds 1
                
                if(perm[i] < perm[j] and sequences[i] < sequences[j]+1):
                    
                    sequences[i] = sequences[j]+1
                    
    maximum = 1
    
    for i in range(n):
        #sets maximum to the longest decreasing subsequence's length
        maximum = max(maximum, sequences[i]) 
        
    longest_seq = np.zeros(maximum, dtype = int)
    
    for i in range(n-1, 0, -1):
        #goes through the resulting lengths array, finds the smallest element
        #with a subsequence length equal to the current maximum, adds it to
        #resulting sequence and removes one from the maximum, thus recreating
        #a valid longest subsequence
            
        if(sequences[i] == maximum and perm[i].astype(int) > longest_seq[maximum-1]):
            
            longest_seq[maximum-1] = perm[i].astype(int)
            maximum -= 1
            
        if(maximum == 0):
            break
        
    return(longest_seq)                

file = open(path,'r')
n = file.readline()
n = int(n)
permutation = file.read()

permutation = permutation.replace("\n", "")
permutation = np.fromstring(permutation, dtype = int, sep = ' ')


print(*increasing_sequence(permutation, n))

print(*decreasing_sequence(permutation, n))
 

file.close()
