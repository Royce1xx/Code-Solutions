from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = nums[0]  

        for i in range(len(nums) - 1):  
            if nums[i + 1] == nums[i] + 1:  
                l += nums[i + 1]            
            else:
                break

        nums_set = set(nums)  
        while l in nums_set: 
            l += 1            
        return l
