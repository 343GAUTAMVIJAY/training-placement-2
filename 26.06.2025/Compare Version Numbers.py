class Solution(object):
    def compareVersion(self, version1, version2):
        val1=list(map(int,version1.split('.')))
        val2=list(map(int,version2.split('.')))
        if len(val1)>=len(val2):
            val2.extend([0]*(len(val1)-len(val2)))
        else:
            val1.extend([0]*(len(val2)-len(val1)))
        n=len(val1)
        for i in range(n):
            if val1[i]>val2[i]:
                return 1
            elif val1[i]<val2[i]:
                return -1
        return 0
