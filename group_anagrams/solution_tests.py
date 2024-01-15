from solution import Solution
import unittest

class Test(unittest.TestCase):

    sol = Solution()

    def test_case_1(self):
        self.assertEqual([["eat","tea","ate"],["tan","nat"],["bat"]], self.sol.group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    
    def test_case_2(self):
        self.assertEqual([[""]], self.sol.group_anagrams([""]))
    
    def test_case_3(self):
        self.assertEqual([["a"]], self.sol.group_anagrams(["a"]))

if __name__ == '__main__':
    unittest.main()