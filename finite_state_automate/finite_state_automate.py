def get_longest_prefix_suffix(pattern_string, code, current_state):
    temporary_string = pattern_string[:current_state] + chr(code) + pattern_string[current_state + 1:]
    result = 0
    for possible_state in range(current_state):
        for offset in range(possible_state + 1):
            if ord(pattern_string[offset]) != ord(temporary_string[current_state - possible_state + offset]):
                break
        else:
            result = max(result, possible_state + 1)
    return result


def get_next_state_by_code(pattern_string, code, current_state):
    if ord(pattern_string[current_state]) == code:
        return current_state + 1
    return get_longest_prefix_suffix(pattern_string, code, current_state)


def generate_transition_function(pattern_string, alphabet):
    alphabet_length = len(alphabet)
    number_of_states = len(pattern_string) + 1

    transition_function = [[0 for i in range(alphabet_length)] for j in range(number_of_states)]

    for state in range(number_of_states - 1):
        for letter_index, letter in enumerate(alphabet):
            transition_function[state][letter_index] = get_next_state_by_code(pattern_string, ord(letter), state)
    return transition_function


def search_substring(input_string, pattern_string, output_function, alphabet=None):
    if alphabet is None:
        alphabet = [chr(code) for code in range(256)]
    transition_function = generate_transition_function(pattern_string, alphabet)

    state = 0
    for index, letter in enumerate(input_string):
        state = transition_function[state][alphabet.index(letter)]
        if state == len(pattern_string):
            start_index = index - len(pattern_string) + 1
            end_index = index
            output_function(start_index, end_index)


if __name__ == '__main__':
    output_list = []
    search_substring("testStringGoesHeretr", "tr", lambda start, end: output_list.append((start, end)))
    print(output_list)
