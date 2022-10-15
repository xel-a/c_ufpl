# I was dumb enough to use word_tokenize but later used regexp_tokenize instead because it has regex :p
from nltk import regexp_tokenize as tk
from tokenizer import gen_tokens
from tokenizer import structure
import string


# this generates tokens and takes in lexemes and line number as paramters
def generate_tokens(lexemes: string, line: int):
    tokenizer = gen_tokens.Token()
    # I used this regex pattern to ignore spaces whilst matching the rest :3
    for lex in tk(lexemes, pattern="[-+]?[0-9]*\.?[0-9]+|[<=>]+|\w+|[#&[\](){}'\",:+\-*/<>=.]"):
        if lex.upper() in structure.operators.keys():
            tokenizer.tokens.append({line: {lex: structure.operators[lex]}})
        elif lex.upper() in structure.keywords:
            tokenizer.tokens.append({line: {lex: "KEYWORD"}})
        elif lex.isdigit():
            tokenizer.tokens.append({line: {lex: "INTEGER"}})
        elif lex.upper() in structure.separators:
            tokenizer.tokens.append({line: {lex: "SEPARATOR"}})
        else:
            try:  # trying to catch a wild float :3
                float(lex)
                tokenizer.tokens.append({line: {lex: "FLOAT"}})
            except ValueError:
                tokenizer.tokens.append({line: {lex: "IDENTIFIER"}})


# tokenizes the code snippet by line
def tokenize():
    code = open("tokenizer/code.txt", 'r')
    for i, lexemes in enumerate(code):
        generate_tokens(lexemes, i + 1)
