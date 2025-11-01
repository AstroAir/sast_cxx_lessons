"""
Chapter 4: Syntax Analysis - Recursive Descent Parser

This module demonstrates a hand-written recursive descent parser that
builds an Abstract Syntax Tree (AST) from a token stream.

Grammar:
    E → T (('+' | '-') T)*
    T → F (('*' | '/') F)*
    F → '(' E ')' | number | identifier

Features:
- Parses arithmetic expressions with proper precedence
- Builds AST nodes for binary operations, numbers, and identifiers
- Handles parenthesized expressions
"""


# AST Node classes
class BinOp:
    """Binary operation node"""

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"


class Number:
    """Number literal node"""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Identifier:
    """Identifier node"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier('{self.name}')"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type, expected_value=None):
        """消费一个 token"""
        token = self.current_token()
        if token and token[0] == expected_type and (expected_value is None or token[1] == expected_value):
            self.pos += 1
            return token
        exp = expected_type if expected_value is None else f"{expected_type}('{expected_value}')"
        raise Exception(f"Expected {exp}, got {token}")

    def parse_expression(self):
        """E → T (('+' | '-') T)*"""
        left = self.parse_term()

        while True:
            tok = self.current_token()
            if not tok or tok[0] != 'OPERATOR' or tok[1] not in ['+', '-']:
                break
            op = self.consume('OPERATOR')  # '+' or '-'
            right = self.parse_term()
            left = BinOp(left, op[1], right)

        return left

    def parse_term(self):
        """T → F (('*' | '/') F)*"""
        left = self.parse_factor()

        while True:
            tok = self.current_token()
            if not tok or tok[0] != 'OPERATOR' or tok[1] not in ['*', '/']:
                break
            op = self.consume('OPERATOR')  # '*' or '/'
            right = self.parse_factor()
            left = BinOp(left, op[1], right)

        return left

    def parse_factor(self):
        """F → '(' E ')' | number | identifier"""
        token = self.current_token()
        if token is None:
            raise Exception("Unexpected end of input while parsing factor")

        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return Number(int(token[1]))

        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return Identifier(token[1])

        elif token[0] == 'OPERATOR' and token[1] == '(':
            self.consume('OPERATOR', '(')
            expr = self.parse_expression()
            self.consume('OPERATOR', ')')
            return expr

        raise Exception(f"Unexpected token: {token}")


# Example usage
if __name__ == "__main__":
    # Test case 1: Simple addition
    tokens1 = [('NUMBER', '3'), ('OPERATOR', '+'), ('NUMBER', '4')]
    parser1 = Parser(tokens1)
    ast1 = parser1.parse_expression()
    print("Tokens:", tokens1)
    print("AST:", ast1)
    print()

    # Test case 2: Precedence (multiplication before addition)
    tokens2 = [
        ('NUMBER', '2'), ('OPERATOR', '+'),
        ('NUMBER', '3'), ('OPERATOR', '*'), ('NUMBER', '4')
    ]
    parser2 = Parser(tokens2)
    ast2 = parser2.parse_expression()
    print("Tokens:", tokens2)
    print("AST:", ast2)
    print()

    # Test case 3: Parentheses
    tokens3 = [
        ('OPERATOR', '('), ('NUMBER', '2'), ('OPERATOR', '+'), ('NUMBER', '3'),
        ('OPERATOR', ')'), ('OPERATOR', '*'), ('NUMBER', '4')
    ]
    parser3 = Parser(tokens3)
    ast3 = parser3.parse_expression()
    print("Tokens:", tokens3)
    print("AST:", ast3)
    print()

    # Test case 4: Identifiers
    tokens4 = [
        ('IDENTIFIER', 'x'), ('OPERATOR', '+'),
        ('IDENTIFIER', 'y'), ('OPERATOR', '*'), ('NUMBER', '2')
    ]
    parser4 = Parser(tokens4)
    ast4 = parser4.parse_expression()
    print("Tokens:", tokens4)
    print("AST:", ast4)
