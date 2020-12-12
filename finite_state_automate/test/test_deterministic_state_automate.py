import unittest

from ..deterministic_state_automate import *


class Test(unittest.TestCase):
    def test_get_longest_prefix_suffix(self):
        self.assertEqual(0, get_longest_prefix_suffix("ABCD", ord('B'), 3))
        self.assertEqual(2, get_longest_prefix_suffix("ABAD", ord('B'), 3))
        self.assertEqual(1, get_longest_prefix_suffix("ABAD", ord('A'), 3))
        self.assertEqual(0, get_longest_prefix_suffix("ACACAGA", ord('C'), 6))
        self.assertEqual(4, get_longest_prefix_suffix("ACACAGA", ord('C'), 5))
        self.assertEqual(3, get_longest_prefix_suffix("ABCABDFF", ord('C'), 5))

    def test_get_next_state_by_code(self):
        self.assertEqual(0, get_next_state_by_code("ABCD", ord('B'), 2))
        self.assertEqual(2, get_next_state_by_code("ABCD", ord('B'), 1))
        self.assertEqual(1, get_next_state_by_code("ABCD", ord('A'), 2))
        self.assertEqual(1, get_next_state_by_code("ABCABDFF", ord('A'), 2))
        self.assertEqual(4, get_next_state_by_code("ABCABDFF", ord('A'), 3))

    def test_generate_transition_function(self):
        self.assertListEqual(
            [[1, 0, 0, 0], [1, 2, 0, 0], [3, 0, 0, 0], [1, 4, 0, 0], [5, 0, 0, 0], [1, 4, 6, 0], [7, 0, 0, 0],
             [0, 0, 0, 0]], generate_transition_function("ACACAGA", ['A', 'C', 'G', 'T']))
        self.assertListEqual([[1], [2], [3], [0]], generate_transition_function("AAA", ['A']))
        self.assertListEqual([[1, 0, 0, 0], [1, 2, 0, 0], [1, 0, 3, 0], [1, 0, 0, 4], [0, 0, 0, 0]],
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


if __name__ == '__main__':
    unittest.main()
