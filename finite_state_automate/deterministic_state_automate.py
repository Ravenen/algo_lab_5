from typing import Callable, List, Dict


def get_next_state_by_letter(pattern_string: str, letter: str, current_state: int, longest_prefix_suffix: int,
                             transition_function):
    if current_state < len(pattern_string) and pattern_string[current_state] == letter:
        return current_state + 1
    return transition_function[longest_prefix_suffix][letter]


def fill_in_zero_state(transition_function: List[Dict[str, int]], pattern_string: str, alphabet: List[str]):
    for letter in alphabet:
        transition_function[0][letter] = 0
    transition_function[0][pattern_string[0]] = 1


def generate_transition_function(pattern_string: str, alphabet: List[str]):
    number_of_states = len(pattern_string) + 1

    transition_function = [{letter: 0 for letter in alphabet} for _ in range(number_of_states)]

    fill_in_zero_state(transition_function, pattern_string, alphabet)

    longest_prefix_suffix = 0
    for state in range(1, number_of_states):
        for letter in alphabet:
            transition_function[state][letter] = get_next_state_by_letter(pattern_string, letter, state,
                                                                          longest_prefix_suffix, transition_function)
        if state < number_of_states - 1:
            longest_prefix_suffix = transition_function[longest_prefix_suffix].get(pattern_string[state])
    return transition_function


def perform_search_on_string(input_string: str, pattern_string: str, output_function: Callable,
                             transition_function: List[Dict[str, int]]):
    state = 0
    for index, letter in enumerate(input_string):
        state = transition_function[state].get(letter)
        if state == len(pattern_string):
            start_index = index - len(pattern_string) + 1
            end_index = index
            output_function(start_index, end_index)


def search_substring(input_string: str, pattern_string: str, output_function: Callable, alphabet: List[str] = None):
    if alphabet is None:
        alphabet = [chr(code) for code in range(256)]
    transition_function = generate_transition_function(pattern_string, alphabet)
    perform_search_on_string(input_string, pattern_string, output_function, transition_function)
