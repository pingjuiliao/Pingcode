#!/usr/bin/env python3

import collections

from pingcode.util import Problem


class Powerset(Problem):
    def get_powerset(self, nums):
        powerset = []
        for bitmask in range(1 << len(nums)):
            subset = []
            for i, num in enumerate(nums):
                if (bitmask >> i) & 1:
                    subset.append(num)

            powerset.append(subset)

        return powerset

    def import_testcases(self):
        test_in = [1,2,3,4]
        test_out = [[],[1],[1,2],[1,2,3],[1,2,3,4],[1,2,4],[1,3],[1,3,4],
                    [1,4],[2],[2,3],[2,3,4],[2,4],[3],[3,4],[4]]
        self.add_testcase(test_in, test_out)

        test_in = [1,2,3,4,5,6]
        test_out = [[],[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],
                    [1,2,3,4,6],[1,2,3,5],[1,2,3,5,6],[1,2,3,6],[1,2,4],
                    [1,2,4,5],[1,2,4,5,6],[1,2,4,6],[1,2,5],[1,2,5,6],[1,2,6],
                    [1,3],[1,3,4],[1,3,4,5],[1,3,4,5,6],[1,3,4,6],[1,3,5],
                    [1,3,5,6],[1,3,6],[1,4],[1,4,5],[1,4,5,6],[1,4,6],[1,5],
                    [1,5,6],[1,6],[2],[2,3],[2,3,4],[2,3,4,5],[2,3,4,5,6],
                    [2,3,4,6],[2,3,5],[2,3,5,6],[2,3,6],[2,4],[2,4,5],
                    [2,4,5,6],[2,4,6],[2,5],[2,5,6],[2,6],[3],[3,4],[3,4,5],
                    [3,4,5,6],[3,4,6],[3,5],[3,5,6],[3,6],[4],[4,5],[4,5,6],
                    [4,6],[5],[5,6],[6]]
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        return self.get_powerset(test_in)

    def evaluate(self, solution, test_out):
        return sorted(solution) == sorted(test_out)


class PowersetWithDuplicate(Problem):
    def get_powerset(self, nums):
        """
        It turns out that backtracking is the most efficient way to sovle this.
        """
        self.counter = collections.Counter(nums)

        self.result = []
        self.backtrack([], [num for num in self.counter])
        return self.result

    def backtrack(self, selected, unique_nums):
        self.result.append(selected)
        for i, num in enumerate(unique_nums):
            for cnt in range(1, self.counter[num] + 1):
                self.backtrack(selected + [num] * cnt, unique_nums[i+1:])

    def import_testcases(self):
        test_in = [1,2,2]
        test_out = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        self.add_testcase(test_in, test_out)

        test_in = [0]
        test_out = [[],[0]]
        self.add_testcase(test_in, test_out)

        test_in = [4,1,2,2,1,2,1,1]
        test_out = [[],[4],[4,1],[4,1,2],[4,1,2,2],[4,1,2,2,2],[4,1,1],
                    [4,1,1,2],[4,1,1,2,2],[4,1,1,2,2,2],[4,1,1,1],[4,1,1,1,2],
                    [4,1,1,1,2,2],[4,1,1,1,2,2,2],[4,1,1,1,1],[4,1,1,1,1,2],
                    [4,1,1,1,1,2,2],[4,1,1,1,1,2,2,2],[4,2],[4,2,2],[4,2,2,2],
                    [1],[1,2],[1,2,2],[1,2,2,2],[1,1],[1,1,2],[1,1,2,2],
                    [1,1,2,2,2],[1,1,1],[1,1,1,2],[1,1,1,2,2],[1,1,1,2,2,2],
                    [1,1,1,1],[1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,1,2,2,2],[2],
                    [2,2],[2,2,2]]
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        return self.get_powerset(test_in)

    def evaluate(self, solution, test_out):
        return sorted(solution) == sorted(test_out)
