# -*- coding: utf-8 -*-

"""
Created on Thu Mar 14 00:09:33 2019

@author: Aputer

A library of functions comprised of finished problems and frequently used code
within them. There might be some cases of code duplication in other problems
since I did not delete any of the functions in their original files,
but all updated, properly formated and documented general use versions
are kept here.
"""

#Library for bioinformatics of useful and widely used functions

import shutil
import os
from glob import glob
import random

def get_codons_dic():
    #returns a dictionary with codons as keys and amino acids as values
    amino_acids = { "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L"
                 ,"UCA":"S", "UCC":"S", "UCG":"S", "UAU":"Y"
                 ,"UGU":"C", "UGC":"C", "UCU":"S", "UAC":"Y"
                 ,"UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L"
                 ,"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P"
                 ,"CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R"
                 ,"CGA":"R", "CGG":"R", "AUC":"I", "AUA":"I"
                 ,"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T"
                 ,"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K"
                 ,"AGU":"S", "AGC":"S", "AGA":"R", "AUG":"M"
                 ,"AGG":"R", "GUC":"V", "GUA":"V", "GUG":"V"
                 ,"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A"
                 ,"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E"
                 ,"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                 ,"CUG":"L", "CAU":"H", "CGC":"R", "AUU":"I"
                 ,"GUU":"V"
                 ,"UGA":"stop", "UAA":"stop" , "UAG":"stop"}
    return(amino_acids)

def get_monoisotopic_table():
    #returns a dictionary with amino acids as keys and their respective
    #monoisotopic mass in daltons as values
    mass={'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841
          ,'G':57.02146, 'H':137.05891,'I':113.08406
          ,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276
          ,'Q':128.05858,'R':156.10111, 'S':87.03203,'T':101.04768,'V':99.06841
          ,'W':186.07931,'Y':163.06333 }
    return(mass)

def get_fasta_file(srcDir, dstDir):
    #moves fasta file from download dir to rosalind dir, allowing the program
    #to work on it, adds a counter for each previous attempt to prevent error
    
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
            # Check if both are directories
            
        for filePath in glob(srcDir + '\*.fasta'):
            # Iterate over all the files in source directory
            
            trymove(filePath,srcDir,dstDir)
    else:
    
        print("srcDir & dstDir should be Directories")
        
def trymove(filePath, srcDir, dstDir, count = 1):

    try:
    
        shutil.move(filePath, dstDir)
        
    except:
    #if a previous attempt with the same name is present,
    #this will attempt to rename it with an attempt number
    #until it reaches a non used number
    
        filename=filePath.replace(srcDir, '')
        newfilename=filename.replace('.', '{}.'.format(count))
        
        try: 
        
            os.rename('{}{}'.format(dstDir,filename),
                       '{}{}'.format(dstDir,newfilename))
                       
            trymove(filePath, srcDir,dstDir,count)
            
        except:
        
             trymove(filePath, srcDir,dstDir, count=count+1)

def archive(srcDir, dstDir):
    #moves all current attempts to archive dir
    
    get_fasta_file(srcDir, dstDir)

def seg_fasta_dic(file):
    #returns a dictionary of DNA sequences from given FASTA file
    #in which the key is the name and value is the strand
    
    sequences = {}
    temp = ""
    
    for line in file:
    
        if(">Rosalind" in line):
           
            temp = line.rstrip("\n")
            temp = temp.replace(">", '')
            sequences[temp] = ""
            
        else:
        
            sequences[temp] += line.rstrip("\n")
                
    return(sequences)

def seg_ncbi_fasta(file):
    #returns a dictionary of DNA sequences from given NCBI formated FASTA file
    #in which the key is the name and value is the strand.
    
    file=file.replace(" ", '')
    file=file.split()
    fin=[]
    
    for line in file:
    
        if(line[0] != '>'):
        
            fin.append(line)
            
    if(len(fin) == 1):
    
        fin = fin[0]
        
    return(fin)

def seg_fasta(file):
    #recives a fasta file and returns a list of
    #the DNA sequences only from the given FASTA file
    
    sequences = []
    temp = ""
    i = 0
    
    for line in file:
    
            if(i == 0):
            
                i = 1
                
            elif(">Rosalind"  in line):
            
                sequences.append(temp.rstrip("\n"))
                temp = ""
                
            else:
            
                temp += line.rstrip("\n")
                
    sequences.append(temp)
    return(sequences)

def transcribe_DNA(strand):

    return(strand.replace('T', 'U'))

def translate_DNA(strand):

    strand = transcribe_DNA(strand)
    return(translate_RNA(strand))
    
def complement_DNA(sequence):

    strand = ""
    
    for nucleotide in sequence:
    
        if(nucleotide == 'A'):
        
            strand += "T"
            
        elif(nucleotide == 'T'):
        
            strand += "A"
            
        elif(nucleotide == 'G'):
        
            strand += "C"
            
        elif(nucleotide == 'C'):
        
            strand += "G"
            
    return(strand)

def reverse_complement_DNA(sequence):

    strand = ""
    
    for nucleotide in sequence:
    
        if(nucleotide == 'A'):
        
            strand += "T"
            
        elif(nucleotide == 'T'):
        
            strand += "A"
            
        elif(nucleotide == 'G'):
        
            strand += "C"
            
        elif(nucleotide == 'C'):
        
            strand += "G"
            
    strand = strand[::-1]
    return(strand)
    
    
def reverse_compliment_RNA(sequence):
    strand = ""
    
    for nucleotide in sequence:
        
        if(nucleotide == 'A'):
            
            strand += "U"
            
        elif(nucleotide == 'U'):
            
            strand += "A"
            
        elif(nucleotide == 'G'):
            
            strand += "C"
            
        elif(nucleotide == 'C'):
            
            strand += "G"
            
    strand = strand[::-1]
    return(strand)    
    
def nucleotide_count(sequence):
    bases = {'A':0, 'T':0, 'G':0, 'C':0}
    for nucleotide in sequence:
    
        if(nucleotide == 'A'):
        
            bases['A'] += 1
            
        elif(nucleotide == 'T'):
        
            bases['T'] += 1
            
        elif(nucleotide == 'G'):
        
            bases['G'] += 1
            
        elif(nucleotide == 'C'):
        
            bases['C'] += 1
            
    return(bases)

def translate_RNA(strand):
    #translates a strand of RNA into a chain of amino acids,

    amino_acids = get_codons_dic()
                 
    protein = ""
    try:
    
        for x in range(0, len(strand), 3):
        
            if(amino_acids[strand[x:x+3]] == "stop"):
            
                return(protein)  
                
            protein += amino_acids[strand[x:x+3]]
            
    except:
    
            pass



def find_ORF(strand):
    #function receives a DNA or an RNA sequence, returns a set of all possible
    #proteins encoded by the sequence
    
    proteins = []
    strand = transcribe_DNA(strand)
    reversed_strand = reverse_compliment_RNA(strand)
    

    for pos in range(len(strand)-1):
        
        if(strand[(pos):(pos+3)] == 'AUG'):
            
            proteins.append(translate_RNA(strand[(pos):]))
                
        if(reversed_strand[(pos):(pos+3)] == 'AUG'):
            
            proteins.append(translate_RNA(reversed_strand[(pos):]))
                
    proteins = set(proteins)
    
    if(None in proteins):
    
        proteins.remove(None)
        
    return(proteins)

def splice_DNA(path):
    #receives a path to a fasta file containing a DNA sequence as its
    #first entry and introns as all other entreis. 
    #returns the protein product after removing the introns from the sequence
    
    file = open(path, 'r')
    fasta = seg_fasta(file)
    file.close()
    
    sequence = fasta.pop(0)
    
    for intron in fasta:
        
        sequence = sequence.replace(intron, '')
        
    protein = translate_DNA(sequence)
    return(protein)


    

 

 

 
def rabin_karp_search(txt, pattern, d = 4):
    #receives a pattern, a text and an optional number of characters in alphabet
    #return an array of all indices where the pattern was found in the text
    
    #a list of primes to use at random, each is about 98 bits large,
    #meaning even a gargantuan pattern and text at a combined size of around 2^40
    #will have an error rate of 1 to 10^18 false positives
    primes = [502323920063011719343437627041, 935531603335139370533916346111,
              719303688542765516387123769211, 522461070523013520232907792983,
              882069643177881843365709038821, 890472469923209042788229106911,
              463993184983857110086517231381, 542780932917143279102495000969,
              564162194756755365679285118543, 879598130787197460378578906057,
              553953960312814487502190453447, 356851317705057135635429284613]
    
    rand = random.SystemRandom().randint(
            int(0), int(len(primes) - 1))
    p = primes[rand]
    
    m = len(pattern)
    n = len(txt)
    
    pattern_hash = ord(pattern[0])
    txt_hash = ord(txt[0])   
    z = 1

        
    #initial computation of pattern, polynomial multiplier
    #and text comparison hash values
    for i in range(1, m):
        pattern_hash = (d * pattern_hash + ord(pattern[i]))%p
        
        txt_hash = (d * txt_hash + ord(txt[i]))%p
        
        z = (d * z)%p
        
    indices = []
    
    #goes over the text, shifting the polynomial values of the text left,
    #removing the left most and adding a rightmost values according to the characters
    for i in range(n - m + 1):
    
        if (pattern_hash == txt_hash):
            indices.append(i)
 
        if (i < n - m):        
            txt_hash = (d * (txt_hash - ord(txt[i]) * z) + ord(txt[i + m]))%p

    return(indices)
 