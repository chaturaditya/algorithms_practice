def isPal(s):
    if s == s[::-1]:
        return True
    return False
    

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        
        for i in range(len(s)):
            for j in range(len(s)):
                word = s[i:j+1] 
                if isPal(word) and len(word)>len(longest):
                    longest = word
                
        return(longest)