import ply.lex as lex
import ply.yacc as yacc
import re

# -------------------
# Lexer
# -------------------
tokens = (
    'CONCEPT', 'ATTRIBUTE', 'ALIAS', 'EXAMPLE', 'CODE', 'MAP',
    'NEWLINE', 'DEFAULT',
)

# Token regex
t_CONCEPT = r'[^a-z\s][^\n(]*'
t_ATTRIBUTE = r'[a-z][^(:\n]*'
t_ignore = ' \t'

def t_ALIAS(t):
    r'\([^)]+\)'
    t.value = t.value[1:-1].strip()  # Remove the ( and ) and strip whitespace
    return t

def t_CODE(t):
    r'```[\s\S]*?```'
    t.value = t.value[3:-3].strip()  # Remove the triple backticks and strip whitespace
    return t

def t_DEFAULT(t):
    r':[^\n]*'
    t.value = t.value[1:].strip()  # Remove the colon and strip whitespace
    return t

def t_MAP(t):
    r'\.\.\.[^\n]*'
    t.value = t.value[3:].strip()  # Remove the ... and strip whitespace
    return t

def t_EXAMPLE(t):
    r'-[^\n]*'
    t.value = t.value[1:].strip()  # Remove the dash and strip whitespace
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# -------------------
# Parser
# -------------------

def p_document(p):
    'document : elements'
    p[0] = ('document', p[1])

def p_elements(p):
    '''elements : element elements
                | element
                | NEWLINE elements
                | NEWLINE'''
    if len(p) == 3:
        if p[1] == '\n':
            p[0] = p[2]
        else:
            p[0] = [p[1]] + p[2]
    elif len(p) == 2:
        if p[1] == '\n':
            p[0] = []
        else:
            p[0] = [p[1]]

def p_element(p):
    '''element : concept_line
               | attribute_line
               | example_line
               | map_line
               | code_line'''
    p[0] = p[1]

def p_concept_line(p):
    'concept_line : CONCEPT opt_alias opt_newline'
    p[0] = ('concept', p[1], p[2])

def p_attribute_line(p):
    '''attribute_line : ATTRIBUTE opt_alias DEFAULT opt_newline
                     | ATTRIBUTE opt_alias opt_newline'''
    if len(p) == 5:
        p[0] = ('attribute', p[1], p[2], p[3])
    else:
        p[0] = ('attribute', p[1], p[2], None)

def p_example_line(p):
    '''example_line : EXAMPLE opt_newline'''
    p[0] = ('example', p[1])

def p_map_line(p):
    '''map_line : MAP opt_newline'''
    p[0] = ('map', p[1])

def p_code_line(p):
    '''code_line : CODE opt_newline'''
    p[0] = ('code', p[1])

def p_opt_alias(p):
    '''opt_alias : ALIAS
                | empty'''
    p[0] = p[1] if len(p) > 1 else None

def p_opt_newline(p):
    '''opt_newline : NEWLINE
                  | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (type {p.type}) line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# -------------
# Example usage
# -------------
if __name__ == "__main__":
    with open("example.aot") as f:
        data = f.read()
    with open("alphabet of thought.aot") as f:
        data = f.read()
    result = parser.parse(data)
    print(result)
