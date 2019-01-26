"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution(object):
    def convert(self, s, numRows):
        
        if numRows==1 or len(s)==1:
            return(s)
        
        answer = ""
        countRow  = 0
        goingDown = True
        rows = ["" for i in range(numRows)]
        for i in s:

            if goingDown and countRow<numRows:
                rows[countRow]+=i
                if countRow+1 == numRows:
                    goingDown = False
                    countRow-=1
                else:
                    countRow+=1
            elif goingDown == False and countRow>=0:
                rows[countRow]+=i
                if countRow == 0:
                    goingDown=True
                    countRow+=1
                else:
                    countRow-=1

        answer=""
        for i in rows:
            answer+=i
        return(answer)
    