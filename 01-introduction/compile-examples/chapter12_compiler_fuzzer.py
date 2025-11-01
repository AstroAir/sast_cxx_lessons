"""
Chapter 12: Compiler Testing - Fuzzer

This module demonstrates fuzzing (fuzz testing) for compilers.
Fuzzing generates random or semi-random inputs to find bugs,
crashes, or unexpected behavior.

Features:
- Random program generation
- Configurable complexity
- Crash detection and reporting
- Test case minimization hints
"""

import random
import string


class CompilerFuzzer:
    """
    Fuzzer for testing compiler robustness.

    Generates random programs to test compiler error handling,
    crash resistance, and correctness.
    """

    def __init__(self, compiler):
        """
        Initialize fuzzer.

        Args:
            compiler: Compiler object to test (must have compile() method)
        """
        self.compiler = compiler
        self.test_cases_generated = 0
        self.crashes_found = 0

    def generate_random_program(self, num_vars=None, num_exprs=None):
        """
        Generate a random valid program.

        Args:
            num_vars: Number of variables (random if None)
            num_exprs: Number of expressions (random if None)

        Returns:
            String containing generated program
        """
        self.test_cases_generated += 1

        program = "int main() {\n"

        # Random number of variables
        if num_vars is None:
            num_vars = random.randint(1, 5)

        var_names = []
        for i in range(num_vars):
            var_name = f"var{i}"
            var_names.append(var_name)
            initial_value = random.randint(0, 100)
            program += f"    int {var_name} = {initial_value};\n"

        # Random number of expressions
        if num_exprs is None:
            num_exprs = random.randint(1, 10)

        for i in range(num_exprs):
            if len(var_names) >= 2:
                var1 = random.choice(var_names)
                var2 = random.choice(var_names)
                op = random.choice(['+', '-', '*', '/'])
                result_var = f"result{i}"
                program += f"    int {result_var} = {var1} {op} {var2};\n"

        program += "    return 0;\n}\n"
        return program

    def generate_random_expression(self, depth=0, max_depth=3):
        """
        Generate a random arithmetic expression.

        Args:
            depth: Current recursion depth
            max_depth: Maximum recursion depth

        Returns:
            String containing expression
        """
        if depth >= max_depth:
            # Base case: return a number or variable
            if random.random() < 0.5:
                return str(random.randint(1, 100))
            else:
                return f"var{random.randint(0, 4)}"

        # Recursive case: binary operation
        left = self.generate_random_expression(depth + 1, max_depth)
        right = self.generate_random_expression(depth + 1, max_depth)
        op = random.choice(['+', '-', '*', '/'])

        return f"({left} {op} {right})"

    def generate_malformed_program(self):
        """
        Generate intentionally malformed program to test error handling.

        Returns:
            String containing malformed program
        """
        malformed_patterns = [
            # Missing semicolon
            "int main() { int x = 5 return x; }",
            # Mismatched braces
            "int main() { int x = 5; ",
            # Invalid operator
            "int main() { int x = 5 & 3; return x; }",
            # Undefined variable
            "int main() { int x = y + 5; return x; }",
            # Type mismatch
            "int main() { int x = 'hello'; return x; }",
            # Division by zero
            "int main() { int x = 5 / 0; return x; }",
        ]

        return random.choice(malformed_patterns)

    def fuzz(self, iterations=100, include_malformed=True):
        """
        Run fuzzing campaign.

        Args:
            iterations: Number of test cases to generate
            include_malformed: Whether to include malformed programs

        Returns:
            List of (program, error) tuples for crashes found
        """
        crashes = []

        for i in range(iterations):
            # Decide whether to generate valid or malformed program
            if include_malformed and random.random() < 0.2:
                program = self.generate_malformed_program()
            else:
                program = self.generate_random_program()

            try:
                # Try to compile
                self.compiler.compile(program)
            except Exception as e:
                # Check if this is an expected error or a crash
                error_msg = str(e)
                if self._is_crash(error_msg):
                    crashes.append((program, error_msg))
                    self.crashes_found += 1
                    print(
                        f"[CRASH] Found crash in iteration {i}: {error_msg[:50]}...")

        return crashes

    def _is_crash(self, error_msg):
        """
        Determine if error is a crash vs expected error.

        Args:
            error_msg: Error message string

        Returns:
            True if this appears to be a crash
        """
        # Crashes typically have these indicators
        crash_indicators = [
            'AssertionError',
            'SegmentationFault',
            'NullPointerException',
            'StackOverflow',
            'InternalError',
        ]

        return any(indicator in error_msg for indicator in crash_indicators)

    def print_statistics(self):
        """Print fuzzing statistics"""
        print("\n=== Fuzzing Statistics ===")
        print(f"Test cases generated: {self.test_cases_generated}")
        print(f"Crashes found: {self.crashes_found}")
        if self.test_cases_generated > 0:
            crash_rate = (self.crashes_found / self.test_cases_generated) * 100
            print(f"Crash rate: {crash_rate:.2f}%")


class DummyCompiler:
    """Dummy compiler for demonstration"""

    def compile(self, source):
        """
        Simulate compilation.

        Raises exceptions for some patterns to demonstrate fuzzer.
        """
        # Simulate some error conditions
        if 'undefined' in source.lower():
            raise Exception("Undefined variable")
        if '/ 0' in source:
            raise Exception("Division by zero")
        if source.count('{') != source.count('}'):
            raise Exception("Mismatched braces")

        # Simulate rare crash
        if random.random() < 0.01:
            raise AssertionError("Internal compiler error")

        return "compiled_code"


# Example usage
if __name__ == "__main__":
    print("=== Compiler Fuzzer Demo ===\n")

    # Create dummy compiler and fuzzer
    compiler = DummyCompiler()
    fuzzer = CompilerFuzzer(compiler)

    # Generate some example programs
    print("Example generated programs:\n")
    for i in range(3):
        program = fuzzer.generate_random_program(num_vars=3, num_exprs=5)
        print(f"Program {i+1}:")
        print(program)
        print()

    # Run fuzzing campaign
    print("="*50)
    print("\nRunning fuzzing campaign (1000 iterations)...")
    crashes = fuzzer.fuzz(iterations=1000, include_malformed=True)

    # Print statistics
    fuzzer.print_statistics()

    # Show some crashes
    if crashes:
        print(f"\n=== Sample Crashes (showing first 3) ===")
        for i, (program, error) in enumerate(crashes[:3]):
            print(f"\nCrash {i+1}:")
            print(f"Error: {error}")
            print(f"Program:\n{program}")
    else:
        print("\nNo crashes found!")

    # Demonstrate expression generation
    print("\n" + "="*50)
    print("\nExample random expressions:")
    for i in range(5):
        expr = fuzzer.generate_random_expression(max_depth=3)
        print(f"  {expr}")
