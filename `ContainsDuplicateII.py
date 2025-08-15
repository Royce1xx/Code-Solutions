from typing import List
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        royce = defaultdict(list)

        for index, value in enumerate(nums):
            royce[value].append(index)

        for index in royce.values():
            if len(index) > 1:
                for j in range(1, len(index)):
                    diff = index[j] - index[j - 1]
                    if diff <= k:
                        return True
        return False