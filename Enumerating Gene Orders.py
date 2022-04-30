"""
@author: Aputer

Rosalind Project problem ID: PERM
"""
def factorial(n):
    if(n<2):
        return(1)
    return(n*factorial(n-1))



def permutations(permutation, picks):
    
    if(len(picks) == 1):
        
        permutation.append(picks[0])
        print(*permutation)

    for i in range(len(picks)):
        
        temp_perm = permutation.copy()
        temp_perm.append(picks[i])
        temp_picks = picks.copy()
        del(temp_picks[i])
        permutations(temp_perm, temp_picks)
        


def print_output(n):
    
       print(factorial(n))
       array = list(range(1,n+1))
       permutations([], array)
       
               

print_output(5)