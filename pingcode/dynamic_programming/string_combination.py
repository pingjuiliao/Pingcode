#!/usr/bin/env python3

from pingcode.util import Problem


class BitstringNoConsecutiveOnes(Problem):
    def num_bitstring(self, length):
        """
        for each length:
            10****
            0*****
        """
        dp = {-1: 1, 0: 1}
        for i in range(1, length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[length]

    def import_testcases(self):
        self.add_testcase(3, 5)
        self.add_testcase(32, 5702887)
        self.add_testcase(0, 1)
        self.add_testcase(1, 2)

    def solve(self, test_in):
        return self.num_bitstring(test_in)
