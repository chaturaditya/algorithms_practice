'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        
        going_right = True
        going_left = going_down = going_down = False
        
        row = len(matrix)
        col = len(matrix[0])
        x = y = counter = 0        
        ans = []
        bound1 = 0
        bound2 = col-1
        bound3 = row-1
        dic = {}
        while counter < row*col:
            
            if (y,x) not in dic.keys():
                dic[(y,x)] =1
                ans.append(matrix[y][x])
            else:
                bound1 += 1
                bound2 -= 1
                bound3 -= 1
                counter -= 1
                y,x = last_val[0], last_val[1]
            
            last_val = (y,x)
            if going_right:
                if x != bound2:
                    x+=1
                else:
                    going_right = False
                    going_down = True
                    y +=1
            elif going_down:
                if y != bound3:
                    y+=1
                else:
                    going_down = False
                    going_left = True
                    x -=1
            elif going_left:
                if x != bound1:
                    x-=1
                else:
                    going_left = False
                    going_up = True
                    y -=1
            elif going_up: 
                if y != bound1:
                    y-=1
                else:
                    going_up = False
                    going_right = True
                    x +=1
                    
            counter += 1
            
        return(ans)
                
            
        