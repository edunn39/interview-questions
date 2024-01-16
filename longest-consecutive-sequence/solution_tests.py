from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_case_1(self):
        self.assertEqual(4, self.sol.longest_consecutive([100,4,200,1,3,2]))

    def test_case_2(self):
        self.assertEqual(9, self.sol.longest_consecutive([0,3,7,2,5,8,4,6,0,1]))

if __name__ == '__main__':
    unittest.main()