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


class LongestConsecutiveOnesAfterDeletingOneElement(Problem):
    def leetcode_id(self):
        return 1493

    def description(self):
        return """ return longest consecutive ones where you are allowed to delete one element """

    def longest(self, nums):
        max_length = 0
        start = 0
        zeros_in_window = 0
        for end, num in enumerate(nums):
            if num == 0:
                zeros_in_window += 1

            while zeros_in_window > 1:
                if nums[start] == 0:
                    zeros_in_window -= 1
                start += 1

            # Because we "must" delete one element:
            # curr_window_length = (end - start + 1) - 1
            max_length = max(max_length, end - start)

        return max_length

    def import_testcases(self):
        self.add_testcase([1,1,0,1], 3)
        self.add_testcase([1,1,1], 2)
        self.add_testcase([0,1,1,1,0,1,1,0,1], 5)

    def solve(self, test_in):
        nums = test_in
        return self.longest(nums)
