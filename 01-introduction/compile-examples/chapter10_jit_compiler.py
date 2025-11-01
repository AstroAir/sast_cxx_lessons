"""
Chapter 10: Modern Compilation - JIT Compiler

This module demonstrates a simple Just-In-Time (JIT) compiler that:
- Starts by interpreting code
- Tracks execution frequency
- Compiles hot code paths after threshold is reached
- Caches compiled code for reuse

Features:
- Execution counting
- Hot code detection
- Mixed interpretation/compilation mode
- Performance optimization through selective compilation
"""

import time


class JITCompiler:
    """
    Simple JIT compiler with hot code detection.

    Strategy:
    1. Initially interpret all functions
    2. Count executions
    3. When execution count exceeds threshold, compile
    4. Use compiled version for subsequent calls
    """

    def __init__(self, jit_threshold=10):
        """
        Initialize JIT compiler.

        Args:
            jit_threshold: Number of executions before compiling
        """
        self.code_cache = {}  # Compiled code cache
        self.execution_count = {}  # Execution counters
        self.JIT_THRESHOLD = jit_threshold
        self.compilation_time = 0  # Track compilation overhead
        self.interpretation_time = 0  # Track interpretation time
        self.compiled_execution_time = 0  # Track compiled execution time

    def execute(self, function):
        """
        Execute or compile function based on execution count.

        Args:
            function: Function to execute

        Returns:
            Result of function execution
        """
        func_name = function.__name__

        # Increment execution count
        if func_name not in self.execution_count:
            self.execution_count[func_name] = 0
        self.execution_count[func_name] += 1

        # Check if should compile
        if self.execution_count[func_name] >= self.JIT_THRESHOLD:
            if func_name not in self.code_cache:
                # Compile function
                start = time.time()
                compiled = self.compile(function)
                self.code_cache[func_name] = compiled
                self.compilation_time += time.time() - start
                print(
                    f"[JIT] Compiled {func_name} after {self.execution_count[func_name]} executions")

            # Execute compiled code
            start = time.time()
            result = self.code_cache[func_name]()
            self.compiled_execution_time += time.time() - start
            return result
        else:
            # Interpret
            start = time.time()
            result = self.interpret(function)
            self.interpretation_time += time.time() - start
            return result

    def compile(self, function):
        """
        Compile function to optimized form.

        In a real JIT, this would generate machine code.
        Here we simulate by creating an optimized closure.

        Args:
            function: Function to compile

        Returns:
            Compiled (optimized) function
        """
        # Simulate compilation by creating an optimized version
        # In reality, this would generate machine code
        return lambda: function()

    def interpret(self, function):
        """
        Interpret function execution.

        Args:
            function: Function to interpret

        Returns:
            Result of function execution
        """
        return function()

    def print_statistics(self):
        """Print JIT compiler statistics"""
        print("\n=== JIT Compiler Statistics ===")
        print(f"Compilation time: {self.compilation_time*1000:.2f} ms")
        print(f"Interpretation time: {self.interpretation_time*1000:.2f} ms")
        print(
            f"Compiled execution time: {self.compiled_execution_time*1000:.2f} ms")
        print(f"\nFunctions compiled: {len(self.code_cache)}")
        print("\nExecution counts:")
        for func_name, count in self.execution_count.items():
            compiled = " (COMPILED)" if func_name in self.code_cache else ""
            print(f"  {func_name}: {count} executions{compiled}")


# Example functions to JIT compile
def fibonacci(n):
    """Calculate fibonacci number (recursive)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_range(n):
    """Sum numbers from 1 to n"""
    return sum(range(1, n + 1))


# Example usage
if __name__ == "__main__":
    print("=== JIT Compiler Demo ===\n")

    jit = JITCompiler(jit_threshold=5)

    # Execute fibonacci multiple times
    print("Executing fibonacci(10) multiple times...")
    for i in range(15):
        result = jit.execute(lambda: fibonacci(10))
        if i == 0:
            print(f"  Result: {result}")

    print("\nExecuting factorial(10) multiple times...")
    for i in range(12):
        result = jit.execute(lambda: factorial(10))
        if i == 0:
            print(f"  Result: {result}")

    print("\nExecuting sum_range(100) multiple times...")
    for i in range(8):
        result = jit.execute(lambda: sum_range(100))
        if i == 0:
            print(f"  Result: {result}")

    # Print statistics
    jit.print_statistics()

    # Demonstrate performance benefit
    print("\n" + "="*50)
    print("\nPerformance comparison:")
    print("(In a real JIT, compiled code would be much faster)")

    # Simulate hot loop
    print("\nSimulating hot loop (1000 iterations)...")
    jit2 = JITCompiler(jit_threshold=10)

    def hot_function():
        total = 0
        for i in range(100):
            total += i * i
        return total

    start = time.time()
    for _ in range(1000):
        jit2.execute(hot_function)
    elapsed = time.time() - start

    print(f"Total time: {elapsed*1000:.2f} ms")
    jit2.print_statistics()
