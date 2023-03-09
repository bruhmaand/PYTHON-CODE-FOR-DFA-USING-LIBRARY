# Design a Program for creating machine that accepts three consecutive one.

#only consecutive 111

# pip install automata-lib
from automata.fa.dfa import DFA

dfa = DFA(
    states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q0", "1": "q2"},
        "q2": {"0": "q0", "1": "q3"},
        "q3": {"0": "q5", "1": "q4"},
        "q4": {"0": "q4", "1": "q4"},
        "q5": {"0": "q5", "1": "q6"},
        "q6": {"0": "q5", "1": "q7"},
        "q7": {"0": "q5", "1": "q3"},
    },
    initial_state="q0",
    final_states={"q3", "q5", "q6", "q7"},
)
n = input("Enter string:")
if dfa.accepts_input(n):
    print("Accepted")
else:
    print("Rejected")