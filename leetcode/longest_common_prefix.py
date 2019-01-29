'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''



class Solution:
    def longestCommonPrefix(self, strs):
       
        index = 0
        run = True
        while run:
            try:
                char = strs[0][index]
                for i in strs:
                    if i[index]==char:
                        char = i[index]

                    else:
                        run = False
                if run:
                    index += 1
            except:
                run = False
        print(index)
        if index == 0:
            return("")
        return(strs[0][0:index]) 