"""
STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]
"""

def twosum(array_nums, target):
	sum_dict = {}
	for i in range(len(array_nums)):
		diff = target - array_nums[i]
		
		if diff in sum_dict.keys():
			return [i, sum_dict[diff]]
	
		if array_nums[i] not in sum_dict.keys():
			sum_dict[array_nums[i]] = i