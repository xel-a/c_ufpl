import re  # for regular expressions
from tokenizer.structure import *
from error.error import *


class Tokenizer:
    def __init__(self):
        self.tokens = []

    def add_token(self, line, datatype, value = None):
        if not value: self.tokens.append({
            "line": line,
            "type": datatype
        })
        else:
            self.tokens.append({
            "line": line,
            "type": datatype,
            "value": value
        })

    def tokenize(self, input_expression):
        current_index = 0
        line_no = 1
        alphabet = re.compile(r"[a-z_0-9]", re.I)  # matching alphabets
        numbers = re.compile(r"[0-9.]")  # matching numbers
        white_space = re.compile(r"\s")  # matching whitespace

        while (current_index < len(input_expression)):
            char = input_expression[current_index]

            # Newline
            if char == '\n':
                line_no += 1
                current_index += 1
                continue

            # Whitespace
            elif re.match(white_space, char):
                current_index += 1
                continue

            # Numbers
            elif re.match(numbers, char):
                dot_count = 0
                is_float = False
                value = ''
                while re.match(numbers, char):
                    if char == '.':
                        is_float = True
                        dot_count += 1
                    value += char
                    current_index += 1
                    if current_index < len(input_expression):
                        char = input_expression[current_index]
                    else:
                        break
                if dot_count > 1:
                    return InvalidSyntaxError(line_no, 'Multiple \'.\'')
                if is_float:
                    self.add_token(line_no, TT_FLOAT, value)
                else:
                    self.add_token(line_no, TT_INT, value)
                continue

            # Strings
            elif re.match(alphabet, char):
                value = ''
                while re.match(alphabet, char):
                    value += char
                    current_index += 1
                    if current_index < len(input_expression):
                        char = input_expression[current_index]
                    else:
                        break
                if f'KEY_{value}' in KEYWORDS:
                    self.add_token(line_no, KEYWORDS[f'KEY_{value}'])
                elif value in OPERATORS:
                    self.add_token(line_no, OPERATORS[value])
                else:
                    self.add_token(line_no, TT_STRING, value)
                continue

            # SEPARATORS
            elif char in SEPARATORS:
                if char == '(':
                    self.add_token(line_no, TT_LPAREN)
                    current_index += 1
                if char == ')':
                    self.add_token(line_no, TT_RPAREN)
                    current_index += 1
                if char == '[':
                    self.add_token(line_no, TT_LSQBRACK)
                    current_index += 1
                if char == ']':
                    self.add_token(line_no, TT_RSQBRACK)
                    current_index += 1
                if char == '{':
                    self.add_token(line_no, TT_LCURBRACK)
                    current_index += 1
                if char == '}':
                    self.add_token(line_no, TT_RCURBRACK)
                    current_index += 1
                if char == '#':
                    self.add_token(line_no, TT_SHARP)
                    current_index += 1
                if char == '&':
                    self.add_token(line_no, TT_AMPERSAND)
                    current_index += 1
                if char == '\'':
                    self.add_token(line_no, TT_SGLQUOTE)
                    current_index += 1
                if char == '"':
                    self.add_token(line_no, TT_DBLQUOTE)
                    current_index += 1
                if char == ',':
                    self.add_token(line_no, TT_COMMA)
                    current_index += 1
                if char == ':':
                    self.add_token(line_no, TT_COLON)
                    current_index += 1
                if char == '.':
                    self.add_token(line_no, TT_DOT)
                    current_index += 1
                continue

            # OPERATORS
            elif char in OPERATORS:
                if char == '+':
                    self.add_token(line_no, TT_PLUS)
                    current_index += 1
                if char == '-':
                    self.add_token(line_no, TT_MINUS)
                    current_index += 1
                if char == '*':
                    self.add_token(line_no, TT_MULT)
                    current_index += 1
                if char == '/':
                    self.add_token(line_no, TT_DIV)
                    current_index += 1
                if char == '%':
                    self.add_token(line_no, TT_MOD)
                    current_index += 1
                if char == '<':
                    value = ''
                    while re.match(r"[<>=]", char):
                        value += char
                        current_index += 1
                        if current_index < len(input_expression):
                            char = input_expression[current_index]
                        else:
                            break
                    if value == '<>':
                        self.add_token(line_no, OPERATORS[value], '<>')
                    elif value == '<=':
                        self.add_token(line_no, OPERATORS[value], '<=')
                    else:
                        self.add_token(line_no, OPERATORS[value], '<')
                if char == '>':
                    value = ''
                    while re.match(r"[>=]", char):
                        value += char
                        current_index += 1

                        if current_index < len(input_expression):
                            char = input_expression[current_index]
                        else:
                            break
                    if value == '>=':
                        self.add_token(line_no, OPERATORS[value], '>=')
                    else:
                        self.add_token(line_no, OPERATORS[value], '>')
                if char == '=':
                    value = ''
                    while re.match(r"=", char):
                        value += char
                        current_index += 1
                        if current_index < len(input_expression):
                            char = input_expression[current_index]
                        else:
                            break
                    if value == '==':
                        self.add_token(line_no, OPERATORS[value], '==')
                    else:
                        self.add_token(line_no, OPERATORS[value], '=')
                continue
            else:
                return [], IllegalCharError(line_no, f'\'{char}\'').to_string()
        return self.tokens, None

    def symbol_table(self):
        print('-' * 58)
        print("Symbol Table".center(53))
        print('-' * 58)
        print("Line Number".ljust(20), "Lexemes".ljust(20), "Tokens".ljust(20))
        print('-' * 58)
        for token in self.tokens:
            if not token.get('value'):
                print("{}".format(token["line"]).ljust(20), "".ljust(20),
                      "{}".format(token["type"]).ljust(20))
                continue
            print("{}".format(token["line"]).ljust(20), "{}".format(token["value"]).ljust(20),
              "{}".format(token["type"]).ljust(20))
        print('-' * 58)
        print("Total Number of Tokens: {}".format(len(self.tokens)))