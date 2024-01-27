#!/usr/bin/env python3

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
        """
        '--prefix--(--infix--)'
        """
        dp_max = [[0 for _ in range(len(rna))] for _ in range(len(rna))]
        dp_back = [['' for _ in range(len(rna))] for _ in range(len(rna))]
        for n in range(2, len(rna) + 1):
            for start in range(len(rna) - n):
                end = start + n - 1
                for i in range(start, end):
                    prefix_pairs = dp_max[start][i - 1]
                    infix_pairs = dp_max[i + 1][end - 1]
                    new_pair = 1 if is_pair(rna[i], rna[end]) else 0
                    total_pairs = prefix_pairs + infix_pairs + new_pair

                    if total_pairs >= dp_max[start][end]:
                        dp_max[start][end] = total_pairs
                        if new_pair == 1:
                            dp_back[start][end] = (dp_back[start][i - 1] +
                                '(' + dp_back[i + 1][end - 1] + ')')
                        else:
                            dp_back[start][end] = (dp_back[start][i - 1] +
                                '.' + dp_back[i + 1][end - 1] + '.')

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


class RNAStructureCombination(Problem):
    def total(self, rna):
        """
        pattern: '*(*)'
        """
        pass

    def import_testcases(self):
        self.add_testcase('GCACG', 6)

    def solve(self, test_in):
        return self.total(test_in)


class RNAKbestPairs(Problem):
    def kbest(self, rna):
        pass

    def import_testcases(self):
        rna = ''
        out = [(2, '((.))'), (1, '(...)'), (1, '..(.)')]
        self.add_testcase()
