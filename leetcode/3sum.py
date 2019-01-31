
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        prev_checked = []

        for i in range(len(nums)-2):

            current = nums[i]

            start = i+1
            end = len(nums)-1
            net = 0 - current

            L = nums[start]
            R = nums[end]

            while start<end:
                x = [L,R,current]
                if L+R == net and L+R+current == 0 and x not in ans:
                    ans.append(x)

                if L+R > net:
                    end -= 1

                elif L+R <= net:
                    start+=1

                L = nums[start]
                R = nums[end]

        return(ans)
        
                