from tokenizer import tokenizer
from tokenizer.gen_tokens import *
from syntax_analyzer.parser import *

tokenizer.tokenize()  # Initiate Tokenizer
Parse(Token.tokens)  # Initiate Parser and pass the tokens as parameters
Token().symbol_table() # Prints the symbol table