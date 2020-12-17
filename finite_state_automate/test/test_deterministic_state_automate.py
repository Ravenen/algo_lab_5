import unittest

from ..deterministic_state_automate import *


class Test(unittest.TestCase):

    def test_generate_transition_function(self):
        self.assertListEqual(
            [{'A': 1, 'C': 0, 'G': 0, 'T': 0}, {'A': 1, 'C': 2, 'G': 0, 'T': 0}, {'A': 3, 'C': 0, 'G': 0, 'T': 0},
             {'A': 1, 'C': 4, 'G': 0, 'T': 0}, {'A': 5, 'C': 0, 'G': 0, 'T': 0}, {'A': 1, 'C': 4, 'G': 6, 'T': 0},
             {'A': 7, 'C': 0, 'G': 0, 'T': 0}, {'A': 1, 'C': 2, 'G': 0, 'T': 0}],
            generate_transition_function("ACACAGA", ['A', 'C', 'G', 'T']))
        self.assertListEqual([{'A': 1}, {'A': 2}, {'A': 3}, {'A': 3}], generate_transition_function("AAA", ['A']))
        self.assertListEqual(
            [{'A': 1, 'B': 0, 'C': 0, 'D': 0}, {'A': 1, 'B': 2, 'C': 0, 'D': 0}, {'A': 1, 'B': 0, 'C': 3, 'D': 0},
             {'A': 1, 'B': 0, 'C': 0, 'D': 4}, {'A': 1, 'B': 0, 'C': 0, 'D': 0}],
            generate_transition_function("ABCD", ['A', 'B', 'C', 'D']))

    def test_search_substring(self):
        def append_to_list(input_list):
            def add_tuple(start, end):
                input_list.append((start, end))

            return add_tuple

        output_list_first = []
        search_substring("ABCABCABCABDABC", "ABCABDA", append_to_list(output_list_first))
        self.assertListEqual([(6, 12)], output_list_first)

        output_list_second = []
        search_substring("AABAACAAD", "AA", append_to_list(output_list_second))
        self.assertListEqual([(0, 1), (3, 4), (6, 7)], output_list_second)

        output_list_third = []
        search_substring("AAAAAAAC", "AA", append_to_list(output_list_third))
        self.assertListEqual([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)], output_list_third)

        output_list_forth = []
        search_substring("HelloWorld", "test", append_to_list(output_list_forth))
        self.assertListEqual([], output_list_forth)


if __name__ == '__main__':
    unittest.main()
