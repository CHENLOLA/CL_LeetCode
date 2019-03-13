class Solution:
    def singleNumber(self,nums):
        number_hash={}
        for i in nums:
            if i not in number_hash:
                number_hash[i]=1
            #if i in number_hash:
            else:
                number_hash[i]= number_hash[i] + 1
        result = list(number_hash.keys()) [ list(number_hash.values()).index(1) ]  
        return result
            
