# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:48:46 2021

@author: Aputer

Project Rosalind ID: LONG
"""
import bio
    

def glue_reads(reads):
    #glues together a list of reads of a DNA, assuming there exists a unique
    #way to reconstruct the entire chromosome from these reads by gluing
    #together pairs of reads that overlap by more than half their length.
    if(len(reads) == 1):
        
        return(reads)
    
    for i in range(1, len(reads)):
        
        read_end = len(reads[i])
        offset = len(reads[i])//2
        
        
        while(offset < read_end):
            
            
            if(reads[0][0:offset] == reads[i][-offset:]):
                #checks the first half plus the offset of the first strand in
                #reads against the last half and the offset bases before it 
                #of strand i
                temp_reads = reads.copy()
                temp_reads[0] = temp_reads[i]+temp_reads[0][offset:]
                
                del(temp_reads[i])
                return(glue_reads(temp_reads))
            
            elif(reads[i][0:offset] == reads[0][-offset:]):
                #checks the first half plus the offset of strand i in
                #reads against the last half and the offset bases before it 
                #of the first strand in reads
                temp_reads = reads.copy()
                temp_reads[0] = temp_reads[0]+temp_reads[i][offset:]
                
                del(temp_reads[i])
                return(glue_reads(temp_reads))
            
            offset += 1
        
            
            
'''
sample dataset:
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
'''           
            

file = open(path,'r')
reads = bio.seg_fasta(file)
write_file = open(path,'w')
write_file.write(glue_reads(reads)[0])

file.close()
write_file.close()