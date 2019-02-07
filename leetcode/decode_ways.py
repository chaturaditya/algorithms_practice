'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0]*(len(s)+1)
        
        count[0] = 1
        
        if int(s[0]) == 0:
            count[1] = 0
        else:
            count[1] = 1
            
        for i in range(2, len(s)+1):
            oneDigit = int(s[i-1:i])
            twoDigit = int(s[i-2:i])
            
            if oneDigit > 0:
                count[i] += count[i-1]
                
            if twoDigit > 9 and twoDigit < 27:
                count[i] += count[i-2]
                
        
        return count[len(s)]