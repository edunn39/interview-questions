from typing import List
from queue import PriorityQueue

class Solution:
    def top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d[num] + 1 if num in d.keys() else 1
        pq = PriorityQueue()
        for key, value in d.items():
            pq.put(value, key)
        result = []
        for i in range(k):
            result.append(pq.get())
        return result
