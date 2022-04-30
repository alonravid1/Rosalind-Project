# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:25:30 2021

@author: Aputer
Rosalind project ID: LGIS

"""
import bisect

def increasing_sequence(perm, n):
    #receives a permutation of numbers from 1 to n, returns the longest
    #increasing subsequence
    
    LIS = [[perm[0]]] #list of previous LIS, keeping one of each length and
                      #replacing it if a new list of same length with smaller
                      #last number is found
               
    max_elements = [perm[0]] #a list keeping all of the last elements of every
                             # LIS stored, used for quicker search and replace
                             
    for i in range(1,n):
        #iterate through every element of the given permutation

        if(perm[i] > max_elements[-1]):
            #if the current number is greater than the largest number in the
            #current largest number than it can be simply added to the last LIS
           
            temp = LIS[-1].copy()
            temp.append(perm[i])
            
            LIS.append(temp)
            max_elements.append(perm[i])
            
        elif(perm[i] > max_elements[0]):
            #if the current number is in the range of the smallest and largest
            #numbers of the current maximum elements, it finds the index of the
            #minimal element which is greater than it, copies the list left to
            #it in the LIS lists, adds the current number at its end and checks
            #if their lengths are equal. if so removes the list with the
            #greater element
            
            
                
            insert_point = bisect.bisect_left(max_elements, perm[i])
            
            temp = LIS[insert_point-1].copy()
            temp.append(perm[i])
            
            LIS.insert(insert_point, temp)
            max_elements.insert(insert_point, perm[i])
            
            
            
            if(len(LIS[insert_point]) >= len(LIS[insert_point+1])):
                #if the current inserted number is less than the number
                #to its right, if the lists's lengths are equal then the
                #right list will always be equal or smaller and is removed
                
                del(LIS[insert_point+1])
                del(max_elements[insert_point+1])
                    
        else:
            
            LIS.insert(0, [perm[i]])
            max_elements.insert(0, perm[i])
            
            if(len(LIS[0]) == len(LIS[1])):
                    #since the current number is inserted if its less than the
                    #number to its right, if the lists's lengths are equal the
                    #right list will always be equal or smaller and is removed
                    
                    del(LIS[1])
                    del(max_elements[1])
            
    return LIS[-1]
            
def decreasing_sequence(perm, n):
    #receives a permutation of numbers from 1 to n, returns the longest
    #decreasing subsequence
    
    LDS = [[perm[0]]] #list of previous LDS, keeping one of each length and
                      #replacing it if a new list of same length with greater
                      #last number is found
               
    min_elements = [perm[0]] #a list keeping all of the last elements of every
                             #LDS stored, used for quicker search and replace
                             
    for i in range(1,n):
        #iterate through every element of the given permutation

        if(perm[i] < min_elements[-1]):
            #if the current number is greater than the largest number in the
            #current largest number than it can be simply added to the last LIS
           
            temp = LDS[-1].copy()
            temp.append(perm[i])
            
            LDS.append(temp)
            min_elements.append(perm[i])
            
        elif(perm[i] < min_elements[0]):
            #if the current number is in the range of the smallest and largest
            #numbers of the current minimum elements, it finds the index of the
            #maximal element which is smaller than it, copies the list left to
            #it in the LDS lists, adds the current number at its end and checks
            #if their lengths are equal. if so removes the list with the
            #smaller element
            
            
            min_elements.reverse()
            insert_point = bisect.bisect_left(min_elements, perm[i])
            insert_point = len(min_elements)-insert_point
            min_elements.reverse()
            
            temp = LDS[insert_point-1].copy()
            temp.append(perm[i])
            
            LDS.insert(insert_point, temp)
            min_elements.insert(insert_point, perm[i])
            
            
            
            if(len(LDS[insert_point]) >= len(LDS[insert_point+1])):
                #if the current inserted number is less than the number
                #to its right, if the lists's lengths are equal then the
                #right list will always be equal or smaller and is removed
                
                del(LDS[insert_point+1])
                del(min_elements[insert_point+1])
                    
        else:
            
            LDS.insert(0, [perm[i]])
            min_elements.insert(0, perm[i])
            
            if(len(LDS[0]) == len(LDS[1])):
                    #since the current number is inserted if its less than the
                    #number to its right, if the lists's lengths are equal the
                    #right list will always be equal or smaller and is removed
                    
                    del(LDS[1])
                    del(min_elements[1])
            
    return LDS[-1]            
    
         
file = open(r'path','r')
n = file.readline()
n = int(n)
permutation = file.read()

permutation = permutation.replace("\n", "")
permutation = permutation.split(' ')



#permutation = "5 1 4 2 3"
#permutation = permutation.split(' ')
#n = 5
for i in range(len(permutation)):
    permutation[i] = int(permutation[i])
    
print(*increasing_sequence(permutation, n))

print(*decreasing_sequence(permutation, n))

file.close()

