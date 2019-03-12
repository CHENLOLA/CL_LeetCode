class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        temp=[]
        result=0
        for i in s:
            if i in temp:
                if len(temp)>result:
                    result=len(temp)
                temp=temp[temp.index(i)+1:]
                temp.append(i)
            else:
                temp.append(i)
        return max(len(temp),result)
