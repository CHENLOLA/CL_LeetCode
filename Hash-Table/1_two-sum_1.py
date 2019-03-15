class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List=[]
        for i in range(0,len(nums)):
            for n in range(0,len(nums)):
                if nums[i]+nums[n] == target:
                    List=[nums[i],nums[n]]
                    return  List
twoSum([2,7,11,15,9],9)
