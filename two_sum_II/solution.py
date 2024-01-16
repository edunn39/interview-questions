from typing import List

class Solution:

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1
        while e > s:
            c = numbers[s] + numbers[e]
            if c == target:
                return [s+1, e+1]
            elif c > target:
                e -= 1
            elif c < target:
                s += 1
        return [s+1, e+1]