from typing import Tuple, List
from finite_state_automate import deterministic_state_automate as dfa

INPUT_FILENAME = "search.in"
OUTPUT_FILENAME = "search.out"


def get_input_strings_for_file(filename: str) -> Tuple[str, str]:
    with open(filename, "r") as file:
        input_string = file.readline().strip()
        pattern_string = file.readline().strip()
    return input_string, pattern_string


def write_result_list_to_file(filename: str, results: List[Tuple[int, int]]):
    with open(filename, "w") as file:
        for result in results:
            file.write(f"{result[0]} {result[1]}\n")


if __name__ == '__main__':
    string, pattern = get_input_strings_for_file(INPUT_FILENAME)
    results_list = []
    dfa.search_substring(string, pattern, lambda start, end: results_list.append((start, end)))
    write_result_list_to_file(OUTPUT_FILENAME, results_list)
