"""
Chapter 5: Semantic Analysis - Type Checking and Symbol Table

This module demonstrates semantic analysis including:
- Symbol table management with scoping
- Type checking for expressions and statements
- Function declaration and call validation
- Control flow statement validation

Features:
- Hierarchical symbol tables for nested scopes
- Type inference and checking
- Error collection and reporting
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SymbolTable:
    """Symbol table with scope management"""

    def __init__(self, parent: Optional['SymbolTable'] = None) -> None:
        self.symbols: Dict[str, Dict[str, Any]] = {}
        self.parent: Optional['SymbolTable'] = parent

    def define(self, name: str, symbol_type: str, value: Any = None) -> None:
        """Define a symbol in current scope"""
        if name in self.symbols:
            raise Exception(
                f"Symbol '{name}' already defined in current scope")
        self.symbols[name] = {'type': symbol_type, 'value': value}

    def lookup(self, name: str) -> Dict[str, Any]:
        """Look up a symbol in current and parent scopes"""
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            raise Exception(f"Undefined symbol: {name}")

    def enter_scope(self) -> 'SymbolTable':
        """Enter a new scope"""
        return SymbolTable(parent=self)

    def exit_scope(self) -> 'SymbolTable':
        """Exit current scope. Never returns None; if at root, return self."""
        return self.parent if self.parent is not None else self


# AST Node classes (simplified)
class BinOp:
    def __init__(self, left: Any, op: str, right: Any) -> None:
        self.left = left
        self.op = op
        self.right = right


class Number:
    def __init__(self, value: Any) -> None:
        self.value = value


class Identifier:
    def __init__(self, name: str) -> None:
        self.name = name


class Assignment:
    def __init__(self, name: str, value: Any) -> None:
        self.name = name
        self.value = value


class FunctionCall:
    def __init__(self, name: str, args: List[Any]) -> None:
        self.name = name
        self.args = args


class FunctionDeclaration:
    def __init__(self, name: str, params: List[Dict[str, Any]], return_type: str, body: List[Any]) -> None:
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body


class IfStatement:
    def __init__(self, condition: Any, then_branch: Any, else_branch: Any = None) -> None:
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class WhileStatement:
    def __init__(self, condition: Any, body: Any) -> None:
        self.condition = condition
        self.body = body


class ReturnStatement:
    def __init__(self, expression: Any = None) -> None:
        self.expression = expression


class SemanticAnalyzer:
    """Semantic analyzer with type checking"""

    def __init__(self) -> None:
        self.symbol_table: SymbolTable = SymbolTable()
        self.errors: List[str] = []
        self.current_function_return_type: Optional[str] = None

    def visit(self, node: Any) -> Any:
        """Visitor pattern dispatcher"""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def visit_Number(self, node: Number) -> str:
        """Number literal"""
        # Access node.value to avoid 'node not accessed' and infer type
        value = node.value
        if isinstance(value, float):
            return 'float'
        return 'int'

    def visit_Identifier(self, node: Identifier) -> str:
        """Variable reference"""
        symbol = self.symbol_table.lookup(node.name)
        return symbol['type']

    def visit_BinOp(self, node: BinOp) -> str:
        """Binary operation"""
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)

        # Type checking for binary operations
        if node.op in ['+', '-', '*', '/']:
            if left_type == 'int' and right_type == 'int':
                return 'int'
            elif left_type in ['int', 'float'] and right_type in ['int', 'float']:
                return 'float'
            else:
                self.errors.append(
                    f"Type mismatch in {node.op}: {left_type} and {right_type}"
                )
                return 'error'

        elif node.op in ['<', '>', '==', '!=', '<=', '>=']:
            if left_type == right_type:
                return 'bool'
            else:
                self.errors.append(
                    f"Type mismatch in comparison: {left_type} and {right_type}"
                )
                return 'error'

        return 'error'

    def visit_Assignment(self, node: Assignment) -> str:
        """Assignment statement"""
        value_type = self.visit(node.value)

        try:
            symbol = self.symbol_table.lookup(node.name)
            if symbol['type'] != value_type:
                self.errors.append(
                    f"Type mismatch in assignment: cannot assign {value_type} to {symbol['type']}"
                )
        except Exception:
            # Variable not defined, define it
            self.symbol_table.define(node.name, value_type)

        return value_type

    def visit_FunctionCall(self, node: FunctionCall) -> str:
        """Function call"""
        func_symbol = self.symbol_table.lookup(node.name)

        if func_symbol['type'] != 'function':
            self.errors.append(f"{node.name} is not a function")
            return 'error'

        # Function metadata is stored under 'value'
        func_info = func_symbol.get('value', {}) or {}
        expected_params = func_info.get('params', [])

        # Check argument count
        if len(node.args) != len(expected_params):
            self.errors.append(
                f"Function {node.name} expects {len(expected_params)} arguments, got {len(node.args)}"
            )

        # Check argument types
        for i, arg in enumerate(node.args):
            arg_type = self.visit(arg)
            if i < len(expected_params):
                expected_type = expected_params[i]['type']
                if arg_type != expected_type:
                    self.errors.append(
                        f"Argument {i+1} type mismatch: expected {expected_type}, got {arg_type}"
                    )

        return func_info.get('return_type', 'void')

    def visit_FunctionDeclaration(self, node: FunctionDeclaration) -> None:
        """Function declaration"""
        # Define function in symbol table
        self.symbol_table.define(
            node.name,
            'function',
            {
                'params': node.params,
                'return_type': node.return_type
            }
        )

        # Enter function scope
        self.symbol_table = self.symbol_table.enter_scope()
        self.current_function_return_type = node.return_type

        # Define parameters
        for param in node.params:
            self.symbol_table.define(param['name'], param['type'])

        # Analyze function body
        for stmt in node.body:
            self.visit(stmt)

        # Exit function scope
        self.symbol_table = self.symbol_table.exit_scope()

    def visit_ReturnStatement(self, node: ReturnStatement) -> str:
        """Return statement"""
        if node.expression is not None:
            return self.visit(node.expression)
        return 'void'

    def visit_IfStatement(self, node: IfStatement) -> None:
        """If statement"""
        condition_type = self.visit(node.condition)
        if condition_type != 'bool':
            self.errors.append(
                f"If condition must be bool, got {condition_type}"
            )

        self.visit(node.then_branch)
        if node.else_branch:
            self.visit(node.else_branch)

    def visit_WhileStatement(self, node: WhileStatement) -> None:
        """While statement"""
        condition_type = self.visit(node.condition)
        if condition_type != 'bool':
            self.errors.append(
                f"While condition must be bool, got {condition_type}"
            )

        self.visit(node.body)

    def generic_visit(self, node: Any) -> None:
        """Default visit method"""
        raise Exception(f"No visit method for {type(node).__name__}")


# Example usage
if __name__ == "__main__":
    analyzer = SemanticAnalyzer()

    # Test: Type checking for binary operations
    expr1 = BinOp(Number(5), '+', Number(3))
    result_type = analyzer.visit(expr1)
    print(f"Expression: 5 + 3, Type: {result_type}")

    # Test: Assignment
    assign1 = Assignment('x', Number(10))
    analyzer.visit(assign1)
    print(f"Defined variable 'x' with type: int")

    # Test: Variable lookup
    var_ref = Identifier('x')
    var_type = analyzer.visit(var_ref)
    print(f"Variable 'x' has type: {var_type}")

    # Print any errors
    if analyzer.errors:
        print("\nErrors found:")
        for error in analyzer.errors:
            print(f"  - {error}")
    else:
        print("\nNo semantic errors found!")
