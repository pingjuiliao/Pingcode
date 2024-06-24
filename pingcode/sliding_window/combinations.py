#!/usr/bin/env python3

import collections

from pingcode.util import Problem

class TotalSubarrayProductLessThanK(Problem):
    def total_subarrray_with_product_less_than_k(self, nums, k):
        total_subarray = 0

        current_product = 1
        start = 0
        for end, num in enumerate(nums):
            current_product *= num
            while current_product >= k and start < end:
                current_product //= nums[start]
                start += 1

            if current_product < k:
                total_subarray += end - start + 1

        return total_subarray


    def import_testcases(self):
        test_in = ([10, 5, 2, 6], 100)
        self.add_testcase(test_in, 8)

        test_in = ([1,2,3], 0)
        self.add_testcase(test_in, 0)

    def solve(self, test_in):
        nums, k = test_in
        return self.total_subarrray_with_product_less_than_k(nums, k)


class TotalSubarrayWithAtLeastKMaxElement(Problem):
    def count_subarrays(self, nums, k):
        max_num = max(nums)
        total_subarray = 0

        start = 0
        max_num_frequency = 0
        for end, num in enumerate(nums):
            if num == max_num:
                max_num_frequency += 1

            # we always keep (k - 1) max_num in the window
            while max_num_frequency >= k:
                if nums[start] == max_num:
                    max_num_frequency -= 1
                start += 1

            # nums[start - 1] should be the k-th max_num
            # we don't check if start > 1 since if start == 0 we don't
            # change the answer
            total_subarray += start

        return total_subarray

    def import_testcases(self):
        test_in = ([1, 3, 2, 3, 3], 2)
        self.add_testcase(test_in, 6)

        test_in = ([1, 3, 2, 3, 2], 2)
        self.add_testcase(test_in, 4)

        test_in = ([1, 4, 2, 1], 3)
        self.add_testcase(test_in, 0)

    def solve(self, test_in):
        nums, k = test_in
        return self.count_subarrays(nums, k)


class TotalSubarrayWithFixedBounds(Problem):
    def subarray_fixed_bounds(self, nums, min_k, max_k):
        total_subarray = 0

        start = 0
        last_min_index = -1  # the last index of min_k in current window
        last_max_index = -1  # the last index of max_k in current window
        for end, num in enumerate(nums):
            # if the number is out of range, break the window by renewing start
            # and invalidate last_min_index, last_max_index
            if num < min_k or max_k < num:
                start = end + 1
                last_min_index = -1
                last_max_index = -1
                continue

            if num == min_k:
                last_min_index = end
            if num == max_k:
                last_max_index = end

            # if we have both min_k and max_k in current window
            if last_min_index >= 0 and last_max_index >= 0:
                last_valid_index = min(last_min_index, last_max_index)
                total_subarray += (last_valid_index - start + 1)

        return total_subarray

    def pseudocode(self):
        return "see leetcode 2444 for explanation"

    def import_testcases(self):
        test_in = ([1,3,5,2,7,5], 1, 5)
        self.add_testcase(test_in, 2)

        test_in = ([1,1,1,1], 1, 1)
        self.add_testcase(test_in, 10)

    def solve(self, test_in):
        nums, min_k, max_k = test_in
        return self.subarray_fixed_bounds(nums, min_k, max_k)
