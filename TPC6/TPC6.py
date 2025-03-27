import re

class Parser:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|[()+\-*/]', expression)
        self.current_token_index = 0

    def current_token(self):
        return self.tokens[self.current_token_index] if self.current_token_index < len(self.tokens) else None

    def eat(self, expected_token):
        if self.current_token() == expected_token:
            self.current_token_index += 1
        else:
            raise SyntaxError(f'Esperado {expected_token}, mas encontrado {self.current_token()}')
    
    def factor(self):
        token = self.current_token()
        if token.isdigit():
            self.eat(token)
            return int(token)
        elif token == '(':
            self.eat('(')
            result = self.expr()
            self.eat(')')
            return result
        else:
            raise SyntaxError(f'Token inesperado: {token}')
    
    def term(self):
        result = self.factor()
        while self.current_token() in ('*', '/'):
            token = self.current_token()
            self.eat(token)
            if token == '*':
                result *= self.factor()
            elif token == '/':
                result /= self.factor()
        return result
    
    def expr(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            token = self.current_token()
            self.eat(token)
            if token == '+':
                result += self.term()
            elif token == '-':
                result -= self.term()
        return result
    
    def parse(self):
        return self.expr()

# Testes
expressions = [
    "2+3",
    "67-(2+3*4)",
    "(9-2)*(13-4)"
]

for expr in expressions:
    parser = Parser(expr)
    result = parser.parse()
    print(f"{expr} = {result}")
