from typing import List

class Solution:

    def contains_duplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        