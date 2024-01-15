from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([1,2,3,4,4]))

    def test_no_duplicate(self):
        self.assertFalse(self.sol.containsDuplicate([]))
        self.assertFalse(self.sol.containsDuplicate([1,2,3]))

    def test_case_1(self):
        self.assertTrue(self.sol.containsDuplicate([1,2,3,1]))
    
    def test_case_2(self):
        self.assertFalse(self.sol.containsDuplicate([1,2,3,4]))
    
    def test_case_3(self):
        self.assertTrue(self.sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == '__main__':
    unittest.main()