from tokenizer.tokenizer import *
from syntax_analyzer.parser import *

def run(input_expression):
    tokenizer = Tokenizer()
    tokenizer.tokenize(input_expression)
    tokens, error = tokenizer.tokenize(input_expression)
    if error: return None, error

    parser = Parser(tokens)
    res, error = parser.parse()
    if error: return None, error

    return None, None