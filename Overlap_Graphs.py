# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:59:44 2019

@author: Aputer

Rosalind Project problem ID: GRPH
"""
import nc

def edges(strands,k):
    #recives segregated fasta file, returns adjecent strands defined as:
    #last 3 bases identical to first 3 bases of next strand
    edges=[]
    for strand in strands:
        for st in strands:
            if(strands[strand][-k:len(strands[strand])]==strands[st][0:k] and strands[strand]!=strands[st]):
                edges.append(strand+" "+st)
    return(edges)

#pseg=open(path)
pseg=nc.seg_fasta_dic(pseg)
print(pseg)
res=edges(pseg,3)
for x in res:
    print(x)