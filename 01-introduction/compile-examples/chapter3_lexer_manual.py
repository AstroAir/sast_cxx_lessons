"""
Chapter 3: Lexical Analysis - Manual Lexer Implementation

This module demonstrates a hand-coded lexer that tokenizes source code
by manually implementing state transitions and character recognition.

Features:
- Recognizes numbers, identifiers, keywords, and operators
- Skips whitespace
- Handles basic error reporting for unknown characters
"""


def lexer(input_string):
    """
    Tokenize input string into a list of tokens.

    Args:
        input_string: Source code string to tokenize

    Returns:
        List of tuples (token_type, token_value)
    """
    tokens = []
    i = 0

    while i < len(input_string):
        # 跳过空白字符
        if input_string[i].isspace():
            i += 1
            continue

        # 识别数字
        if input_string[i].isdigit():
            num = ''
            while i < len(input_string) and input_string[i].isdigit():
                num += input_string[i]
                i += 1
            tokens.append(('NUMBER', num))
            continue

        # 识别标识符和关键字
        if input_string[i].isalpha() or input_string[i] == '_':
            identifier = ''
            while i < len(input_string) and (input_string[i].isalnum() or input_string[i] == '_'):
                identifier += input_string[i]
                i += 1

            # 检查是否为关键字
            keywords = {'if', 'while', 'return', 'int', 'void'}
            if identifier in keywords:
                tokens.append(('KEYWORD', identifier))
            else:
                tokens.append(('IDENTIFIER', identifier))
            continue

        # 识别运算符和分隔符
        # 支持多字符运算符（优先匹配2字符），以及单字符运算符/分隔符
        two_char_ops = {'==', '!=', '<=', '>=', '&&', '||', '++', '--'}
        if i + 1 < len(input_string):
            two = input_string[i:i+2]
            if two in two_char_ops:
                tokens.append(('OPERATOR', two))
                i += 2
                continue

        single_char_ops = set('+-*/=(){}[];,.<>!&|')
        if input_string[i] in single_char_ops:
            tokens.append(('OPERATOR', input_string[i]))
            i += 1
            continue

        # 未知字符
        raise Exception(f"Unknown character: {input_string[i]}")

    return tokens


# Example usage
if __name__ == "__main__":
    # Test case 1: Simple expression
    code1 = "int x = 5 + 3"
    print("Input:", code1)
    print("Tokens:", lexer(code1))
    print()

    # Test case 2: Function definition
    code2 = "int main() { return 0; }"
    print("Input:", code2)
    print("Tokens:", lexer(code2))
    print()

    # Test case 3: While loop
    code3 = "while (x > 0) { x = x - 1; }"
    print("Input:", code3)
    print("Tokens:", lexer(code3))
