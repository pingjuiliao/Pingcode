#!/usr/bin/env python3

from pingcode.util import Problem


class InterleavingString(Problem):

    def interleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        # return self.interleave_backtrack(s1, s2, s3)
        # return self.interleave_dp_optimized(s1, s2, s3)
        return self.interleave_dp(s1, s2, s3)

    def interleave_dp(self, s1, s2, s3):
        """
        Can s1 interleaves s2 to construct s3?
        """
        m, n = len(s1), len(s2)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (
                        (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or
                        (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                    )

        return dp[m][n]

    def interleave_backtrack(self, s1, s2, s3):
        self.memo = [[None for _ in range(len(s2))] for _ in range(len(s1))]
        def backtrack(s1, i1, s2, i2, s3, i3):
            if i3 >= len(s3):
                return True
            if i1 >= len(s1):
                return s2[i2:] == s3[i3:]
            if i2 >= len(s2):
                return s1[i1:] == s3[i3:]

            if self.memo[i1][i2] is not None:
                return self.memo[i1][i2]

            if ((s1[i1] == s3[i3] and backtrack(s1, i1 + 1, s2, i2, s3, i3 + 1)) or
                (s2[i2] == s3[i3] and backtrack(s1, i1, s2, i2 + 1, s3, i3 + 1))):
                self.memo[i1][i2] = True
                return True

            self.memo[i1][i2] = False
            return False

        return backtrack(s1, 0, s2, 0, s3, 0)

    def import_testcases(self):
        self.add_testcase(("aabcc", "dbbca", "aadbbcbcac"), True)
        self.add_testcase(("aabcc", "dbbca", "aadbbbaccc"), False)
        self.add_testcase(("", "", "a"), False)
        self.add_testcase(("", "", ""), True)

        s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
        s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
        s3 = ("babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbabab" +
              "aababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabb" +
              "bbabaaabbababbabbabbab")
        self.add_testcase((s1, s2, s3), False)
        self.add_testcase(("a" * 21, "a" * 37, "a" * 58), True)

    def solve(self, test_in):
        s1, s2, s3 = test_in
        return self.interleave(s1, s2, s3)
