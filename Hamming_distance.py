# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:09:41 2019

@author: Aputer

Rosalind Project problem ID: HAMM
"""
def dH(s,t):
    #recives 2 strings and returns the minimum
    #number of single character replacments needed
    #to compare the strings
    d=0
    for x in range(len(s)):
        if(s[x]!=t[x]):
            d+=1
    return(d)
