"""
Chapter 3: Lexical Analysis - Regex-based Lexer

This module demonstrates a lexer implementation using regular expressions
to define token patterns. This approach is more declarative and easier to
maintain than manual state machines.

Features:
- Uses Python's re module for pattern matching
- Supports numbers, identifiers, operators, and whitespace
- Automatically filters out whitespace tokens
"""

import re


class RegexLexer:
    def __init__(self):
        # 定义 Token 模式
        self.token_patterns = [
            ('NUMBER',    r'\d+(\.\d*)?'),           # 整数或浮点数
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # 标识符
            ('PLUS',      r'\+'),                     # 加号
            ('MINUS',     r'-'),                      # 减号
            ('TIMES',     r'\*'),                     # 乘号
            ('DIVIDE',    r'/'),                      # 除号
            ('LPAREN',    r'\('),                     # 左括号
            ('RPAREN',    r'\)'),                     # 右括号
            ('WHITESPACE', r'\s+'),                   # 空白字符
        ]

        # 编译正则表达式
        self.regex = '|'.join(
            f'(?P<{name}>{pattern})' for name, pattern in self.token_patterns)
        self.pattern = re.compile(self.regex)

    def tokenize(self, code):
        """
        Tokenize input code using regex patterns.

        Args:
            code: Source code string to tokenize

        Returns:
            List of tuples (token_type, token_value)
        """
        tokens = []
        for match in self.pattern.finditer(code):
            token_type = match.lastgroup
            token_value = match.group()

            # 跳过空白字符
            if token_type == 'WHITESPACE':
                continue

            tokens.append((token_type, token_value))

        return tokens


# Example usage
if __name__ == "__main__":
    lexer = RegexLexer()

    # Test case 1: Simple arithmetic
    code1 = "3 + 4 * 5"
    print("Input:", code1)
    print("Tokens:", lexer.tokenize(code1))
    print()

    # Test case 2: Expression with parentheses
    code2 = "(10 + 20) * 3"
    print("Input:", code2)
    print("Tokens:", lexer.tokenize(code2))
    print()

    # Test case 3: Floating point numbers
    code3 = "3.14 + 2.71"
    print("Input:", code3)
    print("Tokens:", lexer.tokenize(code3))
    print()

    # Test case 4: Identifiers
    code4 = "x + y_value"
    print("Input:", code4)
    print("Tokens:", lexer.tokenize(code4))
