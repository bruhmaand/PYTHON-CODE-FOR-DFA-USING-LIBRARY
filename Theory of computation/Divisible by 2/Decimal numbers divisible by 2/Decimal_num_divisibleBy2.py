# Design a program for accepting decimal number divisible by 2.

# pip install automata-lib on terminal or CMD
from automata.fa.dfa import DFA

dfa = DFA(
    states={"q0", "q1"},
    input_symbols={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
    transitions={
        "q0": {
            "0": "q0",
            "1": "q1",
            "2": "q0",
            "3": "q1",
            "4": "q0",
            "5": "q1",
            "6": "q0",
            "7": "q1",
            "8": "q0",
            "9": "q1",
        },
        "q1": {
            "0": "q0",
            "1": "q1",
            "2": "q0",
            "3": "q1",
            "4": "q0",
            "5": "q1",
            "6": "q0",
            "7": "q1",
            "8": "q0",
            "9": "q1",
        },
    },
    initial_state="q0",
    final_states={"q0"},
)
n = input("Enter string:")
if dfa.accepts_input(n):
    print("Accepted")
else:
    print("Rejected")
