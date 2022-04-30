# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:15:58 2019
    
@author: Aputer
Rosalind Project problem ID: IPRB
"""

def Dom_Prob(k,m,n):
    #function recives k items with 2 dominant alels
    #m items with 1 dominant and 1 recessive alels
    #n items with 2 recessive alels
    #returns probabilty that paring 2 random items will
    #result in an item with 1 dominant alel at least
    x=k+m+n
    return(k/x+(k*n+k*m+m*n)/(x*x-x)+(3*m*m-3*m)/(4*x*x-4*x))
print(Dom_Prob(2,2,2))