"""
Chapter 9: Runtime Environment - Calling Convention

This module demonstrates the x86-64 System V ABI calling convention,
which defines how function parameters are passed and how the stack
is managed during function calls.

Features:
- Parameter allocation to registers or stack
- Register classification (caller-saved vs callee-saved)
- Stack frame management
- Return value handling
"""


class Parameter:
    """Represents a function parameter"""

    def __init__(self, name, param_type):
        self.name = name
        self.type = param_type


class CallingConvention:
    """x86-64 System V ABI calling convention"""

    def __init__(self):
        # 前6个整数参数使用寄存器: rdi, rsi, rdx, rcx, r8, r9
        self.int_param_regs = ['rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9']
        # 前8个浮点参数使用寄存器: xmm0-xmm7
        self.float_param_regs = [f'xmm{i}' for i in range(8)]
        # 返回值寄存器: rax (整数), xmm0 (浮点)
        self.return_regs = {'int': 'rax', 'float': 'xmm0'}
        # 被调用者保存的寄存器
        self.callee_saved = ['rbx', 'rbp', 'r12', 'r13', 'r14', 'r15']
        # 调用者保存的寄存器
        self.caller_saved = ['rax', 'rcx', 'rdx',
                             'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11']

    def allocate_parameters(self, params):
        """
        Allocate parameters to registers or stack.

        Args:
            params: List of Parameter objects

        Returns:
            List of tuples (param_name, location)
            where location is either a register name or stack offset
        """
        allocations = []
        int_reg_idx = 0
        float_reg_idx = 0
        stack_offset = 0

        for param in params:
            if param.type == 'int' and int_reg_idx < len(self.int_param_regs):
                allocations.append(
                    (param.name, self.int_param_regs[int_reg_idx]))
                int_reg_idx += 1
            elif param.type == 'float' and float_reg_idx < len(self.float_param_regs):
                allocations.append(
                    (param.name, self.float_param_regs[float_reg_idx]))
                float_reg_idx += 1
            else:
                # 参数放在栈上
                allocations.append((param.name, f'[rbp+{stack_offset + 16}]'))
                stack_offset += 8

        return allocations

    def generate_function_prologue(self, local_vars_size):
        """
        Generate function prologue (entry code).

        Args:
            local_vars_size: Size of local variables in bytes

        Returns:
            List of assembly instructions
        """
        prologue = [
            "push rbp",              # Save old base pointer
            "mov rbp, rsp",          # Set new base pointer
            f"sub rsp, {local_vars_size}"  # Allocate space for locals
        ]

        # Save callee-saved registers if needed
        for reg in self.callee_saved:
            if reg != 'rbp':  # rbp already saved
                prologue.append(f"push {reg}")

        return prologue

    def generate_function_epilogue(self):
        """
        Generate function epilogue (exit code).

        Returns:
            List of assembly instructions
        """
        epilogue = []

        # Restore callee-saved registers
        for reg in reversed(self.callee_saved):
            if reg != 'rbp':
                epilogue.append(f"pop {reg}")

        epilogue.extend([
            "mov rsp, rbp",          # Restore stack pointer
            "pop rbp",               # Restore base pointer
            "ret"                    # Return
        ])

        return epilogue

    def generate_function_call(self, function_name, args):
        """
        Generate code for a function call.

        Args:
            function_name: Name of function to call
            args: List of argument values

        Returns:
            List of assembly instructions
        """
        instructions = []

        # Allocate arguments to registers/stack
        int_reg_idx = 0
        float_reg_idx = 0
        stack_args = []

        for arg in args:
            if arg['type'] == 'int' and int_reg_idx < len(self.int_param_regs):
                instructions.append(
                    f"mov {self.int_param_regs[int_reg_idx]}, {arg['value']}")
                int_reg_idx += 1
            elif arg['type'] == 'float' and float_reg_idx < len(self.float_param_regs):
                instructions.append(
                    f"movsd {self.float_param_regs[float_reg_idx]}, {arg['value']}")
                float_reg_idx += 1
            else:
                stack_args.append(arg)

        # Push stack arguments in reverse order
        for arg in reversed(stack_args):
            instructions.append(f"push {arg['value']}")

        # Call the function
        instructions.append(f"call {function_name}")

        # Clean up stack if needed
        if stack_args:
            instructions.append(f"add rsp, {len(stack_args) * 8}")

        return instructions


# Example usage
if __name__ == "__main__":
    convention = CallingConvention()

    # Example 1: Parameter allocation
    print("=== Example 1: Parameter Allocation ===")
    params = [
        Parameter('a', 'int'),
        Parameter('b', 'int'),
        Parameter('c', 'int'),
        Parameter('d', 'float'),
        Parameter('e', 'int'),
        Parameter('f', 'int'),
        Parameter('g', 'int'),  # This will go on stack
    ]

    allocations = convention.allocate_parameters(params)
    print("Function parameters:")
    for name, location in allocations:
        print(f"  {name}: {location}")
    print()

    # Example 2: Function prologue
    print("=== Example 2: Function Prologue ===")
    prologue = convention.generate_function_prologue(32)  # 32 bytes for locals
    print("Prologue instructions:")
    for instr in prologue:
        print(f"  {instr}")
    print()

    # Example 3: Function epilogue
    print("=== Example 3: Function Epilogue ===")
    epilogue = convention.generate_function_epilogue()
    print("Epilogue instructions:")
    for instr in epilogue:
        print(f"  {instr}")
    print()

    # Example 4: Function call
    print("=== Example 4: Function Call ===")
    args = [
        {'type': 'int', 'value': '5'},
        {'type': 'int', 'value': '10'},
        {'type': 'int', 'value': '15'},
    ]
    call_code = convention.generate_function_call('add_three', args)
    print("Call instructions:")
    for instr in call_code:
        print(f"  {instr}")
