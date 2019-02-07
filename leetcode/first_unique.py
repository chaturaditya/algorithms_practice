'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


class data():
    def __init__(self, loc, count):
        self.loc = loc
        self.count = count

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {}
        
        for i, j in enumerate(s):
            
            a = j
            if a in dic:
                dic[a].count+=1
                
            else:
                dic[a] = data(i, 1)
        
        ans = []
        for i in dic:
            if dic[i].count == 1:
                ans.append(dic[i].loc)
        
        if not ans:
            return -1
        
        return min(ans)