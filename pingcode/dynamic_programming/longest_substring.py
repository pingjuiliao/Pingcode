#!/usr/bin/env python3

from pingcode.util import Problem


class LongestPalindrome(Problem):
    def longest(self, s):
        """
        No dynamic programming required: just expand from the middle: O(N^2)
        """
        max_len = 0
        max_str = ""
        for left in range(len(s)):
            for right in range(left, left + 2):
                while 0 <= left and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                left = left + 1
                right = right - 1
                curr_len = right - left + 1
                if curr_len > max_len:
                    max_len = curr_len
                    max_str = s[left: right + 1]
        return max_str

    def import_testcases(self):
        self.add_testcase("caba", 3)
        self.add_testcase("babad", 3)
        self.add_testcase("cbbd", 2)

    def solve(self, test_in):
        return self.longest(test_in)

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True

    def evaluate(self, solution, test_out):
        return (self.is_palindrome(solution) and len(solution) == test_out)

class LongestParenthesis(Problem):
    def longest(self, s):
        dp = [0] * len(s)
        max_len = 0

        for close_idx in range(len(s)):
            if s[close_idx] != ')':
                continue
            if s[close_idx - 1] == '(':
                dp[close_idx] = dp[close_idx - 2] + 2 if close_idx >= 2 else 2
            else:
                open_idx = close_idx - 1 - dp[close_idx - 1]
                if (open_idx < 0 or s[open_idx] != '(' or
                    dp[close_idx - 1] == 0):
                    continue
                dp[close_idx] = dp[close_idx - 1] + 2
                if open_idx >= 1:
                    dp[close_idx] += dp[open_idx - 1]
            max_len = max(max_len, dp[close_idx])
        return max_len


    def import_testcases(self):
        self.add_testcase("(()", 2)
        self.add_testcase(")()())", 4)

        test_in = """
())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())("""

        self.add_testcase(test_in.strip(), 310)

    def solve(self, test_in):
        return self.longest(test_in)
