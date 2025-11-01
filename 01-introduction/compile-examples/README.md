# Compiler Examples - Executable Python Code

This directory contains executable Python implementations of compiler concepts from the compilation principles tutorial (`01-introduction/compile.md`).

## Overview

Each file is a standalone, runnable Python program that demonstrates a specific compiler component or technique. All examples include:

- Detailed docstrings explaining the concept
- Working implementations
- Example usage with test cases
- Educational comments

## Files and Descriptions

### Chapter 3: Lexical Analysis

#### `chapter3_lexer_manual.py`

**Manual Lexer Implementation**

- Hand-coded lexer using state transitions
- Recognizes numbers, identifiers, keywords, and operators
- Demonstrates character-by-character scanning
- **Run:** `python chapter3_lexer_manual.py`

#### `chapter3_lexer_regex.py`

**Regex-based Lexer**

- Uses Python's `re` module for pattern matching
- More declarative approach than manual implementation
- Supports floating-point numbers
- **Run:** `python chapter3_lexer_regex.py`

### Chapter 4: Syntax Analysis

#### `chapter4_parser_recursive_descent.py`

**Recursive Descent Parser**

- Implements a hand-written parser for arithmetic expressions
- Builds Abstract Syntax Tree (AST)
- Handles operator precedence correctly
- Grammar: `E → T (('+' | '-') T)*`, `T → F (('*' | '/') F)*`, `F → '(' E ')' | number | identifier`
- **Run:** `python chapter4_parser_recursive_descent.py`

### Chapter 5: Semantic Analysis

#### `chapter5_semantic_analyzer.py`

**Semantic Analyzer with Type Checking**

- Symbol table management with scoping
- Type checking for expressions and statements
- Function declaration and call validation
- Error collection and reporting
- **Run:** `python chapter5_semantic_analyzer.py`

### Chapter 6: Intermediate Code Generation

#### `chapter6_intermediate_code_generator.py`

**Three-Address Code Generator**

- Generates three-address code (TAC) from AST
- Implements quadruples (op, arg1, arg2, result)
- Handles expressions, assignments, and control flow
- Manages temporary variables and labels
- **Run:** `python chapter6_intermediate_code_generator.py`

### Chapter 7: Code Optimization

#### `chapter7_optimizer.py`

**Code Optimization Techniques**

- Constant folding: Evaluate constant expressions at compile time
- Constant propagation: Replace variables with known values
- Dead code elimination concepts
- Demonstrates optimization effectiveness
- **Run:** `python chapter7_optimizer.py`

### Chapter 9: Runtime Environment

#### `chapter9_calling_convention.py`

**x86-64 Calling Convention**

- Implements x86-64 System V ABI calling convention
- Parameter allocation to registers or stack
- Function prologue and epilogue generation
- Demonstrates register usage rules
- **Run:** `python chapter9_calling_convention.py`

#### `chapter9_heap_manager.py`

**Heap Memory Manager**

- Dynamic memory allocation (malloc/free)
- First-fit allocation strategy
- Free list management
- Automatic coalescing of adjacent free blocks
- **Run:** `python chapter9_heap_manager.py`

#### `chapter9_garbage_collector.py`

**Mark-and-Sweep Garbage Collector**

- Implements mark-and-sweep GC algorithm
- Root set management
- Handles circular references
- Demonstrates automatic memory reclamation
- **Run:** `python chapter9_garbage_collector.py`

### Chapter 10: Modern Compilation Techniques

#### `chapter10_jit_compiler.py`

**Just-In-Time (JIT) Compiler**

- Mixed interpretation/compilation mode
- Hot code detection based on execution frequency
- Execution counting and profiling
- Demonstrates JIT compilation strategy
- **Run:** `python chapter10_jit_compiler.py`

### Chapter 12: Compiler Testing

#### `chapter12_compiler_fuzzer.py`

**Compiler Fuzzer**

- Random program generation
- Malformed input generation for error testing
- Crash detection and reporting
- Fuzzing statistics
- **Run:** `python chapter12_compiler_fuzzer.py`

## Running the Examples

All examples are standalone Python scripts. To run any example:

```bash
cd compile-examples
python <filename>.py
```

For example:

```bash
python chapter3_lexer_manual.py
python chapter4_parser_recursive_descent.py
python chapter9_garbage_collector.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies (all examples use only Python standard library)

## Learning Path

Recommended order for studying the examples:

1. **Lexical Analysis** (Chapter 3)
   - Start with `chapter3_lexer_manual.py` to understand basic tokenization
   - Then `chapter3_lexer_regex.py` for a more elegant approach

2. **Syntax Analysis** (Chapter 4)
   - `chapter4_parser_recursive_descent.py` to build ASTs

3. **Semantic Analysis** (Chapter 5)
   - `chapter5_semantic_analyzer.py` for type checking and symbol tables

4. **Intermediate Code** (Chapter 6)
   - `chapter6_intermediate_code_generator.py` to generate three-address code

5. **Optimization** (Chapter 7)
   - `chapter7_optimizer.py` to see optimization techniques in action

6. **Runtime Environment** (Chapter 9)
   - `chapter9_calling_convention.py` for function calling
   - `chapter9_heap_manager.py` for memory management
   - `chapter9_garbage_collector.py` for automatic memory reclamation

7. **Modern Techniques** (Chapter 10)
   - `chapter10_jit_compiler.py` for JIT compilation concepts

8. **Testing** (Chapter 12)
   - `chapter12_compiler_fuzzer.py` for compiler testing strategies

## Extending the Examples

These examples are designed to be educational and extensible. You can:

- Add more token types to the lexers
- Extend the parser grammar to support more language features
- Implement additional optimization passes
- Add more sophisticated GC algorithms (generational, copying, etc.)
- Enhance the JIT compiler with actual code generation
- Create more sophisticated fuzzing strategies

## Notes

- These are simplified educational implementations
- Production compilers are much more complex
- Focus is on clarity and understanding, not performance
- Each example is self-contained for easy experimentation

## Related Documentation

See `../01-introduction/compile.md` for the complete compilation principles tutorial that these examples are based on.

## License

These examples are part of the SAST C++ course materials.
