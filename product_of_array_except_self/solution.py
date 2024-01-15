from typing import List

class Solution:
    def product_of_array_except_self(self, nums: List[int]) -> List[int]:
        product_from_left = [0]*len(nums)
        product_left = 1
        for i, n in enumerate(nums):
            product_left *= n
            product_from_left[i] = product_left
        product_from_right = [0]*len(nums)
        product_right = 1
        reversed_nums = reversed(nums)
        for i, n in enumerate(reversed_nums):
            product_right *= n
            product_from_right[i] = product_right
        result = [0]*len(nums)
        for i in range(1, len(nums)-1):
            result[i] = product_from_left[i-1]*product_from_right[len(nums)-i-2]
        result[0] = product_from_right[len(nums)-2]
        result[len(nums)-1] = product_from_left[len(nums)-2]
        return result