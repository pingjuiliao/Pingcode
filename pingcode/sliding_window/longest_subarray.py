#!/usr/bin/env python3

import collections

from pingcode.util import Problem


class LongestSubarrayWithAtMostKFrequency(Problem):
    def max_subarray_length(self, nums, k):
        max_length = 0
        frequency = collections.Counter()

        start = 0
        for end, num in enumerate(nums):
            frequency[num] += 1

            while frequency[num] > k:
                frequency[nums[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


    def import_testcases(self):
        test_in = ([1, 2, 3, 1, 2, 3, 1, 2], 2)
        self.add_testcase(test_in, 6)

        test_in = ([1, 2, 1, 2, 1, 2, 1, 2], 1)
        self.add_testcase(test_in, 2)

        test_in = ([5, 5, 5, 5, 5, 5, 5], 4)
        self.add_testcase(test_in, 4)


    def solve(self, test_in):
        nums, k = test_in
        return self.max_subarray_length(nums, k)
