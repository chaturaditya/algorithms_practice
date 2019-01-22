"""
STATEMENT
Given a string, find the length of the longest substring without repeating characters.

EXAMPLES
"abcabcbb" -> 3 ("abc", starts at first)
"bbbbb" -> 1 ("b", single element substring)
"pwwkew" -> 3 ("wke", starts at middle)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l==0:
            return l
        
        max_num = 0
        bottom = 0
        d = {}
        
        for i, j in enumerate(s):
            
            if j in d and bottom <= d[j]:
                bottom = d[j]+1 
                
            max_num = max(max_num, i-bottom+1)
            d[j]=i
        
        return(max_num)