# -*- coding: utf-8 -*-
"""
@author: Aputer

Rosalind Project problem ID: REVP
"""
import bio

def check_palindrom(strand, complement_strand):
    #checks if the given strand and its complement are a palindrom
    for i in range((len(strand)//2)):
        
        if(strand[i] != complement_strand[-i-1]):
            
            return(False)
        
    return(True)
        
def get_restriction_sites(strand):
    #receives a DNA strand, finds and prints all potential restriction sites
    #with a length between 4 and 12 BP
    reverse_palindromes = []
    complement_strand = bio.complement_DNA(strand)
    
    for i in range(len(strand)): 
        
        for j in range(3,12,2):
            
            if(i+j>=len(strand)):
                continue
            
            if(strand[i] == complement_strand[i+j]):
                
                check = check_palindrom(strand[i:i+j+1],
                                           complement_strand[i:i+j+1])
            
                if(check):
                   reverse_palindromes.append([i+1, j+1])
                   
    for array in reverse_palindromes:
        
        print("{} {}".format(array[0], array[1]))
    
sample = """CGCGCTCCTCCGTTGTAATACGCCCATCCACACATTATTTGAGCGTATCTCGTACATTGC
    CAAATACTCTCCAGTTTTTAATATTGAGGGTCGCAATGCGATTAAAGGCAATGTGAGTAC
    GTTACACGTCCGTAGAAGACCCATGGTCGATTCATAAACGAGCCCTCTCCCCAGAGATTC
    TATAGCTCGTGCTGCGTAAGTCGGGCTTTTTCGCGATATGACCATGGGCGAACTTCGAGC
    AGATTTTTAAAAGATTATCTAATATACGACCGTTCCCAGTCCGCACTGTTATTTCAGTTG
    AGGTCGGCCTCTTTAAACCGGAGAACCCTAGCAATAGTTTTCATCACTAGCCTTATCGGC
    TCCTTATGGATTGCGCCCACCCAAAGATGTCCTGATACAGTTTTGGGACTAGAGCCGAAC
    CCGGGTAGCTAAAAACAGCCAAATGTTCAACGTTCTCGGTTCTATACATGTATAAGTGAT
    AAACGTAAGTCGATTCTGCACCGACGGATGCCCGAGGTTGCATAAGGGCACACAGATTTA
    ACTGGTTTACCGAGCGTCGCAGTGAAAGACATATAGCCCGGCGGCGTTGCACCTAGCTCA
    AGCACAGGGTAGTTCAAAATAAGAACCTTTTTCTTTAGTGGATAATAAGTTTTACTCAAG
    TACATGAGGACGCGGCAGCCGGGCACCTAGCATCTACGAATCGCTATGCTAGTCTTCTGA
    TCTGCGTTCCCAGAGGGAGCGGGGATGCTTACCATAACTACTGAATCGCCAAAGCTGATT
    CGCTGAGACTCATCTTTATGGCCCAACCCTTTATGGCGCCGGTCTGTGGGAAGAGTGTGC
    GTTGTACTAAAGCACTATCTCTGCCTCCGGTTGGGATGTGACTTCTTGAGTGTCAAGCGT
    GATGGGGGTGGATACCTTCATATGACAAAATTGCGC"""
    
sample = sample.replace(' ','')
sample = sample.replace('\n','')
get_restriction_sites(sample)