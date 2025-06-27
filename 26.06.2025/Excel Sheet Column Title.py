class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        L=str()
        while columnNumber>0:
            columnNumber -= 1  
            L=L+str(chr(columnNumber%26+65))
            columnNumber=columnNumber//26
        return (L[::-1])
            
        
