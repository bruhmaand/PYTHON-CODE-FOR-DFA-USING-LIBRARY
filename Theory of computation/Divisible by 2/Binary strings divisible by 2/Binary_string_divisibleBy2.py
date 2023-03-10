# Design a program for accepting Binary string divisible by 2.

# pip install automata-lib
from automata.fa.dfa import DFA

dfa = DFA(
    states={"q0", "q1"},
    input_symbols={"0", "1"},
    transitions={
      "q0": {"0": "q0", "1": "q1"},
      "q1": {"0": "q0", "1": "q1"}
    },
    initial_state="q0",
    final_states={"q0"},
)
n = input("Enter string:")
if dfa.accepts_input(n):
    print("Accepted")
else:
    print("Rejected")

# github.com/bruhmaand