class Token:
    tokens = []

    def symbol_table(self):
        print('-' * 55)
        print("Symbol Table".center(53))
        print('-' * 55)
        print("Line Number".ljust(20), "Lexemes".ljust(20), "Tokens".ljust(20))
        print('-' * 55)
        for token in self.tokens:
            print("{}".format(list(token.keys()).pop()).ljust(20),
                  "{}".format(list(token[list(token.keys()).pop()].keys()).pop()).ljust(20),
                  "{}".format(
                      token[list(token.keys()).pop()][list(token[list(token.keys()).pop()].keys()).pop()]).ljust(20))
        print('-' * 55)
        print("Total Number of Tokens: {}".format(len(self.tokens)))

# for reference

# list(token.keys()).pop() --> THE LINE NUMBER

# list(token[list(token.keys()).pop()].keys()).pop() --> THE LEXEMES

# token[list(token.keys()).pop()][list(token[list(token.keys()).pop()].keys()).pop()]  --> THE TOKENS
