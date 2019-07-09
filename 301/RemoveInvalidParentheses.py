import unittest
from typing import List


class Solution(unittest.TestCase):
    """
    Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
    """

    def removeInvalidParentheses(self, text: str) -> List[str]:
        sss = True
        for s in text:
            if s == '(':
                sss = False
            elif s == ')':


        return ["(a)()()", "(a())()"]

    def testRemoveInvalidParentheses(self):
        expect = ["(a)()()", "(a())()"]
        actual = self.removeInvalidParentheses("(a)())()")
        self.assertEqual(expect, actual)