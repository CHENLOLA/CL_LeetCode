class Solution:
    def twoSum(self,nums,target ):
        
        nums_hash={}
        nums_len=len(nums)
        for i in range(nums_len):
            sub = target - nums[i] 
            if sub not in nums_hash:
                nums_hash[nums[i]]=i
            else :  return [nums_hash[sub], i]

if __name__ == '__main__':
    nums=[2,7,11,15]
    target =9
    print (Solution().twoSum(nums,target))
