from syntax_analyzer.nodes import *
from tokenizer.structure import *
from error.error import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.length = len(tokens)
        self.current_token = None
        self.current_index = -1
        self.next()

    def next(self):
        self.current_index += 1
        if self.current_index != self.length:
            self.current_token = self.tokens[self.current_index]

        return self.current_token

    def parse(self):
        while(self.current_index < self.length):
            # COMMENT
            if self.current_token.get('type') == TT_MULT:
                current_line = self.current_token.get('line')
                while self.current_token.get('line') < current_line + 1:
                    self.next()
                continue
            # VAR KEYWORD
            elif self.current_token.get('type') == 'VAR':
                current_line = self.current_token.get('line')
                while self.current_token.get('line') < current_line +1:
                    if self.tokens[self.current_index + 1].get('type') == 'STRING':
                        self.next()
                        # Comma
                        if self.tokens[self.current_index + 1].get('type') == TT_COMMA:
                            self.next()
                        else:
                            if self.tokens[self.current_index + 1].get('type') == 'AS':
                                self.next()
                                if self.tokens[self.current_index + 1].get('value') == TT_INT:
                                    self.next()
                                    self.next()
                                else:
                                    return None, InvalidSyntaxError(self.current_token.get('line'),
                                                                    self.current_token.get('type')).to_string()
                            else:
                                return None, InvalidSyntaxError(self.current_token.get('line'),
                                                                self.current_token.get('value')).to_string()
                    else:
                        return None, InvalidSyntaxError(self.current_token.get('line'),
                                                        self.current_token.get('type')).to_string()

            elif self.current_token.get('type') == 'START':
                while self.current_token.get('type') != 'STOP':
                    if self.current_index != self.length-1:
                        self.next()
                    else: break
                if self.current_token.get('type') == 'STOP':
                    return None, None
                else:
                    return None, InvalidSyntaxError(self.current_token.get('line'),
                                                    'Expected: \'STOP\'').to_string()
            else:
                return None, InvalidSyntaxError(self.current_token.get('line'), self.current_token.get('value')).to_string()



