from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_case_1(self):
        self.assertEqual([1, 2], self.sol.two_sum([2,7,11,15], 9))

    def test_case_2(self):
        self.assertEqual([1, 3], self.sol.two_sum([2,3,4], 6))

    def test_case_3(self):
        self.assertEqual([1, 2], self.sol.two_sum([-1,0], -1))

if __name__ == '__main__':
    unittest.main()