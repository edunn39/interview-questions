from typing import List

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        chains = []
        seq = []
        for n in nums:
            if n not in s:
                pass
            chain = [n]
            m = n
            while n-1 in s:
                chain.append(n-1)
                s.remove(n-1)
                n = n-1
            n = m
            while n+1 in s:
                chain.append(n+1)
                s.remove(n+1)
                n = n+1
            chains.append(chain)
        return max([len(c) for c in chains])