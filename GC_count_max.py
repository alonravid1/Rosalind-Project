# -*- coding: utf-8 -*-
"""
@author: Aputer

Rosalind Project problem ID: GC
"""

#a simple early problem i solved, used old problems instead of the bio library
import nucleotide_count
def GC_content(sequence):
    #calculates GC% of given DNA strand
    seq=nucleotide_count.nucleotide_count(sequence)
    total=0
    gc=0
    for base,count in seq.items():
        if(base=='G' or base=='C'):
            gc+=count
        total+=count
    return((gc/total)*100)
    
    
    
def seg_fasta(file):
    #returns a dictionary of DNA sequences from given FASTA file
    #in which the key is the name and value is the strand
    sequences={}
    temp=""
    for line in file:
        if(">Rosalind" in line):
           
            temp=line.rstrip("\n")
            temp=temp.replace(">",'')
            sequences[temp]=""
        else:
            sequences[temp]+=line.rstrip("\n")
                
    return(sequences)

def Max_GC(sequence):
    #return highest GC content ratio strand
    #name and GC content ratio
    GCR={}
    top=0
    temp=0
    top_name=""
    for name,strand in sequence.items():
        GCR[name]=GC_content(strand)
        temp=GCR[name]
        if(temp>top):
            top=temp
            top_name=name
            
            
    return(top,top_name)

#original path was in my own computer
strands=open(#path)
strands=seg_fasta(strands)
for name,strand in strands.items():
    print(name)
    print(GC_content(strand))
