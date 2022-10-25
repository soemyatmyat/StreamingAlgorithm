# StreamingAlgorithm

##  Objective
The objective is to implement a novel streaming algorithm under the constraints of limited memory. In particular, this assignment serves as a practical exercise to approximate the distinct values, median and most frequent value in streaming data to understand the concepts in the course and their practical application. 

A stream of integers representing yearly incomes of individuals (in 10s of thousands, e.g., 1 represents $10,000; 234 represents $2,340,000) is fed. The goal is to summarize the stream in three ways: 
a)	the approximate distinct number of incomes seen,
b)	the median income, and 
c)	the most frequent value of income. 

## Data 
Two versions of the data are prepared and provided for the assignment -  
(1)	trial_incomes.csv: a small trial version with only 1000 integers to use while developing the methods, and 
(2)	test_incomes.csv.zip: a test that goes over 1 million integers to test the implemented methods on a larger dataset.

## Starter code
Additionally, a starting template code is provided. Python version 3.7 or later would work with the starter code. It includes all the data science, machine learning, or statistics libraries that are necessary. 
The starter code reads the input file and set limits on memory (to constrain working with data as a stream). It iterates over elements in the stream and calls each of the three methods passing the value along.
a)	Task 1A: "def task1ADistinctValues", 
b)	Task 1B: "def task1BMedian", 
c)	Task 1C: "def task1CMostFreqValue" 

Purpose is to implement above three methods such that they return the approximate value, and only use the 100 elements array (technically, a deque object with a maxsize but it operates as an array) provided to them as a memory. 100 elements array may only contain ints or floats as values. 
During streaming, the current size of the array will be printed. It should remain < 8,000. At each of the following interactions: 10, 102, 103, ... , 106 it prints the current calculation from the method along with the memory usage.

## Task 1A. Approximate the count of distinct incomes 

### Overview

Flajolet Martin Algorithm, also known as FM algorithm, is used to approximate the number of unique incomes in a data stream. 
Pseudo Code of FM algorithm:
1.	Selecting a hash function h so each element in the set is mapped to a string to at least log n bits.
2.	For each element x, r(x) = length of trailing zeroes in h(x)
3.	R = max(r(x))
4.	Distinct elements = 2R
FM algorithm is sensitive to the parameters of hash function and thus, the results from FM algorithm can vary significantly depending on the hash function values. Since it is allowed to store up to 100 elements at a time in memory as “memory1a” deque object, we will use 100 hash functions to optimize the accuracy of FM algorithm. 

After which, we could use the mean of the results from 100 functions as an approximation for the count of distinct incomes. However, averaging would be susceptible to outliners. Therefore, we use the median of mean approach to average the estimates resulting from all hash functions.

### Hash functions
First, we look at how to determine the hash function. 
The hash function follows below pattern: 

h(x) = ax + b mod c 

where a is an odd numbers and c is the capping limit of hash range (2^k). 

#### Explanation on choice of values for hash function

When a is even and b is odd, the hash function always returns odd numbers which causes the trailing zeros to be 0 all the time. When a is even and b is even, the hash function could return the same value for two different inputs of x. Hence, we would use odd numbers for a. For c, we will keep 264 as a constant value; which would be more than sufficient to cover the maximum income data. 

In order to generate the values for a and b, we use ‘i’ which has a value from 0 to 99 (as ‘i’ will a dynamic value and would be keeping the number of loop when looping through 100 elements in “memory1a”). 

### Memory Utilization 

Every income value will pass through 100 hash functions, giving 100 trailing zeros. Current 100 trailing zeros are compared with previous 100 trailing zeros to determine the higher number of trailing zeros. Then, the higher number of trailing zeros are stored in “memory1a”. Therefore, “memory1a” store 100 highest number of trailing zeros from 100 hash functions on the data seen so far. 

### Approximating count of distinct incomes

Every time the function is called to return the approximate count of distinct incomes, 100 highest number of trailing zeros in “memory1a” are bucketed into 10 groups to get 10 means and then, the median of these 10 means is returned as the approximate count of distinct incomes. 

### Summary

In summary, the followings have been performed to improve the accuracy of the algorithm: 
1)	100 hash function to get 100 highest trailing zeros from each function (maximum elements we can store in the memory is 100)
2)	Means by Bucketing (100 highest trailing zeros in memory are split into 10 buckets with 10 elements in each bucket, and then we calculate the means from each bucket, resulting in 10 means)
3)	Median of means (10 means are sorted into an ascending order and the median of means is picked as the approximate value for the count of distinct incomes)





