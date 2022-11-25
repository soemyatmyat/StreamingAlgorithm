# StreamingAlgorithm

##  Objective
The objective is to implement a novel streaming algorithm under the constraints of limited memory. In particular, this serves as a practical exercise to approximate the distinct values, median and most frequent value in streaming data to understand the concepts of Big Data and their practical application. 

A stream of integers representing yearly incomes of individuals (in 10s of thousands, e.g., 1 represents $10,000; 234 represents $2,340,000) is fed. The goal is to summarize the stream in three ways: 

* the approximate distinct number of incomes seen,
* the median income, and 
* the most frequent value of income. 

## Data 
Two versions of the data are prepared for verification
1. trial_incomes.csv: a small trial version with only 1000 integers to use while developing the methods, and 
2. test_incomes.csv.zip: a test that goes over 1 million integers to test the implemented methods on a larger dataset.

## Code
The  code reads the input file and set limits on memory (to constrain working with data as a stream). It iterates over elements in the stream and calls each of the three methods passing the value along.
* Task 1A: "def task1ADistinctValues", 
* Task 1B: "def task1BMedian", 
* Task 1C: "def task1CMostFreqValue" 

Purpose is to implement above three methods such that they return the approximate value, by only using the 100 elements array (technically, a deque object with a maxsize but it operates as an array) provided to them as a memory. 100 elements array may only contain ints or floats as values. 
During streaming, the current size of the array will be printed. It should remain < 8,000. At each of the following interactions: 10, 102, 103, ... , 106 it prints the current calculation from the method along with the memory usage.
