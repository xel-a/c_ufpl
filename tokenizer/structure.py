# keywords according to the documentation

# CONSTANTS
TT_INT          = 'INT'
TT_FLOAT        = 'FLOAT'
TT_STRING       = 'STRING'
TT_CHAR         = 'CHAR'
TT_BOOL         = 'BOOL'
TT_PLUS         = 'PLUS'
TT_MINUS        = 'MINUS'
TT_MULT         = 'MULT'
TT_DIV          = 'DIVIDE'
TT_MOD          = 'MODULO'
TT_LPAREN       = 'LPAREN'
TT_RPAREN       = 'RPAREN'
TT_LSQBRACK     = 'LSQBRACK'
TT_RSQBRACK     = 'RSQBRACK'
TT_LCURBRACK    = 'LCURBRACK'
TT_RCURBRACK    = 'RCURBRACK'
TT_COMMENT      = 'COMMENT'
TT_SHARP        = 'SHARP'
TT_AMPERSAND    = 'AMPERSAND'
TT_SGLQUOTE     = 'SGLQUOTE'
TT_DBLQUOTE     = 'DBLQUOTE'
TT_COMMA        = 'COMMA'
TT_COLON        = 'COLON'
TT_DOT          = 'DOT'


# KEYWORDS
KEYWORDS = {
    'KEY_START'   : 'START',
    'KEY_STOP'    : 'STOP',
    'KEY_VAR'     : 'VAR',
    'KEY_AS'      : 'AS',
    'KEY_INPUT'   : 'INPUT',
    'KEY_OUTPUT'  : 'OUTPUT',
    'KEY_TRUE'    :'TRUE',
    'KEY_FALSE'   :'FALSE'
}

# separators according to the documentation
SEPARATORS = [
    '#',
    '&',
    '[',
    ']',
    '(',
    ')',
    '{',
    '}',
    '\'',
    '"',
    ",",
    ':',
    '.'
    ]

# operators according to the documentation
OPERATORS = {
    '*': "MULT",
    '/': "DIV",
    '%': "MOD",
    '+': "ADD",
    '-': "SUBT",
    '>': "GT",
    '<': "LT",
    '=': "EQ",
    '==': "DBL_EQ",
    '<>': "NT_EQ",
    '<=': "LT_EQ",
    '>=': "GT_EQ",
    'AND': "AND",
    'OR': "OR",
    'NOT': "NOT"
    }
