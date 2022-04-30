# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:51:34 2019

@author: Aputer
Rosalind Project problem ID: CONS
"""

def seg_fasta(file):
    #recives a read file and returns a list of
    #DNA sequences from given FASTA file
    sequences=[]
    temp=""
    i=0
    for line in file:
            if(i==0):
                i=1
            elif(">Rosalind"  in line):
                sequences.append(temp.rstrip("\n"))
                temp=""
            else:
                temp+=line.rstrip("\n")
                
    return(sequences)
#Strands=open(path)
#Strands=seg_fasta(Strands)


def concensus(strands):
    #receives a list of DNA strands of equal length,
    #returns a concensus strand and
    nuc=[]
    for i in range(len(strands[0])):
        nuc.append({'A':0,'C':0,'G':0,'T':0})
        for strand in strands:
            if(strand[i]=='A'):
                nuc[i]['A']+=1
            elif(strand[i]=='C'):
                 nuc[i]['C']+=1
            elif(strand[i]=='G'):
                 nuc[i]['G']+=1
            elif(strand[i]=='T'):
                 nuc[i]['T']+=1
    constrand=""
    for base in range(len(nuc)):
        if(nuc[base]['A']>nuc[base]['C']):
            temp1='A'
        else:
            temp1='C'
        if(nuc[base]['G']>nuc[base]['T']):
            temp2='G'
        else:
            temp2='T'
        if(nuc[base][temp1]>nuc[base][temp2]):
            constrand+=temp1
        else:
            constrand+=temp2
    return(constrand)
#concensus(Strands)