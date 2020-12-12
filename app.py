from finite_state_automate import deterministic_state_automate as dfa

if __name__ == '__main__':
    input_string = "HelloWorldIAmWritingRandomTextWithRepeatingLetters"
    search_string = "ing"
    dfa.search_substring(input_string, search_string, print)
