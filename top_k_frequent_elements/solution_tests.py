from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_case_1(self):
        self.assertEqual([1, 2], self.sol.top_k_frequent_elements([1,1,1,2,2,3], 2))

    def test_case_2(self):
        self.assertEqual([1], self.sol.top_k_frequent_elements([1], 1))

if __name__ == '__main__':
    unittest.main()