"""
Chapter 6: Intermediate Code Generation - Three-Address Code

This module demonstrates generating three-address code (TAC) from an AST.
Three-address code is a common intermediate representation used in compilers.

Features:
- Generates quadruples (op, arg1, arg2, result)
- Handles expressions, assignments, control flow
- Manages temporary variables and labels
- Supports if statements and while loops
"""


# AST Node classes
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Number:
    def __init__(self, value):
        self.value = value


class Identifier:
    def __init__(self, name):
        self.name = name


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class IfStatement:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class Quadruple:
    """Three-address code instruction"""

    def __init__(self, op, arg1, arg2, result):
        self.op = op        # 操作符
        self.arg1 = arg1    # 第一个操作数
        self.arg2 = arg2    # 第二个操作数
        self.result = result  # 结果

    def __str__(self):
        if self.arg2:
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"
        elif self.arg1:
            return f"{self.result} = {self.op} {self.arg1}"
        else:
            return f"{self.op} {self.result}"


class IntermediateCodeGenerator:
    """Generate three-address code from AST"""

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        """Generate a new temporary variable"""
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def new_label(self):
        """Generate a new label"""
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    def emit(self, op, arg1=None, arg2=None, result=None):
        """Emit a three-address code instruction"""
        quad = Quadruple(op, arg1, arg2, result)
        self.code.append(quad)
        return result

    def generate(self, node):
        """Generate code for an AST node"""
        method_name = f'gen_{type(node).__name__}'
        generator = getattr(self, method_name, self.generic_generate)
        return generator(node)

    def gen_Number(self, node):
        """Generate code for number literal"""
        return str(node.value)

    def gen_Identifier(self, node):
        """Generate code for identifier"""
        return node.name

    def gen_BinOp(self, node):
        """Generate code for binary operation"""
        left = self.generate(node.left)
        right = self.generate(node.right)
        temp = self.new_temp()
        self.emit(node.op, left, right, temp)
        return temp

    def gen_Assignment(self, node):
        """Generate code for assignment"""
        value = self.generate(node.value)
        self.emit('=', value, None, node.name)
        return node.name

    def gen_IfStatement(self, node):
        """Generate code for if statement"""
        # Evaluate condition
        condition = self.generate(node.condition)

        # Create labels
        else_label = self.new_label()
        end_label = self.new_label()

        # If condition is false, jump to else
        self.emit('ifFalse', condition, None, else_label)

        # Then branch
        for stmt in node.then_branch:
            self.generate(stmt)

        # Jump to end
        self.emit('goto', None, None, end_label)

        # Else label
        self.emit('label', None, None, else_label)

        # Else branch (if exists)
        if node.else_branch:
            for stmt in node.else_branch:
                self.generate(stmt)

        # End label
        self.emit('label', None, None, end_label)

    def gen_WhileStatement(self, node):
        """Generate code for while loop"""
        # Create labels
        start_label = self.new_label()
        end_label = self.new_label()

        # Start label
        self.emit('label', None, None, start_label)

        # Evaluate condition
        condition = self.generate(node.condition)

        # If condition is false, exit loop
        self.emit('ifFalse', condition, None, end_label)

        # Loop body
        for stmt in node.body:
            self.generate(stmt)

        # Jump back to start
        self.emit('goto', None, None, start_label)

        # End label
        self.emit('label', None, None, end_label)

    def generic_generate(self, node):
        """Default generate method"""
        raise Exception(f"No generate method for {type(node).__name__}")

    def print_code(self):
        """Print generated three-address code"""
        for i, quad in enumerate(self.code):
            print(f"{i:3d}: {quad}")


# Example usage
if __name__ == "__main__":
    generator = IntermediateCodeGenerator()

    # Test 1: Simple expression
    print("=== Test 1: Expression (a + b * 2) ===")
    expr = BinOp(
        Identifier('a'),
        '+',
        BinOp(Identifier('b'), '*', Number(2))
    )
    generator.generate(expr)
    generator.print_code()
    print()

    # Test 2: Assignment
    print("=== Test 2: Assignment (c = a + b) ===")
    generator2 = IntermediateCodeGenerator()
    assign = Assignment('c', BinOp(Identifier('a'), '+', Identifier('b')))
    generator2.generate(assign)
    generator2.print_code()
    print()

    # Test 3: If statement
    print("=== Test 3: If statement ===")
    generator3 = IntermediateCodeGenerator()
    if_stmt = IfStatement(
        BinOp(Identifier('x'), '>', Number(0)),
        [Assignment('y', Number(1))],
        [Assignment('y', Number(0))]
    )
    generator3.generate(if_stmt)
    generator3.print_code()
    print()

    # Test 4: While loop
    print("=== Test 4: While loop ===")
    generator4 = IntermediateCodeGenerator()
    while_stmt = WhileStatement(
        BinOp(Identifier('i'), '<', Number(10)),
        [Assignment('i', BinOp(Identifier('i'), '+', Number(1)))]
    )
    generator4.generate(while_stmt)
    generator4.print_code()
