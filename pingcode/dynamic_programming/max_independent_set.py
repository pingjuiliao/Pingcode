#!/usr/bin/env python3

from pingcode.util import Problem


class MaxIndependentSet(Problem):
    def max_independent_set_with_path(self, nums):
        best = {-1: 0, -2: 0}
        back = [None] * len(nums)

        for i, n in enumerate(nums):
            best[i] = max(best[i - 1], best[i - 2] + n)
            back[i] = best[i] == best[i - 1]

        return best[len(nums) - 1], self.backtrack(nums, back, len(nums) - 1)

    def backtrack(self, nums, back, i):
        if i < 0:
            return []
        if back[i]:
            return self.backtrack(nums, back, i - 1)
        return self.backtrack(nums, back, i - 2) + [nums[i]]

    def import_testcases(self):
        test_in = [6, 16, 0, 12, 17, 20, 7]
        test_out = (48, [16, 12, 20])
        self.add_testcase(test_in, test_out)

        test_in = [-9, 13, 13, -8, -9, 13, 3]
        test_out = (26, [13, 13])
        self.add_testcase(test_in, test_out)

        test_in = [5, 10, -6, 8, 9, 15, 2]
        test_out = (33, [10, 8, 15])
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        return self.max_independent_set_with_path(test_in)
