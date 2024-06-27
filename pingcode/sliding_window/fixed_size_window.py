#!/usr/bin/env python3

import collections

from pingcode.util import Problem


class PermutationInString(Problem):
    def leetcode_id(self):
        return 567

    def description(self):
        return "Given s1 and s2, check if reordered s1 is a part of s2."

    def permute_match(self, s1, s2):

        frequency1 = collections.Counter()
        frequency2 = collections.Counter()
        for i in range(len(s1)):
            frequency1[s1[i]] += 1
            frequency2[s2[i]] += 1

        # sliding window
        incompleted_unique_chars = len(frequency1.keys())
        for end in range(len(s1), len(s2)):
            # first, increase/decrease frequency by including the 'end' char
            end_char = s2[end]
            end_char_target_frequency = frequency1[end_char]
            if end_char in frequency1:
                frequency2[end_char] += 1
                if frequency2[end_char] == end_char_target_frequency:
                    incompleted_unique_chars -= 1
                elif frequency2[end_char] == end_char_target_frequency + 1:
                    incompleted_unique_chars += 1

            # then, increase/decrease frequency by including the 'start - 1' char
            start_char = s2[end - len(s1)]
            start_char_target_frequency = frequency1[start_char]
            if start_char in frequency1:
                if frequency2[start_char] == start_char_target_frequency:
                    incompleted_unique_chars += 1
                elif frequency2[start_char] == start_char_target_frequency + 1:
                    incompleted_unique_chars -= 1
                frequency2[start_char] -= 1

            # if we have completed all the chars
            if incompleted_unique_chars == 0:
                return True

        return False


    def import_testcases(self):
        test_in = ("abc", "bbbca")
        self.add_testcase(test_in, True)

        test_in = ("ab", "eidbaooo")
        self.add_testcase(test_in, True)

        test_in = ("ba", "eidboaoo")
        self.add_testcase(test_in, False)

    def solve(self, test_in):
        s1, s2 = test_in
        assert(len(s1) < len(s2))
        return self.permute_match(s1, s2)
