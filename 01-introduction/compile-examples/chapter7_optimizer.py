"""
Chapter 7: Code Optimization - Constant Folding and Dead Code Elimination

This module demonstrates common compiler optimizations:
- Constant folding: Evaluate constant expressions at compile time
- Constant propagation: Replace variables with known constant values
- Dead code elimination: Remove unused code

Features:
- AST-based optimizations
- Multiple optimization passes
- Demonstrates optimization effectiveness
"""


# AST Node classes
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"


class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Identifier:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier('{self.name}')"


def constant_folding(node):
    """
    Constant folding optimization.

    Evaluates constant expressions at compile time.
    Example: 2 + 3 * 4 → 14
    """
    if isinstance(node, BinOp):
        left = constant_folding(node.left)
        right = constant_folding(node.right)

        # If both operands are constants, compute the result
        if isinstance(left, Number) and isinstance(right, Number):
            if node.op == '+':
                return Number(left.value + right.value)
            elif node.op == '-':
                return Number(left.value - right.value)
            elif node.op == '*':
                return Number(left.value * right.value)
            elif node.op == '/':
                if right.value != 0:
                    return Number(left.value / right.value)

        node.left = left
        node.right = right

    return node


class ConstantPropagator:
    """
    Constant propagation optimization.

    Replaces variables with their known constant values.
    Example: x = 5; y = x + 3 → x = 5; y = 8
    """

    def __init__(self):
        self.constants = {}  # Maps variable names to constant values

    def propagate(self, node):
        """Propagate constants through the AST"""
        if isinstance(node, Number):
            return node

        elif isinstance(node, Identifier):
            # Replace identifier with constant if known
            if node.name in self.constants:
                return Number(self.constants[node.name])
            return node

        elif isinstance(node, BinOp):
            node.left = self.propagate(node.left)
            node.right = self.propagate(node.right)

            # Try constant folding after propagation
            return constant_folding(node)

        return node


class DeadCodeEliminator:
    """
    Dead code elimination.

    Removes code that doesn't affect program output.
    """

    def __init__(self):
        self.live_variables = set()

    def mark_live(self, node):
        """Mark variables that are used"""
        if isinstance(node, Identifier):
            self.live_variables.add(node.name)
        elif isinstance(node, BinOp):
            self.mark_live(node.left)
            self.mark_live(node.right)

    def is_dead(self, assignment_target):
        """Check if an assignment is dead (result never used)"""
        return assignment_target not in self.live_variables


# Optimization pipeline
class Optimizer:
    """
    Complete optimization pipeline.

    Applies multiple optimization passes in sequence.
    """

    def __init__(self):
        self.passes = 0

    def optimize(self, ast):
        """Apply all optimizations"""
        print(f"Original AST: {ast}")

        # Pass 1: Constant folding
        ast = constant_folding(ast)
        print(f"After constant folding: {ast}")

        # Pass 2: Constant propagation
        propagator = ConstantPropagator()
        propagator.constants = {'x': 5, 'y': 10}  # Example known constants
        ast = propagator.propagate(ast)
        print(f"After constant propagation: {ast}")

        return ast


# Example usage
if __name__ == "__main__":
    print("=== Optimization Examples ===\n")

    # Example 1: Constant folding
    print("Example 1: Constant Folding")
    print("Expression: 2 + 3 * 4")
    expr1 = BinOp(
        Number(2),
        '+',
        BinOp(Number(3), '*', Number(4))
    )
    optimized1 = constant_folding(expr1)
    print(f"Optimized: {optimized1}")
    print()

    # Example 2: Nested constant folding
    print("Example 2: Nested Constant Folding")
    print("Expression: (10 + 20) * (5 - 3)")
    expr2 = BinOp(
        BinOp(Number(10), '+', Number(20)),
        '*',
        BinOp(Number(5), '-', Number(3))
    )
    optimized2 = constant_folding(expr2)
    print(f"Optimized: {optimized2}")
    print()

    # Example 3: Constant propagation
    print("Example 3: Constant Propagation")
    print("Expression: x + y (where x=5, y=10)")
    expr3 = BinOp(Identifier('x'), '+', Identifier('y'))
    propagator = ConstantPropagator()
    propagator.constants = {'x': 5, 'y': 10}
    optimized3 = propagator.propagate(expr3)
    print(f"Optimized: {optimized3}")
    print()

    # Example 4: Combined optimizations
    print("Example 4: Combined Optimizations")
    print("Expression: x + 3 * 4 (where x=5)")
    expr4 = BinOp(
        Identifier('x'),
        '+',
        BinOp(Number(3), '*', Number(4))
    )
    optimizer = Optimizer()
    optimized4 = optimizer.optimize(expr4)
    print()

    # Example 5: Algebraic simplification potential
    print("Example 5: Strength Reduction Concept")
    print("Expression: x * 2 could be optimized to x << 1 (left shift)")
    print("Expression: x / 4 could be optimized to x >> 2 (right shift)")
    print("(These optimizations would be implemented in a real compiler)")
