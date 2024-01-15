from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_case_1(self):
        self.assertEqual([24,12,8,6], self.sol.product_of_array_except_self([1,2,3,4]))

    def test_case_2(self):
        self.assertEqual([0,0,9,0,0], self.sol.product_of_array_except_self([-1,1,0,-3,3]))

if __name__ == '__main__':
    unittest.main()