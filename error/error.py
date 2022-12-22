class Error:
    def __init__(self, error_name, line_no, details):
        self.error_name = error_name
        self.line_no = line_no
        self.details = details

    def to_string(self):
        return f'{self.error_name}: near line {self.line_no}' \
               f'\n--> {self.details}'

class IllegalCharError(Error):
    def __init__(self, line_no, details):
        super().__init__('Illegal Character', line_no, details)


class InvalidSyntaxError(Error):
    def __init__(self, line_no, details=''):
        super().__init__('Invalid Syntax', line_no, details)