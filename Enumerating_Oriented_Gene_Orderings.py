# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:49:36 2021

@author: Aputer

Rosalind project ID: SIGN

"""
def factorial(n):
    if(n<2):
        return(1)
    return(n*factorial(n-1))


output =[]

def permutations(permutation, picks, output):
    #the recursive function calls for itself twice for each member in the picks
    #set. each call it gives the current permutation with a single additional 
    #member from picks, once call as it is and one call with it as a negative
    #number until there is only one member to pick, then it adds it to the output list.
    
    
    
    if(len(picks) == 1):
        
        positive_perm = permutation.copy()
        positive_perm.append(picks[0])
        output.append(positive_perm)
        
        permutation.append(-picks[0])
        output.append(permutation)
        return(output)

    for i in range(len(picks)):
        
        positive_perm = permutation.copy()
        positive_perm.append(picks[i])
        positive_picks = picks.copy()
        del(positive_picks[i])
        
        permutations(positive_perm, positive_picks, output)
        
        negative_perm = permutation.copy()
        negative_perm.append(-picks[i])
        negative_picks = picks.copy()
        del(negative_picks[i])
        
        permutations(negative_perm, negative_picks, output)
        
        
    return(output)
    
n=2
#prints number of possbilites
print(factorial(n)*(2**n))

#prints all premutations
array = list(range(1,n+1))
print(permutations([], array, output))