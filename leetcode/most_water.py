'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''




class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        #Brute Force Approach
        max_area = 0
        x = len(height)
        for i in range(x):
            for j in range(x):
                area = min(height[i],height[j])*(j-i)
                if(area>max_area):
                    max_area = area
        return(max_area)
        '''
        
        L, R, w, ans = 0, len(height)-1, len(height)-1, 0
        
        for i in range(w, 0, -1):
            if height[L]<height[R]:
                ans = max(ans, height[L]*w)
                L = L+1
            else:
                ans = max(ans, height[R]*w)
                R= R-1
        return(ans)
        
        