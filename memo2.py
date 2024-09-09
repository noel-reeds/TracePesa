#!/usr/bin/env python3
# Class to represent a job 

class Job: 
  def __init__(self, start, finish, profit): 
        self.start = start 
        self.finish = finish 
        self.profit = profit 
    
    
# A Binary Search based function to find the latest job 
# (before current job) that doesn't conflict with current 
# job. "index" is index of the current job. This function 
# returns -1 if all jobs before index conflict with it. 
def binarySearch(job, start_index): 
	# https://en.wikipedia.org/wiki/Binary_search_algorithm
    
	# Initialize 'lo' and 'hi' for Binary Search 
    lo = 0
    hi = start_index - 1
    
    # Perform binary Search iteratively 
    while lo <= hi: 
    	mid = (lo + hi) // 2
    	if job[mid].finish <= job[start_index].start: 
    		if job[mid + 1].finish <= job[start_index].start: 
    			lo = mid + 1
    		else: 
    			return mid 
    	else: 
    		hi = mid - 1
    return -1
    
# The main function that returns the maximum possible 
# profit from given array of jobs 
def schedule(job): 
    # Sort jobs according to start time 
    job = sorted(job, key = lambda j: j.start) 
    
    # Create an array to store solutions of subproblems. table[i] 
    # stores the profit for jobs till arr[i] (including arr[i]) 
    n = len(job)
    table = [0 for _ in range(n)]

    table[0] = job[0].profit;

   	# Fill entries in table[] using recursive property 
    for i in range(1, n):

   	    # Find profit including the current job 
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];

        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])

    return table[n-1]

# Driver code to test above function
job = [Job(1, 2, 50), Job(3, 5, 20), 
    Job(6, 19, 100), Job(2, 100, 200)] 
print("Optimal profit is"),
print(schedule(job))
