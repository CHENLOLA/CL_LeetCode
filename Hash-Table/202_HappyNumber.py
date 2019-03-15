class Solution:
    def cal(self,n):
        result=0
        while n >0:
            result += (n%10) **2
            n=n//10
        return result

    def isHappy(self, n: int) -> bool:
        list_hash=[]
        while cal(n) not in list_hash:
            list_hash.append( cal(n) )
            if list_hash[-1]==1:
                return True
            cal(list_hash[-1])
            n=list_hash[-1]
        return False
