class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if (x<0):
            x=x*-1
            neg = True
        y = str(x)
        rev_y = int(y[::-1])
        
        if neg:
            rev_y = -1*int(rev_y)
        
        if(rev_y.bit_length()>=32):
            return(0)
            
        return(int(rev_y))