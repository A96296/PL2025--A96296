import ply.lex as lex

# Palavras reservadas
reserved = {
    'select': 'SELECT',
    'where': 'WHERE',
    'LIMIT': 'LIMIT'
}

# Lista de tokens
tokens = [
    'VAR',
    'PREFIX',
    'LITERAL',
    'IDENTIFIER',
    'DOT',
    'LBRACE', 'RBRACE',
    'NUMBER',
    'COMMENT'
] + list(reserved.values())

# Definições de tokens simples
t_DOT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Variável
t_VAR = r'\?[a-zA-Z_]\w*'

# Número (LIMIT 100)
t_NUMBER = r'\d+'

# Comentários (ignorar)
def t_COMMENT(t):
    r'\#.*'
    pass

# Literais (ex: "Chuck Berry"@en)
def t_LITERAL(t):
    r'"[^"]*"(@[a-zA-Z]+)?'
    return t

# Prefixo como "dbo:", "foaf:"
def t_PREFIX(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:'
    return t

# Identificadores (MusicalArtist, name, abstract)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Ignorar espaços e quebras de linha
t_ignore = ' \t\n'

# Tratamento de erro
def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

# Criar lexer
lexer = lex.lex()

# Query de teste
query = """
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 100
"""

# Rodar lexer
lexer.input(query)

# Mostrar tokens
for tok in lexer:
    print(f'{tok.type}: {tok.value}')
