def twosum(array_nums, target):
	sum_dict = {}
	for i in range(len(array_nums)):
		diff = target - array_nums[i]
		
		if diff in sum_dict.keys():
			return [i, sum_dict[diff]]
	
		if array_nums[i] not in sum_dict.keys():
			sum_dict[array_nums[i]] = i