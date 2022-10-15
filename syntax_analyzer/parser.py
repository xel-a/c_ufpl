from c_ufpl.tokenizer.gen_tokens import *
from c_ufpl.tokenizer import tokenizer

class Parse:
    def __init__(self, tokens):
        for i, token in enumerate(tokens):
            if list(token[list(token.keys()).pop()].keys()).pop() == '*':
                print("Caught!", i) # now that I caught it how to determine if it is a comment :3