#!/usr/bin/env python3

from pingcode.util import Problem


class NumBST(Problem):
    def num_bst(self, num_nodes: int):
        dp = [0 for _ in range(num_nodes + 1)]
        dp[0] = dp[1] = 1
        for n in range(2, num_nodes + 1):
            for root_idx in range(n):
                num_left = root_idx
                num_right = n - 1 - root_idx
                dp[n] += dp[num_left] * dp[num_right]
        return dp[num_nodes]

    def import_testcases(self):
        self.add_testcase(19, 1767263190)
        self.add_testcase(10, 16796)
        self.add_testcase(1, 1)

    def solve(self, test_in):
        return self.num_bst(test_in)
