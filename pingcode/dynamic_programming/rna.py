#!/usr/bin/env python3

import heapq

from pingcode.util import Problem


def is_pair(c0, c1):
    if c0 == 'C':
        return c1 == 'G'
    elif c0 == 'A':
        return c1 == 'U'
    elif c0 == 'U':
        return c1 in ['G', 'A']
    elif c0 == 'G':
        return c1 in ['C', 'U']
    return False


class RNAMaximumPairs(Problem):
    def max_pair_structure(self, rna):
        dp_max = [[0 for _ in range(len(rna) + 1)] for _ in range(len(rna))]
        dp_pattern = [['.' if sub_l == 1 else ''
                       for sub_l in range(len(rna) + 1)]
                      for _ in range(len(rna))]

        for sub_l in range(2, len(rna) + 1):
            for start in range(len(rna) - sub_l + 1):
                end = start + sub_l - 1
                dp_max[start][sub_l] = dp_max[start][sub_l - 1]
                dp_pattern[start][sub_l] = dp_pattern[start][sub_l - 1] + '.'

                for prefix_l in range(sub_l - 1):
                    infix_l = max(0, sub_l - 2 - prefix_l)
                    i = start + prefix_l

                    prefix_max = dp_max[start][prefix_l]
                    infix_max = dp_max[i + 1][infix_l]
                    new_pair = 1 if is_pair(rna[i], rna[end]) else 0
                    total_max = prefix_max + infix_max + new_pair
                    if dp_max[start][sub_l] < total_max:
                        dp_max[start][sub_l] = total_max
                        if new_pair == 1:
                            dp_pattern[start][sub_l] = (
                                dp_pattern[start][prefix_l] +
                                '(' + dp_pattern[i + 1][infix_l] + ')'
                            )
                        else:
                            dp_pattern[start][sub_l] = (
                                dp_pattern[start][prefix_l] +
                                '.' + dp_pattern[i + 1][infix_l] + '.'
                            )

        return dp_max[0][len(rna)], dp_pattern[0][len(rna)]

    def max_pair_structure_alternative(self, rna):
        """
        '--prefix--(--infix--)'
        """
        dp_max = [[0 for _ in range(len(rna) + 1)] for _ in range(len(rna))]
        dp_back = [['.' if start <= end else ''
                    for end in range(len(rna))]
                   for start in range(len(rna))]

        for n in range(2, len(rna) + 1):
            for start in range(len(rna) - n + 1):
                end = start + n - 1
                for i in range(start, end):
                    prefix_pairs = dp_max[start][i - 1] if i >= 1 else 0
                    infix_pairs = dp_max[i + 1][end - 1]
                    new_pair = 1 if is_pair(rna[i], rna[end]) else 0
                    total_pairs = prefix_pairs + infix_pairs + new_pair

                    if total_pairs >= dp_max[start][end]:
                        dp_max[start][end] = total_pairs
                        if new_pair == 1:
                            dp_back[start][end] = (
                                dp_back[start][i - 1] +
                                '(' + dp_back[i + 1][end - 1] + ')'
                            )
                        #else:
                        #    dp_back[start][end] = (
                        #        dp_back[start][i - 1] +
                        #        '.' + dp_back[i + 1][end - 1] + '.'
                        #    )

        return dp_max[0][len(rna) - 1], dp_back[0][len(rna) - 1]

    def import_testcases(self):
        rna = 'GCACG'
        out = (2, '().()')
        self.add_testcase(rna, out)

        rna = 'UUCAGGA'
        out = (3, '(((.)))')
        self.add_testcase(rna, out)

        rna = 'GUUAGAGUCU'
        out = (4, '((())(.)).')
        self.add_testcase(rna, out)

        rna = 'AUAACCUUAUAGGGCUCUG'
        out = (8, '(()(((((())))).).).')
        self.add_testcase(rna, out)

        rna = 'AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU'
        out = (11, '(((.).)((().)(()..()..)()))()..')
        self.add_testcase(rna, out)

        rna = 'GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG'
        out = (14, '(((()()(()))))(((((.))(.)(.)))).')
        self.add_testcase(rna, out)

        rna = 'CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU'
        out = (18, '(()())((((().)())(((())(.((().()).))))))')
        self.add_testcase(rna, out)

        rna = 'ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC'
        out = (19, '.()(((.)()..)((((()).(())))(((.)((())))))())')
        self.add_testcase(rna, out)

        rna = 'AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA'
        out = (20, '((()())...((((()()))((()(((()((.))).)())))))).')
        self.add_testcase(rna, out)

    def solve(self, test_in):
        return self.max_pair_structure(test_in)

    def evaluate(self, solution, test_out):
        return solution[0] == test_out[0]


class RNAStructureCombination(Problem):
    def total(self, rna):
        """
        pattern: '*(*)'
        """
        dp = [[1 if sub_l <= 1 else 0
               for sub_l in range(len(rna) + 1)]
              for _ in range(len(rna))]

        for sub_l in range(2, len(rna) + 1):
            for start in range(len(rna) - sub_l + 1):
                end = start + sub_l - 1

                dp[start][sub_l] += dp[start][sub_l - 1]
                for prefix_l in range(sub_l - 1):
                    infix_l = max(sub_l - prefix_l - 2, 0)
                    i = start + prefix_l
                    if is_pair(rna[i], rna[end]):
                        dp[start][sub_l] += (
                            dp[start][prefix_l] * dp[i + 1][infix_l]
                        )
                # print(f'dp[{start}][{sub_l}] = {dp[start][sub_l]}')

        return dp[0][len(rna)]

    def import_testcases(self):
        self.add_testcase('GCACG', 6)

    def solve(self, test_in):
        return self.total(test_in)


class RNAKbestPairs(Problem):
    def kbest(self, rna, k):
        dp = [[[] for _ in range(len(rna) + 1)] for _ in range(len(rna))]
        for i in range(len(rna)):
            dp[i][0] = [(0, '')]
            dp[i][1] = [(0, '.')]

        for sub_l in range(2, len(rna) + 1):
            for start in range(len(rna) - sub_l + 1):
                end = start + sub_l - 1
                pq = dp[start][sub_l]
                for num_pair, pattern in dp[start][sub_l - 1]:
                    self.pq_update(pq, k, (num_pair, pattern + '.'))

                for prefix_l in range(sub_l - 1):
                    infix_l = max(sub_l - prefix_l - 2, 0)
                    i = start + prefix_l
                    if not is_pair(rna[i], rna[end]):
                        continue

                    for prefix_pair, prefix in dp[start][prefix_l]:
                        for infix_pair, infix in dp[i + 1][infix_l]:
                            num_pair = prefix_pair + infix_pair + 1
                            pattern = prefix + '(' + infix + ')'
                            self.pq_update(pq, k, (num_pair, pattern))

        return sorted(dp[0][len(rna)])

    def pq_update(self, pq, k, entry):
        heapq.heappush(pq, entry)
        if len(pq) > k:
            heapq.heappop(pq)

    def import_testcases(self):
        rna = 'UCAGAGGCAUCAAACCU'
        k = 300
        out = [(2, '((.))'), (1, '(...)'), (1, '..(.)')]
        self.add_testcase((rna, k), out)

    def solve(self, test_in):
        rna, k = test_in
        return self.kbest(rna, k)
