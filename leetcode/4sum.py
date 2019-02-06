'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        
        ans = []
        
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                a = nums[i]
                b = nums[j]
                start = j+1
                end = len(nums)-1
                
                while start < end:
                    c = nums[start]
                    d = nums[end]
                    
                    if a+b+c+d == target:
                        temp = [a,b,c,d]
                        if temp not in ans:
                            ans.append([a,b,c,d])
                        start+=1

                    elif a+b+c+d < target:
                        start+=1

                    else:
                        end-=1

            
        return(ans)
                    
            
            
            
        