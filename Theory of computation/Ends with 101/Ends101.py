# Design a Program for creating machine that accepts the string always ending with 101.

# pip install automata-lib
from automata.fa.dfa import DFA

dfa = DFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q2", "1": "q1"},
        "q2": {"0": "q0", "1": "q3"},
        "q3": {"0": "q2", "1": "q1"},
    },
    initial_state="q0",
    final_states={"q3"},
)
n = input("Enter string:")
if dfa.accepts_input(n):
    print("Accepted")
else:
    print("Rejected")