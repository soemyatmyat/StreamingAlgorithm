import sys
from pprint import pprint
from random import random
from collections import deque
from sys import getsizeof
import resource

##########################################################################
##########################################################################
# Methods: implement the methods of the assignment below.  
#
# Each method gets 1 100 element array for holding ints of floats. 
# This array is called memory1a, memory1b, or memory1c
# You may not store anything else outside the scope of the method.
# "current memory size" printed by main should not exceed 8,000.

MEMORY_SIZE = 100 #do not edit

memory1a =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task1ADistinctValues(element, returnResult = True):
    #[TODO]#
    #procss the element you may only use memory1a, storing at most 100 

    for i in range(len(memory1a)): # loop through 100 hash functions 
        temp=memory1a.popleft() # store the previous value from hash function (loop 100 times) to compare
        hashValue=((((2 * i) + 1) * element) + i) % 2 ** 64 # h(x)=ax+b mod c <== generate a and b based on i values and c (2^64) is the length of the hash range 
        binary=bin(hashValue)[2:]
        numTrailingZero=len(binary)-len(binary.strip('0'))
        if temp is not None:
            if (temp < numTrailingZero): # see if previous value is greater than current value (with that, we get the highest trailing zeros)
                memory1a.append(numTrailingZero) # if so, replace it by appending into the deque
            else:
                memory1a.append(temp) # else, re-input the previous value to the deque
        else:
            memory1a.append(numTrailingZero) # initializaton 

    if returnResult: #when the stream is requesting the current result
        result = 0
        #[TODO]#
        #any additional processing to return the result at this point
        means=[] # initialization of arrays to store the means of 10 buckets of numTrailingZero from memory1a - 1 bucket to hold 10 numTrailingZeros
        for i in range(len(memory1a)): # memory1a stores the r value from 100 hash functions where r is the max number of zeros at tail
            result += memory1a[i]
            if (i % 10 == 9): # for every 10 hash function 
                means.append(result / 10) # get the mean 
                result = 0 # reset the result to zero
        means.sort() # sort the mean of 10 hash function by ascending order
        result = (means[4] + means[5]) / 2 # median of means         
        result = 2 ** result # 2^r 
        return result
    else: #no need to return a result
        pass


memory1b =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task1BMedian(element, returnResult = True):
    #[TODO]#
    import numpy as np
    n = memory1b.popleft() # memory1b[0]: stores the number of element procesed 
    s = memory1b.popleft() # memory1b[1]: stores the summation of ln(ei) 
    

    if s is not None:
        s = s + np.log(element)
        memory1b.appendleft(s) 
    else:
        memory1b.appendleft(np.log(element))

    if n is not None:
        n = n + 1
        memory1b.appendleft(n)
    else:
        memory1b.appendleft(1)

    if returnResult: #when the stream is requesting the current result
        result = 0
        #[TODO]#
        #any additional processing to return the result at this point
        result = n / s 
        return result
    else: #no need to return a result
        pass
    
memory1c =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit


def task1CMostFreqValue(element, returnResult = True):
    #[TODO]#
    # memory1c will have element and its count e.g: [2, 1, 10, 2,...] 2 appears once, 10 appears twice, etc. 
    found = False 

    #############################################################################
    ## the first loop of memory1c to find if the element exist in the memory  ## 
    ###########################################################################
    for i in range(len(memory1c)):
        if (i % 2 == 0): # if i is even because the element value is stored in even positions of memory1c
            if (element == memory1c[i]): # if the element already exists in the memory1c 
                memory1c[i+1] += 2 # increase the counter by 2 
                found = True 
                break
        
    if (found == False): # if the element does not exist in the memory1c, add it along with its count which is 1.
        ###################################################################### 
        ##   Precaution to check if we are popping the high seen value pair 
        ###################################################################### 
        storeValue = memory1c[0]
        storeCount = memory1c[1]
        n = 50 # to keep track of how many rounds of loops we have already completed (50 paris in memory1c)
        minCount = 1 # assuming minium seen count would be 1 in the memory1c 
        while (storeCount is not None and storeCount != minCount): # if it's not minimum Count 
            n -= 1 
            memory1c.append(memory1c.popleft()) # put them into the back of the array
            memory1c.append(memory1c.popleft())
            storeValue = memory1c[0]
            storeCount = memory1c[1]
            if (n == 0): # if n become 0, we have completed a round of loop in the memory1c
                minCount += 1 # minimum count would have to increase by 1 now 
                n = 50 # reset n 

        memory1c.append(element) # this will pop the first element in deque and its count in memory1c
        memory1c.append(1) 
    else: 
        for i in range(1, len(memory1c), 2): # loop through memory1c to decrease the counter by 1 <== we have limited space/slots (50 slots max), so, we will remove those unfrequently seen elements
            if memory1c[i] is not None:
                memory1c[i] -= 1 # decrease all the elements counter by 1 

        for i in range(0, 100): # check if any elements has counter = zero and remove them 
            storeValue = memory1c.popleft() 
            storeCount = memory1c.popleft() 
            if (storeCount is not None and storeCount != 0): # it's not zero, add them back 
                memory1c.append(storeValue)
                memory1c.append(storeCount)
            else: 
                memory1c.append(None)
                memory1c.append(None)

    if returnResult: #when the stream is requesting the current result
        result = 0
        #[TODO]#
        #any additional processing to return the result at this point
        maxCount = 0 # initialization for the maximum number of count 
        maxIndex = 0 # initialization for the index position of mode 
        for i in range(1, len(memory1c), 2): # loop through memory1c counter O(n/2)
            if memory1c[i] is not None: 
                if memory1c[i] > maxCount: # check the count value 
                    maxCount = memory1c[i] 
                    maxIndex = i-1

        result = memory1c[maxIndex]
        return result
    else: #no need to return a result
        pass


##########################################################################
##########################################################################
# MAIN: the code below setups up the stream and calls your methods
# Printouts of the results returned will be done every so often
# DO NOT EDIT BELOW

def getMemorySize(l): #returns sum of all element sizes
    return sum([getsizeof(e) for e in l])+getsizeof(l)

if __name__ == "__main__": #[Uncomment peices to test]
    
    print("\n\nTESTING YOUR CODE\n")
    
    ###################
    ## The main stream loop: 
    print("\n\n*************************\n Beginning stream input \n*************************\n")
    filename = sys.argv[1]#the data file to read into a stream
    printLines = frozenset([10**i for i in range(1, 20)]) #stores lines to print
    peakMem = 0 #tracks peak memory usage
    
    with open(filename, 'r') as infile:
        i = 0#keeps track of lines read
        for line in infile:
            #remove \n and convert to int
            element = int(line.strip())
            i += 1
            
            #call tasks         
            if i in printLines: #print status at this point: 
                result1a = task1ADistinctValues(element, returnResult=True)
                result1b = task1BMedian(element, returnResult=True)
                result1c = task1CMostFreqValue(element, returnResult=True)
                
                print(" Result at stream element # %d:" % i)
                print("   1A:     Distinct values: %d" % int(result1a))
                print("   1B:              Median: %.2f" % float(result1b))
                print("   1C: Most frequent value: %d" % int(result1c))
                print(" [current memory sizes: A: %d, B: %d, C: %d]\n" % \
                    (getMemorySize(memory1a), getMemorySize(memory1b), getMemorySize(memory1c)))

            else: #just pass for stream processing
                result1a = task1ADistinctValues(element, False)
                result1b = task1BMedian(element, False)
                result1c = task1CMostFreqValue(element, False)
                
            memUsage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if memUsage > peakMem: peakMem = memUsage
        
    print("\n*******************************\n       Stream Terminated \n*******************************")
    print("(peak memory usage was: ", peakMem, ")")
   
