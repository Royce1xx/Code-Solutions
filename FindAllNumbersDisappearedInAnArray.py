from collections import Counter
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        num = Counter(nums)

        royce = []

        for i in range(1, n+ 1):
            if num[i] == 0:
                royce.append(i)
        return royce
      

        