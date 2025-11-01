# 编译原理：编译流程完整教程

## 课程目标

- 深入理解编译器的完整工作原理和实现细节
- 掌握编译过程各个阶段的算法和数据结构
- 了解现代编译技术和优化方法
- 能够设计和实现简单的编译器

---

## 第一章：编译器基础

### 1.1 什么是编译器？

编译器是一种特殊的程序，它将用某种编程语言（源语言）编写的程序转换为另一种编程语言（目标语言）编写的等价程序。

**编译器的定义特征：**

- **输入：** 源程序（高级语言）
- **输出：** 目标程序（低级语言/机器代码）
- **保持语义等价性**
- **进行错误检测和报告**

### 1.2 编译器 vs 解释器

**编译器：**

- 一次性翻译整个程序
- 生成独立的可执行文件
- 执行速度快
- 示例：C、C++、Go

**解释器：**

- 逐条解释执行语句
- 不生成独立的目标程序
- 启动快，但执行较慢
- 示例：Python、Ruby、JavaScript（早期）

**混合模式：**

- **Java：** 编译成字节码 + JVM 解释/JIT
- **Python：** 编译成字节码 + 解释器执行
- **JavaScript：** V8 引擎的 JIT 编译

### 1.3 编译器的历史

| 年代 | 重要事件 |
|------|----------|
| 1950年代 | FORTRAN 编译器（John Backus，IBM） |
| 1960年代 | COBOL、ALGOL，编译理论奠基 |
| 1970年代 | C 语言和 Unix，可移植编译器 |
| 1980年代 | C++、Ada，面向对象语言 |
| 1990年代 | Java、Python，虚拟机和动态语言 |
| 2000年代至今 | LLVM、Rust、Go，现代编译技术 |

### 1.4 编译器在软件系统中的位置

```text
源程序 (.c)
    ↓
预处理器 (cpp) → 预处理后的源程序
    ↓
编译器 (cc1) → 汇编代码 (.s)
    ↓
汇编器 (as) → 可重定位目标文件 (.o)
    ↓
链接器 (ld) + 库文件 → 可执行文件
    ↓
加载器 → 内存中的可执行程序
    ↓
执行
```

---

## 第二章：编译流程概览

### 2.1 编译过程的阶段划分

编译器的工作可以分为**分析部分（前端）**和**综合部分（后端）**：

**分析部分（Analysis）：**

1. 词法分析（Lexical Analysis）
2. 语法分析（Syntax Analysis）
3. 语义分析（Semantic Analysis）

**综合部分（Synthesis）：**

4. 中间代码生成（Intermediate Code Generation）
5. 代码优化（Code Optimization）
6. 目标代码生成（Code Generation）

**辅助模块：**

- 符号表管理（Symbol Table Management）
- 错误处理（Error Handling）

### 2.2 编译流程数据流图

```text
源程序
    ↓
┌─────────────────┐
│   词法分析器    │ ← 符号表
│ (Lexer/Scanner) │
└─────────────────┘
    ↓ Token Stream
┌─────────────────┐
│   语法分析器    │ ← 符号表
│    (Parser)     │
└─────────────────┘
    ↓ Syntax Tree
┌─────────────────┐
│   语义分析器    │ ↔ 符号表
│(Semantic Analyzer)│
└─────────────────┘
    ↓ Annotated Tree
┌─────────────────┐
│ 中间代码生成器  │ ↔ 符号表
└─────────────────┘
    ↓ Intermediate Code
┌─────────────────┐
│   代码优化器    │
└─────────────────┘
    ↓ Optimized Code
┌─────────────────┐
│ 目标代码生成器  │
└─────────────────┘
    ↓
目标程序
```

---

## 第三章：词法分析（Lexical Analysis）

### 3.1 词法分析的任务

词法分析器（Lexer/Scanner）是编译器的第一个阶段，负责：

- 读取源程序的字符流
- 将字符序列组织成词法单元（Token）
- 过滤注释和空白字符
- 记录行号，用于错误报告
- 可能进行宏扩展（预处理）

### 3.2 词法单元（Token）

Token 是语法分析的最小单位，包含两部分信息：

- **Token 类型（Token Type）**
- **Token 值（Token Value）**

**常见的 Token 类型：**

| 类型 | 说明 | 示例 |
|------|------|------|
| 关键字 (Keyword) | 语言保留字 | if, while, return, int, void |
| 标识符 (Identifier) | 变量名、函数名 | variable, functionName |
| 常量 (Constant) | 字面值 | 123, 3.14, "hello", 'a' |
| 运算符 (Operator) | 操作符 | +, -, *, /, =, ==, != |
| 分隔符 (Delimiter) | 分隔符号 | (, ), {, }, [, ], ;, , |

### 3.3 词法分析示例

**源代码：**

```c
int main() {
    int count = 0;
    count = count + 1;
    return count;
}
```

**Token 序列：**

```text
<KEYWORD, "int">
<IDENTIFIER, "main">
<LPAREN, "(">
<RPAREN, ")">
<LBRACE, "{">
<KEYWORD, "int">
<IDENTIFIER, "count">
<ASSIGN, "=">
<NUMBER, "0">
<SEMICOLON, ";">
<IDENTIFIER, "count">
<ASSIGN, "=">
<IDENTIFIER, "count">
<PLUS, "+">
<NUMBER, "1">
<SEMICOLON, ";">
<KEYWORD, "return">
<IDENTIFIER, "count">
<SEMICOLON, ";">
<RBRACE, "}">
```

### 3.4 词法分析的实现方法

#### 3.4.1 手工编码

使用状态转换图或直接编程实现：

```python
def lexer(input_string):
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
        if input_string[i] in '+-*/=(){}[];,':
            tokens.append(('OPERATOR', input_string[i]))
            i += 1
            continue

        # 未知字符
        raise Exception(f"Unknown character: {input_string[i]}")

    return tokens
```

#### 3.4.2 正则表达式

使用正则表达式定义 Token 模式：

```python
import re

class RegexLexer:
    def __init__(self):
        # 定义 Token 模式
        self.token_patterns = [
            ('NUMBER',    r'\d+(\.\d*)?'),           # 整数或浮点数
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), # 标识符
            ('PLUS',      r'\+'),                     # 加号
            ('MINUS',     r'-'),                      # 减号
            ('TIMES',     r'\*'),                     # 乘号
            ('DIVIDE',    r'/'),                      # 除号
            ('LPAREN',    r'\('),                     # 左括号
            ('RPAREN',    r'\)'),                     # 右括号
            ('WHITESPACE', r'\s+'),                   # 空白字符
        ]

        # 编译正则表达式
        self.regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_patterns)
        self.pattern = re.compile(self.regex)

    def tokenize(self, code):
        tokens = []
        for match in self.pattern.finditer(code):
            token_type = match.lastgroup
            token_value = match.group()

            # 跳过空白字符
            if token_type == 'WHITESPACE':
                continue

            tokens.append((token_type, token_value))

        return tokens
```

#### 3.4.3 有限自动机（Finite Automaton）

**确定有限自动机（DFA）示例：**

**识别标识符的 DFA：**

```text
状态 0 (初始状态)
  --[字母或_]--> 状态 1 (接受状态)

状态 1 (接受状态)
  --[字母、数字或_]--> 状态 1
```

**识别整数的 DFA：**

```text
状态 0 (初始状态)
  --[数字]--> 状态 1 (接受状态)

状态 1 (接受状态)
  --[数字]--> 状态 1
```

### 3.5 词法分析工具

**Lex/Flex：**

```lex
%{
#include <stdio.h>
%}

%%
[0-9]+          { printf("NUMBER: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("IDENTIFIER: %s\n", yytext); }
"+"             { printf("PLUS\n"); }
"-"             { printf("MINUS\n"); }
"*"             { printf("TIMES\n"); }
"/"             { printf("DIVIDE\n"); }
[ \t\n]         { /* 忽略空白字符 */ }
.               { printf("UNKNOWN: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}
```

### 3.6 词法分析中的难点

**1. 最长匹配原则：**

```c
int count = 0;  // "count" 而不是 "c" + "ount"
```

**2. 关键字识别：**

```c
int if = 5;     // "if" 是关键字还是标识符？
```

**3. 浮点数识别：**

```text
3.14, .5, 3., 1e10, 1.5e-3
```

**4. 字符串和转义字符：**

```c
"Hello \"World\"\n"
```

**5. 注释处理：**

```c
// 单行注释
/* 多行
   注释 */
```

---
## 第四章：语法分析（Syntax Analysis）

### 4.1 语法分析的任务

语法分析器（Parser）的主要职责：

- 接收词法分析器产生的 Token 序列
- 根据语言的语法规则检查 Token 序列的结构
- 构建语法树（Parse Tree）或抽象语法树（AST）
- 报告语法错误

### 4.2 上下文无关文法（Context-Free Grammar）

#### 4.2.1 文法的定义

一个上下文无关文法 G 由四元组 (N, T, P, S) 定义：

- **N：** 非终结符集合（Non-terminals）
- **T：** 终结符集合（Terminals）
- **P：** 产生式集合（Productions）
- **S：** 起始符号（Start symbol）

#### 4.2.2 BNF 表示法

**示例：简单算术表达式文法**

```bnf
E → E + T | E - T | T
T → T * F | T / F | F
F → (E) | number | identifier
```

**扩展 BNF（EBNF）：**

```bnf
E → T (('+' | '-') T)*
T → F (('*' | '/') F)*
F → '(' E ')' | number | identifier
```

#### 4.2.3 推导和归约

**最左推导示例：** `id + id * id`

```text
E ⇒ E + T
  ⇒ T + T
  ⇒ F + T
  ⇒ id + T
  ⇒ id + T * F
  ⇒ id + F * F
  ⇒ id + id * F
  ⇒ id + id * id
```

### 4.3 语法树

#### 4.3.1 分析树（Parse Tree）

**对于表达式 `a + b * c`：**

```text
          E
         /|\
        E + T
        |  /|\
        T T * F
        | |   |
        F F   c
        | |
        a b
```

#### 4.3.2 抽象语法树（AST）

**简化的表示：**

```text
       +
      / \
     a   *
        / \
       b   c
```

**AST 节点定义（Python）：**

```python
class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

# 构建 AST: a + b * c
ast = BinOp(
    Identifier('a'),
    '+',
    BinOp(
        Identifier('b'),
        '*',
        Identifier('c')
    )
)
```

### 4.4 自顶向下分析

#### 4.4.1 递归下降分析

**手写递归下降分析器示例：**

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type):
        """消费一个 token"""
        token = self.current_token()
        if token and token[0] == expected_type:
            self.pos += 1
            return token
        raise Exception(f"Expected {expected_type}, got {token}")

    def parse_expression(self):
        """E → T (('+' | '-') T)*"""
        left = self.parse_term()

        while self.current_token() and self.current_token()[1] in ['+', '-']:
            op = self.consume('OPERATOR')
            right = self.parse_term()
            left = BinOp(left, op[1], right)

        return left

    def parse_term(self):
        """T → F (('*' | '/') F)*"""
        left = self.parse_factor()

        while self.current_token() and self.current_token()[1] in ['*', '/']:
            op = self.consume('OPERATOR')
            right = self.parse_factor()
            left = BinOp(left, op[1], right)

        return left

    def parse_factor(self):
        """F → '(' E ')' | number | identifier"""
        token = self.current_token()

        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return Number(int(token[1]))

        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return Identifier(token[1])

        elif token[1] == '(':
            self.consume('OPERATOR')
            expr = self.parse_expression()
            self.consume('OPERATOR')  # ')'
            return expr

        raise Exception(f"Unexpected token: {token}")
```

#### 4.4.2 LL(1) 分析

**LL(1) 分析表构造：**

1. 计算 FIRST 集合
2. 计算 FOLLOW 集合
3. 构造预测分析表

**示例：简单表达式文法的 LL(1) 分析表**

```text
文法：
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id

分析表：
        id      +       *       (       )       $
E       TE'     -       -       TE'     -       -
E'      -       +TE'    -       -       ε       ε
T       FT'     -       -       FT'     -       -
T'      -       ε       *FT'    -       ε       ε
F       id      -       -       (E)     -       -
```

### 4.5 自底向上分析

#### 4.5.1 LR 分析

**LR 分析的类型：**

- **LR(0)：** 最简单，实用性有限
- **SLR(1)：** Simple LR，改进的 LR(0)
- **LR(1)：** 规范 LR，功能最强
- **LALR(1)：** Look-Ahead LR，Yacc/Bison 使用

#### 4.5.2 移进-归约分析

**操作类型：**

- **移进（Shift）：** 将当前输入符号压入栈
- **归约（Reduce）：** 用产生式左部替换栈顶的产生式右部
- **接受（Accept）：** 分析成功
- **报错（Error）：** 语法错误

**示例：分析 `id + id * id`**

```text
栈              输入              动作
$               id+id*id$         移进
$id             +id*id$           归约 F→id
$F              +id*id$           归约 T→F
$T              +id*id$           归约 E→T
$E              +id*id$           移进
$E+             id*id$            移进
$E+id           *id$              归约 F→id
$E+F            *id$              归约 T→F
$E+T            *id$              移进
$E+T*           id$               移进
$E+T*id         $                 归约 F→id
$E+T*F          $                 归约 T→T*F
$E+T            $                 归约 E→E+T
$E              $                 接受
```

### 4.6 语法分析工具

#### 4.6.1 Yacc/Bison

```yacc
%{
#include <stdio.h>
#include <stdlib.h>
%}

%token NUMBER IDENTIFIER
%left '+' '-'
%left '*' '/'

%%
program:
    expression { printf("Result: %d\n", $1); }
    ;

expression:
    expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression { $$ = $1 / $3; }
    | '(' expression ')' { $$ = $2; }
    | NUMBER { $$ = $1; }
    ;
%%

int main() {
    yyparse();
    return 0;
}
```

### 4.7 错误恢复

#### 4.7.1 恐慌模式（Panic Mode）

跳过输入符号，直到找到同步记号（如分号、右括号）

#### 4.7.2 短语层次恢复

在栈顶或输入中进行局部修正

#### 4.7.3 错误产生式

在文法中加入错误产生式来处理常见错误

#### 4.7.4 全局纠正

找到最少修改使程序合法（开销大，很少使用）

---

## 第五章：语义分析（Semantic Analysis）

### 5.1 语义分析的任务

语义分析确保程序在语法正确的基础上，语义也是合理的：

- **类型检查：** 确保操作数类型匹配
- **作用域检查：** 确保变量在使用前已声明
- **类型转换：** 插入必要的隐式类型转换
- **语义约束：** 检查各种语言特定的规则

### 5.2 符号表（Symbol Table）

#### 5.2.1 符号表的作用

符号表存储标识符的属性信息：

- 名称（Name）
- 类型（Type）
- 作用域（Scope）
- 存储位置（Memory Location）
- 其他属性（常量值、函数参数等）

#### 5.2.2 符号表的实现

**哈希表实现：**

```python
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None  # 支持嵌套作用域

    def define(self, name, symbol_type, attributes=None):
        """定义新符号"""
        if name in self.symbols:
            raise Exception(f"Symbol '{name}' already defined")

        self.symbols[name] = {
            'type': symbol_type,
            'attributes': attributes or {}
        }

    def lookup(self, name):
        """查找符号（支持作用域链）"""
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return None

    def enter_scope(self):
        """进入新作用域"""
        new_table = SymbolTable()
        new_table.parent = self
        return new_table

    def exit_scope(self):
        """退出当前作用域"""
        return self.parent
```

#### 5.2.3 作用域管理

**词法作用域示例：**

```c
int x = 10;          // 全局作用域

void foo() {
    int x = 20;      // 局部作用域
    {
        int x = 30;  // 内层作用域
        printf("%d", x);  // 输出 30
    }
    printf("%d", x);      // 输出 20
}
```

**符号表结构：**

```text
全局符号表
├─ x: int, global
└─ foo: function
   └─ 局部符号表
      ├─ x: int, local
      └─ 块符号表
         └─ x: int, local
```

### 5.3 类型系统

#### 5.3.1 类型检查

**基本类型检查规则：**

```python
def check_binary_op(left_type, op, right_type):
    """检查二元运算的类型"""
    # 算术运算符
    if op in ['+', '-', '*', '/']:
        if left_type in ['int', 'float'] and right_type in ['int', 'float']:
            # 如果有一个是 float，结果为 float
            if left_type == 'float' or right_type == 'float':
                return 'float'
            return 'int'
        else:
            raise TypeError(f"Cannot apply {op} to {left_type} and {right_type}")

    # 比较运算符
    elif op in ['<', '>', '<=', '>=', '==', '!=']:
        if left_type in ['int', 'float'] and right_type in ['int', 'float']:
            return 'bool'
        else:
            raise TypeError(f"Cannot compare {left_type} and {right_type}")

    # 逻辑运算符
    elif op in ['&&', '||']:
        if left_type == 'bool' and right_type == 'bool':
            return 'bool'
        else:
            raise TypeError(f"Logical operators require bool operands")

    else:
        raise Exception(f"Unknown operator: {op}")
```

#### 5.3.2 类型转换

**隐式类型转换（Type Coercion）：**

```c
int a = 5;
float b = 3.14;
float c = a + b;  // a 被隐式转换为 float
```

**显式类型转换（Type Casting）：**

```c
float x = 3.14;
int y = (int)x;  // 显式转换，y = 3
```

**类型转换的实现：**

```python
class TypeChecker:
    def insert_cast(self, node, from_type, to_type):
        """插入类型转换节点"""
        if from_type == to_type:
            return node

        if self.can_cast(from_type, to_type):
            return CastNode(node, to_type)
        else:
            raise TypeError(f"Cannot cast {from_type} to {to_type}")

    def can_cast(self, from_type, to_type):
        """判断是否可以进行类型转换"""
        # 定义类型转换规则
        cast_rules = {
            ('int', 'float'): True,
            ('int', 'double'): True,
            ('float', 'double'): True,
            ('char', 'int'): True,
            # ... 其他规则
        }
        return cast_rules.get((from_type, to_type), False)
```

#### 5.3.3 类型推导

**示例：变量类型推导**

```python
# Python 风格的类型推导
x = 42        # 推导为 int
y = 3.14      # 推导为 float
z = x + y     # 推导为 float

def infer_type(node, symbol_table):
    """类型推导"""
    if isinstance(node, Number):
        if '.' in str(node.value):
            return 'float'
        return 'int'

    elif isinstance(node, Identifier):
        symbol = symbol_table.lookup(node.name)
        if symbol:
            return symbol['type']
        else:
            raise NameError(f"Undefined variable: {node.name}")

    elif isinstance(node, BinOp):
        left_type = infer_type(node.left, symbol_table)
        right_type = infer_type(node.right, symbol_table)
        return check_binary_op(left_type, node.op, right_type)
```

### 5.4 语义检查示例

#### 5.4.1 完整的语义分析器

```python
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def visit(self, node):
        """访问者模式"""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def visit_BinOp(self, node):
        """二元运算"""
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        return check_binary_op(left_type, node.op, right_type)

    def visit_Number(self, node):
        """数字字面量"""
        if isinstance(node.value, int):
            return 'int'
        return 'float'

    def visit_Identifier(self, node):
        """标识符"""
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.errors.append(f"Undefined variable: {node.name}")
            return 'error'
        return symbol['type']

    def visit_Assignment(self, node):
        """赋值语句"""
        # 检查变量是否已声明
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.errors.append(f"Undefined variable: {node.name}")
            return 'error'

        # 检查赋值类型是否匹配
        value_type = self.visit(node.value)
        if symbol['type'] != value_type:
            if not self.can_cast(value_type, symbol['type']):
                self.errors.append(
                    f"Type mismatch: cannot assign {value_type} to {symbol['type']}"
                )

        return symbol['type']

    def visit_FunctionCall(self, node):
        """函数调用"""
        # 检查函数是否已声明
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.errors.append(f"Undefined function: {node.name}")
            return 'error'

        if symbol['type'] != 'function':
            self.errors.append(f"'{node.name}' is not a function")
            return 'error'

        # 检查参数数量
        expected_params = symbol['attributes'].get('params', [])
        if len(node.arguments) != len(expected_params):
            self.errors.append(
                f"Function '{node.name}' expects {len(expected_params)} arguments, "
                f"got {len(node.arguments)}"
            )
            return symbol['attributes'].get('return_type', 'void')

        # 检查参数类型
        for i, (arg, param) in enumerate(zip(node.arguments, expected_params)):
            arg_type = self.visit(arg)
            if arg_type != param['type']:
                if not self.can_cast(arg_type, param['type']):
                    self.errors.append(
                        f"Argument {i+1} type mismatch: expected {param['type']}, "
                        f"got {arg_type}"
                    )

        return symbol['attributes'].get('return_type', 'void')

    def visit_FunctionDeclaration(self, node):
        """函数声明"""
        # 添加函数到符号表
        self.symbol_table.define(node.name, 'function', {
            'params': node.parameters,
            'return_type': node.return_type
        })

        # 进入新作用域
        self.symbol_table = self.symbol_table.enter_scope()

        # 添加参数到作用域
        for param in node.parameters:
            self.symbol_table.define(param['name'], param['type'])

        # 分析函数体
        for statement in node.body:
            self.visit(statement)

        # 退出作用域
        self.symbol_table = self.symbol_table.exit_scope()

    def visit_ReturnStatement(self, node):
        """返回语句"""
        if node.expression:
            return self.visit(node.expression)
        return 'void'

    def visit_IfStatement(self, node):
        """if 语句"""
        condition_type = self.visit(node.condition)
        if condition_type != 'bool':
            self.errors.append(
                f"If condition must be bool, got {condition_type}"
            )

        self.visit(node.then_branch)
        if node.else_branch:
            self.visit(node.else_branch)

    def visit_WhileStatement(self, node):
        """while 语句"""
        condition_type = self.visit(node.condition)
        if condition_type != 'bool':
            self.errors.append(
                f"While condition must be bool, got {condition_type}"
            )

        self.visit(node.body)

    def can_cast(self, from_type, to_type):
        """判断是否可以进行类型转换"""
        cast_rules = {
            ('int', 'float'): True,
            ('int', 'double'): True,
            ('float', 'double'): True,
        }
        return cast_rules.get((from_type, to_type), False)

    def generic_visit(self, node):
        """默认访问方法"""
        raise Exception(f"No visit method for {type(node).__name__}")
```

### 5.5 属性文法（Attribute Grammar）

#### 5.5.1 综合属性和继承属性

**综合属性（Synthesized Attributes）：**
- 由子节点计算得出
- 自底向上传递

**继承属性（Inherited Attributes）：**
- 由父节点或兄弟节点计算得出
- 自顶向下传递

#### 5.5.2 属性文法示例

```text
文法：E → E₁ + T
综合属性计算：
E.type = if E₁.type == int and T.type == int
         then int
         else if E₁.type == float or T.type == float
         then float
         else error

继承属性示例：
Decl → Type VarList
Type.type 是综合属性
VarList.type = Type.type (继承属性)
```

---

## 第六章：中间代码生成

### 6.1 中间表示的作用

中间表示（Intermediate Representation, IR）的优势：

- **机器独立性：** 便于支持多种目标平台
- **优化便利：** 提供统一的优化接口
- **模块化设计：** 前端和后端解耦
- **可读性：** 比机器码更易理解和调试

### 6.2 三地址码（Three-Address Code）

#### 6.2.1 三地址码的形式

每条指令最多有三个操作数，通常形式为：

```text
x = y op z
```

**常见的三地址指令：**

| 类型 | 指令格式 | 说明 |
|------|----------|------|
| 赋值指令 | `x = y` | 简单赋值 |
| 算术指令 | `x = y op z` | op: +, -, *, /, % |
| 逻辑指令 | `x = y op z` | op: &&, \|\|, ! |
| 关系指令 | `x = y relop z` | relop: <, >, ==, !=, <=, >= |
| 无条件跳转 | `goto L` | 跳转到标签 L |
| 条件跳转 | `if x relop y goto L` | 条件跳转 |
|  | `ifFalse x goto L` | 假则跳转 |
| 过程调用 | `param x` | 传递参数 |
|  | `call p, n` | 调用过程 p，n 个参数 |
|  | `x = call p, n` | 带返回值的调用 |
| 返回指令 | `return x` | 返回值 |
| 索引赋值 | `x = y[i]` | 数组读取 |
|  | `x[i] = y` | 数组写入 |
| 地址指令 | `x = &y` | 取地址 |
|  | `x = *y` | 解引用 |
|  | `*x = y` | 间接赋值 |

#### 6.2.2 三地址码示例

**源代码：**

```c
int a = 5;
int b = 10;
int c = a + b * 2;
if (c > 20) {
    c = c - 10;
}
```

**生成的三地址码：**

```text
    a = 5
    b = 10
    t1 = b * 2
    t2 = a + t1
    c = t2
    t3 = c > 20
    ifFalse t3 goto L1
    t4 = c - 10
    c = t4
L1: ...
```

#### 6.2.3 三地址码的实现

**四元式（Quadruple）表示：**

```python
class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op        # 操作符
        self.arg1 = arg1    # 第一个操作数
        self.arg2 = arg2    # 第二个操作数
        self.result = result # 结果

    def __str__(self):
        if self.arg2:
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"
        elif self.arg1:
            return f"{self.result} = {self.op} {self.arg1}"
        else:
            return f"{self.op} {self.result}"

# 示例：t1 = a + b
quad = Quadruple('+', 'a', 'b', 't1')
print(quad)  # 输出: t1 = a + b
```

**三元式（Triple）表示：**

```python
class Triple:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.index = None  # 指令索引，用于引用

    def __str__(self):
        if self.arg2:
            return f"({self.index}) {self.arg1} {self.op} {self.arg2}"
        else:
            return f"({self.index}) {self.op} {self.arg1}"

# 示例：
# (0) t1 = a + b
# (1) t2 = (0) * c
triples = [
    Triple('+', 'a', 'b'),      # 结果通过索引 (0) 引用
    Triple('*', '(0)', 'c')     # 引用第 0 条指令的结果
]
triples[0].index = 0
triples[1].index = 1
```

### 6.3 从 AST 生成三地址码

#### 6.3.1 代码生成器实现

```python
class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []  # 存储生成的三地址码
        self.temp_count = 0  # 临时变量计数器
        self.label_count = 0  # 标签计数器

    def new_temp(self):
        """生成新的临时变量"""
        self.temp_count += 1
        return f't{self.temp_count}'

    def new_label(self):
        """生成新的标签"""
        self.label_count += 1
        return f'L{self.label_count}'

    def emit(self, op, arg1=None, arg2=None, result=None):
        """生成一条三地址码指令"""
        quad = Quadruple(op, arg1, arg2, result)
        self.code.append(quad)
        return quad

    def generate(self, node):
        """从 AST 生成三地址码"""
        method_name = f'gen_{type(node).__name__}'
        generator = getattr(self, method_name, self.generic_gen)
        return generator(node)

    def gen_BinOp(self, node):
        """生成二元运算的三地址码"""
        left = self.generate(node.left)
        right = self.generate(node.right)
        temp = self.new_temp()
        self.emit(node.op, left, right, temp)
        return temp

    def gen_Number(self, node):
        """数字字面量"""
        return str(node.value)

    def gen_Identifier(self, node):
        """标识符"""
        return node.name

    def gen_Assignment(self, node):
        """赋值语句"""
        value = self.generate(node.value)
        self.emit('=', value, None, node.name)
        return node.name

    def gen_IfStatement(self, node):
        """if 语句"""
        # 生成条件表达式的代码
        condition = self.generate(node.condition)

        # 创建标签
        else_label = self.new_label()
        end_label = self.new_label()

        # 条件跳转
        self.emit('ifFalse', condition, None, else_label)

        # then 分支
        self.generate(node.then_branch)
        self.emit('goto', None, None, end_label)

        # else 分支
        self.emit('label', None, None, else_label)
        if node.else_branch:
            self.generate(node.else_branch)

        # 结束标签
        self.emit('label', None, None, end_label)

    def gen_WhileStatement(self, node):
        """while 语句"""
        # 创建标签
        start_label = self.new_label()
        end_label = self.new_label()

        # 循环开始
        self.emit('label', None, None, start_label)

        # 生成条件
        condition = self.generate(node.condition)
        self.emit('ifFalse', condition, None, end_label)

        # 循环体
        self.generate(node.body)
        self.emit('goto', None, None, start_label)

        # 循环结束
        self.emit('label', None, None, end_label)

    def generic_gen(self, node):
        """默认生成方法"""
        raise Exception(f"No generator for {type(node).__name__}")
```

### 6.4 其他中间表示形式

#### 6.4.1 静态单赋值形式（SSA）

**特点：**

- 每个变量只被赋值一次
- 使用 φ 函数合并不同路径的值

**示例：**

```c
// 原始代码
x = 1;
if (condition) {
    x = 2;
} else {
    x = 3;
}
y = x + 1;

// SSA 形式
x₁ = 1;
if (condition) {
    x₂ = 2;
} else {
    x₃ = 3;
}
x₄ = φ(x₂, x₃);  // φ 函数
y₁ = x₄ + 1;
```

#### 6.4.2 控制流图（CFG）

```python
class BasicBlock:
    def __init__(self, label):
        self.label = label
        self.instructions = []
        self.predecessors = []  # 前驱基本块
        self.successors = []    # 后继基本块

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def add_successor(self, block):
        if block not in self.successors:
            self.successors.append(block)
            block.predecessors.append(self)

class ControlFlowGraph:
    def __init__(self):
        self.blocks = []
        self.entry = None
        self.exit = None

    def add_block(self, block):
        self.blocks.append(block)
        if self.entry is None:
            self.entry = block

    def build_from_code(self, code):
        """从三地址码构建 CFG"""
        current_block = BasicBlock('B0')
        self.add_block(current_block)

        for instr in code:
            if instr.op == 'label':
                # 新建基本块
                new_block = BasicBlock(instr.result)
                current_block.add_successor(new_block)
                self.add_block(new_block)
                current_block = new_block
            elif instr.op in ['goto', 'ifFalse', 'if']:
                current_block.add_instruction(instr)
                # 跳转指令结束当前基本块
                new_block = BasicBlock(f'B{len(self.blocks)}')
                self.add_block(new_block)
                current_block = new_block
            else:
                current_block.add_instruction(instr)
```

#### 6.4.3 抽象语法树（AST）作为中间表示

某些现代编译器直接在 AST 上进行优化和代码生成，如 LLVM 的早期版本。

#### 6.4.4 LLVM IR

LLVM IR 是一种类型化的、SSA 形式的中间表示：

```llvm
define i32 @add(i32 %a, i32 %b) {
entry:
  %sum = add i32 %a, %b
  ret i32 %sum
}

define i32 @main() {
entry:
  %result = call i32 @add(i32 5, i32 3)
  ret i32 %result
}
```

---

## 第七章：代码优化

### 7.1 优化的分类

#### 7.1.1 按作用范围分类

**局部优化（Local Optimization）：**

- 在单个基本块内进行
- 开销小，效果有限

**全局优化（Global Optimization）：**

- 在整个函数或过程内进行
- 需要数据流分析

**过程间优化（Interprocedural Optimization）：**

- 跨函数边界进行
- 内联、常量传播等

#### 7.1.2 按机器相关性分类

**机器无关优化：**

- 在中间代码层面进行
- 不依赖具体的目标机器

**机器相关优化：**

- 针对特定处理器架构
- 指令调度、寄存器分配等

### 7.2 数据流分析

#### 7.2.1 到达定义分析（Reaching Definitions）

**目的：** 确定变量的某个定义是否能到达程序的某个点

**数据流方程：**

```text
OUT[B] = GEN[B] ∪ (IN[B] - KILL[B])
IN[B] = ∪ OUT[P]  (对所有前驱 P)
```

**Python 实现：**

```python
def reaching_definitions(cfg):
    """到达定义分析"""
    # 初始化
    IN = {block: set() for block in cfg.blocks}
    OUT = {block: set() for block in cfg.blocks}

    # 计算 GEN 和 KILL 集合
    GEN = {}
    KILL = {}

    for block in cfg.blocks:
        GEN[block] = set()
        KILL[block] = set()

        for instr in block.instructions:
            if instr.result:  # 如果指令定义了变量
                # 添加到 GEN
                GEN[block].add((instr.result, block, instr))
                # KILL 该变量的其他定义
                for other_block in cfg.blocks:
                    for other_instr in other_block.instructions:
                        if other_instr.result == instr.result and other_instr != instr:
                            KILL[block].add((instr.result, other_block, other_instr))

    # 迭代计算不动点
    changed = True
    while changed:
        changed = False

        for block in cfg.blocks:
            # 计算 IN[B]
            new_in = set()
            for pred in block.predecessors:
                new_in |= OUT[pred]

            # 计算 OUT[B]
            new_out = GEN[block] | (new_in - KILL[block])

            if new_in != IN[block] or new_out != OUT[block]:
                changed = True
                IN[block] = new_in
                OUT[block] = new_out

    return IN, OUT
```

#### 7.2.2 活跃变量分析（Live Variable Analysis）

**目的：** 确定变量在程序某个点之后是否会被使用

**数据流方程：**

```text
IN[B] = USE[B] ∪ (OUT[B] - DEF[B])
OUT[B] = ∪ IN[S]  (对所有后继 S)
```

**应用：** 寄存器分配、死代码删除

#### 7.2.3 可用表达式分析（Available Expressions）

**目的：** 确定某个表达式在程序点是否已被计算且值未改变

**应用：** 公共子表达式消除

### 7.3 常见优化技术

#### 7.3.1 常量折叠（Constant Folding）

**原理：** 在编译时计算常量表达式

**示例：**

```c
// 优化前
int a = 2 + 3 * 4;
int b = 100 / 10;

// 优化后
int a = 14;
int b = 10;
```

**实现：**

```python
def constant_folding(node):
    """常量折叠优化"""
    if isinstance(node, BinOp):
        left = constant_folding(node.left)
        right = constant_folding(node.right)

        # 如果两个操作数都是常量，计算结果
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
```

#### 7.3.2 常量传播（Constant Propagation）

**原理：** 将已知的常量值传播到使用它的地方

**示例：**

```c
// 优化前
int x = 5;
int y = x + 3;
int z = x * y;

// 优化后
int x = 5;
int y = 8;      // x 的值传播
int z = 40;     // x 和 y 的值传播并折叠
```

#### 7.3.3 复写传播（Copy Propagation）

**原理：** 用变量的原始定义替换复制

**示例：**

```c
// 优化前
int x = a;
int y = x + b;

// 优化后
int x = a;
int y = a + b;  // 用 a 替换 x
```

#### 7.3.4 死代码删除（Dead Code Elimination）

**原理：** 删除不会影响程序输出的代码

**类型：**

- 无用的赋值
- 不可达代码
- 无效的计算

**示例：**

```c
// 优化前
int x = 5;      // x 从未被使用
int y = 10;
return y;

// 优化后
int y = 10;
return y;
```

**实现：**

```python
def dead_code_elimination(cfg):
    """死代码删除"""
    # 进行活跃变量分析
    live_variable_analysis(cfg)

    for block in cfg.blocks:
        new_instructions = []

        for instr in block.instructions:
            # 如果指令定义的变量是活跃的，保留
            if instr.result and is_live(instr.result, instr, block):
                new_instructions.append(instr)
            # 如果指令有副作用（函数调用、I/O等），保留
            elif has_side_effect(instr):
                new_instructions.append(instr)

        block.instructions = new_instructions
```

#### 7.3.5 公共子表达式消除（Common Subexpression Elimination, CSE）

**原理：** 识别重复计算的表达式，只计算一次

**示例：**

```c
// 优化前
a = b + c;
d = b + c + e;

// 优化后
temp = b + c;
a = temp;
d = temp + e;
```

**实现：**

```python
def common_subexpression_elimination(cfg):
    """公共子表达式消除"""
    # 进行可用表达式分析
    available_exprs = available_expressions_analysis(cfg)

    expr_to_temp = {}  # 表达式到临时变量的映射

    for block in cfg.blocks:
        new_instructions = []

        for instr in block.instructions:
            if instr.op in ['+', '-', '*', '/']:
                # 构造表达式
                expr = (instr.op, instr.arg1, instr.arg2)

                # 检查表达式是否可用
                if expr in available_exprs[block]:
                    # 使用已计算的临时变量
                    if expr in expr_to_temp:
                        new_instr = Quadruple('=', expr_to_temp[expr], None, instr.result)
                        new_instructions.append(new_instr)
                    else:
                        # 第一次计算，保存临时变量
                        expr_to_temp[expr] = instr.result
                        new_instructions.append(instr)
                else:
                    new_instructions.append(instr)
            else:
                new_instructions.append(instr)

        block.instructions = new_instructions
```

#### 7.3.6 代码移动（Code Motion）

**循环不变代码外提（Loop-Invariant Code Motion）：**

**示例：**

```c
// 优化前
for (int i = 0; i < n; i++) {
    x = a + b;  // a 和 b 在循环中不变
    array[i] = x * i;
}

// 优化后
x = a + b;      // 移到循环外
for (int i = 0; i < n; i++) {
    array[i] = x * i;
}
```

#### 7.3.7 强度削减（Strength Reduction）

**原理：** 用开销小的操作替换开销大的操作

**示例：**

```c
// 优化前
for (int i = 0; i < n; i++) {
    a[i] = i * 4;
}

// 优化后
int temp = 0;
for (int i = 0; i < n; i++) {
    a[i] = temp;
    temp = temp + 4;  // 乘法变加法
}
```

#### 7.3.8 函数内联（Function Inlining）

**原理：** 用函数体替换函数调用

**示例：**

```c
// 优化前
int square(int x) {
    return x * x;
}

int main() {
    int a = square(5);
}

// 优化后
int main() {
    int a = 5 * 5;  // 函数体内联并常量折叠
}
```

#### 7.3.9 循环展开（Loop Unrolling）

**原理：** 复制循环体多次以减少循环开销

**示例：**

```c
// 优化前
for (int i = 0; i < 100; i++) {
    a[i] = b[i] + c[i];
}

// 优化后（展开 4 次）
for (int i = 0; i < 100; i += 4) {
    a[i] = b[i] + c[i];
    a[i+1] = b[i+1] + c[i+1];
    a[i+2] = b[i+2] + c[i+2];
    a[i+3] = b[i+3] + c[i+3];
}
```

### 7.4 优化的权衡

**优化的目标：**

- 执行速度
- 代码大小
- 内存使用
- 编译时间
- 能耗

**优化可能带来的问题：**

- 编译时间增加
- 代码膨胀（如循环展开）
- 调试困难
- 数值精度变化

---

## 第八章：目标代码生成

### 8.1 目标代码生成的任务

目标代码生成器将优化后的中间代码转换为目标机器代码，主要任务包括：

- **指令选择：** 为中间代码选择合适的机器指令
- **寄存器分配：** 为变量和临时值分配寄存器
- **指令调度：** 安排指令执行顺序以提高性能

### 8.2 指令选择

#### 8.2.1 简单的指令选择

**示例：x86 汇编**

| 三地址码 | x86 汇编 |
|----------|----------|
| `t1 = a + b` | `MOV EAX, [a]`<br>`ADD EAX, [b]`<br>`MOV [t1], EAX` |
| `t2 = t1 * 2` | `MOV EAX, [t1]`<br>`IMUL EAX, 2`<br>`MOV [t2], EAX` |
| `if t2 > 100`<br>`goto L1` | `MOV EAX, [t2]`<br>`CMP EAX, 100`<br>`JG L1` |

#### 8.2.2 指令选择算法

**树匹配（Tree Matching）：**

使用动态规划找到覆盖表达式树的最优指令序列

**实现示例：**

```python
class InstructionSelector:
    def __init__(self, target_machine):
        self.target = target_machine
        self.code = []

    def select_instructions(self, three_address_code):
        """为三地址码选择机器指令"""
        for instr in three_address_code:
            if instr.op == '+':
                self.emit(f"MOV EAX, {instr.arg1}")
                self.emit(f"ADD EAX, {instr.arg2}")
                self.emit(f"MOV {instr.result}, EAX")

            elif instr.op == '*':
                self.emit(f"MOV EAX, {instr.arg1}")
                self.emit(f"IMUL EAX, {instr.arg2}")
                self.emit(f"MOV {instr.result}, EAX")

            elif instr.op == '=':
                self.emit(f"MOV {instr.result}, {instr.arg1}")

            elif instr.op == 'goto':
                self.emit(f"JMP {instr.result}")

            elif instr.op == 'ifFalse':
                self.emit(f"CMP {instr.arg1}, 0")
                self.emit(f"JE {instr.result}")

            elif instr.op == 'label':
                self.emit(f"{instr.result}:")

    def emit(self, instruction):
        """生成一条机器指令"""
        self.code.append(instruction)
```

### 8.3 寄存器分配

#### 8.3.1 寄存器分配的挑战

- 寄存器数量有限
- 需要处理寄存器溢出（spilling）
- 需要考虑寄存器的特殊用途（如栈指针、返回值寄存器）

#### 8.3.2 图着色算法

将寄存器分配问题转化为图着色问题：

- 节点：变量
- 边：同时活跃的变量之间连边
- 着色：为每个节点分配颜色（寄存器）

#### 8.3.3 活跃区间分析

确定每个变量的活跃区间（从定义到最后一次使用）

#### 8.3.4 线性扫描寄存器分配

**优点：** 编译速度快，适用于 JIT 编译器

**算法：**

```python
def linear_scan_allocation(intervals, num_registers):
    """线性扫描寄存器分配"""
    # intervals: [(变量, 开始位置, 结束位置)]
    intervals.sort(key=lambda x: x[1])  # 按开始位置排序
    
    active = []  # 活跃的区间
    allocation = {}
    free_registers = list(range(num_registers))
    
    for var, start, end in intervals:
        # 释放已结束的区间占用的寄存器
        active = [(v, s, e, r) for v, s, e, r in active if e > start]
        for v, s, e, r in active:
            if e <= start:
                free_registers.append(r)
        
        # 分配寄存器
        if free_registers:
            reg = free_registers.pop(0)
            allocation[var] = f'R{reg}'
            active.append((var, start, end, reg))
        else:
            # 溢出到内存
            allocation[var] = 'MEMORY'
    
    return allocation
python

8.4 指令调度

8.4.1 指令调度的目的

现代处理器特性：
流水线（Pipeline）
超标量（Superscalar）
乱序执行（Out-of-Order Execution）

目标：
减少流水线停顿
隐藏内存访问延迟
最大化指令级并行

8.4.2 列表调度算法（List Scheduling）


					
class InstructionScheduler:
    def __init__(self):

				
8.5 完整的代码生成示例

8.5.1 生成 x86-64 汇编代码


					
class X86CodeGenerator:
    def __init__(self):

				
8.5.2 完整编译流程示例


					
def compile_program(source_code):
    """完整的编译流程"""
```

---

## 第九章：运行时环境

### 9.1 内存组织

#### 9.1.1 典型的内存布局

```text
高地址
┌─────────────┐
│  命令行参数  │
│  环境变量    │
├─────────────┤
│    栈区     │  ← 向下增长
│     ↓       │
│             │
│   (空闲)    │
│             │
│     ↑       │
│    堆区     │  ← 向上增长
├─────────────┤
│   BSS 段    │  未初始化全局变量
├─────────────┤
│   数据段    │  已初始化全局变量
├─────────────┤
│   代码段    │  程序指令
└─────────────┘
低地址
```

### 9.2 活动记录（Activation Record）

#### 9.2.1 栈帧结构

```text
高地址
┌─────────────────┐
│   实际参数 n    │
│      ...        │
│   实际参数 1    │
├─────────────────┤
│   返回地址      │
├─────────────────┤ ← 当前 rbp
│  保存的 rbp     │
├─────────────────┤
│   局部变量 1    │
│      ...        │
│   局部变量 n    │
├─────────────────┤
│   临时变量      │
├─────────────────┤ ← 当前 rsp
低地址
```

#### 9.2.2 函数调用约定

**x86-64 System V ABI 调用约定：**

```python
class CallingConvention:
    """x86-64 调用约定"""

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
        self.caller_saved = ['rax', 'rcx', 'rdx', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11']

    def allocate_parameters(self, params):
        """分配参数到寄存器或栈"""
        allocations = []
        int_reg_idx = 0
        float_reg_idx = 0
        stack_offset = 0

        for param in params:
            if param.type == 'int' and int_reg_idx < len(self.int_param_regs):
                allocations.append((param.name, self.int_param_regs[int_reg_idx]))
                int_reg_idx += 1
            elif param.type == 'float' and float_reg_idx < len(self.float_param_regs):
                allocations.append((param.name, self.float_param_regs[float_reg_idx]))
                float_reg_idx += 1
            else:
                # 参数放在栈上
                allocations.append((param.name, f'[rbp+{stack_offset + 16}]'))
                stack_offset += 8

        return allocations
```

### 9.3 参数传递

#### 9.3.1 参数传递方式

**按值传递（Call by Value）：**

```c
void increment(int x) {
    x = x + 1;  // 不影响调用者
}

int main() {
    int a = 5;
    increment(a);  // a 仍然是 5
}
```

**按引用传递（Call by Reference）：**

```c
void increment(int *x) {
    *x = *x + 1;  // 影响调用者
}

int main() {
    int a = 5;
    increment(&a);  // a 变成 6
}
```

### 9.4 堆管理

#### 9.4.1 动态内存分配

```python
class HeapManager:
    """简单的堆管理器"""

    def __init__(self, heap_size):
        self.heap = bytearray(heap_size)
        self.free_list = [(0, heap_size)]  # (起始地址, 大小)

    def malloc(self, size):
        """分配内存"""
        # 首次适配算法
        for i, (start, block_size) in enumerate(self.free_list):
            if block_size >= size:
                # 分配内存
                self.free_list.pop(i)

                # 如果有剩余空间，加回空闲列表
                if block_size > size:
                    self.free_list.insert(i, (start + size, block_size - size))

                return start

        # 内存不足
        raise MemoryError("Out of memory")

    def free(self, address, size):
        """释放内存"""
        # 将释放的块加入空闲列表
        self.free_list.append((address, size))

        # 合并相邻的空闲块
        self.coalesce()

    def coalesce(self):
        """合并相邻的空闲块"""
        self.free_list.sort()

        i = 0
        while i < len(self.free_list) - 1:
            start1, size1 = self.free_list[i]
            start2, size2 = self.free_list[i + 1]

            if start1 + size1 == start2:
                # 合并
                self.free_list[i] = (start1, size1 + size2)
                self.free_list.pop(i + 1)
            else:
                i += 1
```

### 9.5 垃圾回收

#### 9.5.1 标记-清除算法（Mark-Sweep）

```python
class GarbageCollector:
    def __init__(self):
        self.objects = {}  # 所有对象
        self.roots = set()  # 根对象

    def collect(self):
        """执行垃圾回收"""
        # 标记阶段
        marked = set()
        self.mark(self.roots, marked)

        # 清除阶段
        to_delete = []
        for obj_id in self.objects:
            if obj_id not in marked:
                to_delete.append(obj_id)

        for obj_id in to_delete:
            del self.objects[obj_id]

    def mark(self, objects, marked):
        """标记可达对象"""
        for obj in objects:
            if obj not in marked:
                marked.add(obj)
                # 递归标记引用的对象
                if obj in self.objects:
                    references = self.objects[obj].get_references()
                    self.mark(references, marked)
```

---

## 第十章：现代编译技术

### 10.1 即时编译（JIT Compilation）

#### 10.1.1 JIT 编译的优势

**解释执行 vs JIT 编译：**

- **解释执行：** 启动快，执行慢
- **JIT 编译：** 编译开销，但执行快
- **混合模式：** 先解释，热点代码 JIT 编译

#### 10.1.2 JIT 编译示例

```python
class JITCompiler:
    def __init__(self):
        self.code_cache = {}
        self.execution_count = {}
        self.JIT_THRESHOLD = 10  # 执行 10 次后编译

    def execute(self, function):
        """执行或编译函数"""
        # 增加执行计数
        if function not in self.execution_count:
            self.execution_count[function] = 0
        self.execution_count[function] += 1

        # 检查是否应该编译
        if self.execution_count[function] >= self.JIT_THRESHOLD:
            if function not in self.code_cache:
                # 编译函数
                compiled = self.compile(function)
                self.code_cache[function] = compiled

            # 执行编译后的代码
            return self.code_cache[function]()
        else:
            # 解释执行
            return self.interpret(function)

    def compile(self, function):
        """将函数编译成机器码"""
        # 实际实现会生成机器码
        # 这里简化处理
        return lambda: function()

    def interpret(self, function):
        """解释执行函数"""
        return function()
```

### 10.2 多阶段编译（Multi-tier Compilation）

**示例：Java HotSpot VM**

```text
Java 源码
    ↓
字节码 (javac)
    ↓
解释执行 (初期)
    ↓
C1 编译器 (客户端编译器，快速编译)
    ↓
C2 编译器 (服务器编译器，优化编译)
```

### 10.3 LLVM 架构

#### 10.3.1 LLVM 编译流程

```text
源语言前端 (Clang, Swift, Rust)
    ↓
LLVM IR (中间表示)
    ↓
LLVM 优化器 (opt)
    ↓
LLVM 后端
    ↓
目标代码
(x86, ARM, RISC-V, etc.)
```

#### 10.3.2 LLVM IR 示例

**简单的 C 程序：**

```c
int add(int a, int b) {
    return a + b;
}
```

**对应的 LLVM IR：**

```llvm
define i32 @add(i32 %a, i32 %b) {
entry:
  %sum = add i32 %a, %b
  ret i32 %sum
}
```

**更复杂的例子：**

```c
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

**LLVM IR：**

```llvm
define i32 @factorial(i32 %n) {
entry:
  %cmp = icmp sle i32 %n, 1
  br i1 %cmp, label %if.then, label %if.else

if.then:
  ret i32 1

if.else:
  %sub = sub i32 %n, 1
  %call = call i32 @factorial(i32 %sub)
  %mul = mul i32 %n, %call
  ret i32 %mul
}
```

### 10.4 向量化（Vectorization）

#### 10.4.1 SIMD 指令

**单指令多数据（SIMD）：**

```c
// 标量版本
for (int i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
}

// 向量化版本（概念）
for (int i = 0; i < n; i += 4) {
    // 一次处理 4 个元素
    vec4 va = load_vec4(&a[i]);
    vec4 vb = load_vec4(&b[i]);
    vec4 vc = vec_add(va, vb);
    store_vec4(&c[i], vc);
}
```

#### 10.4.2 自动向量化

```python
class AutoVectorizer:
    def __init__(self):
        self.vector_width = 4  # SIMD 宽度

    def vectorize_loop(self, loop):
        """自动向量化循环"""
        # 检查循环是否可向量化
        if not self.is_vectorizable(loop):
            return loop

        # 生成向量化代码
        vectorized_code = []

        # 向量化主体
        iterations = loop.iterations // self.vector_width
        for i in range(iterations):
            vectorized_code.append(
                f"vec_op({i * self.vector_width}, {self.vector_width})"
            )

        # 处理剩余迭代
        remainder = loop.iterations % self.vector_width
        for i in range(remainder):
            vectorized_code.append(
                f"scalar_op({iterations * self.vector_width + i})"
            )

        return vectorized_code

    def is_vectorizable(self, loop):
        """检查循环是否可向量化"""
        # 检查数据依赖、内存访问模式等
        return True  # 简化处理
```

### 10.5 多线程和并行编译

#### 10.5.1 并行编译策略

**文件级并行：**

```python
import multiprocessing

def parallel_compile(source_files):
    """并行编译多个源文件"""
    with multiprocessing.Pool() as pool:
        object_files = pool.map(compile_single_file, source_files)

    # 链接所有目标文件
    link(object_files)

    return object_files
```

#### 10.5.2 函数级并行

```python
from concurrent.futures import ThreadPoolExecutor

class ParallelCompiler:
    def __init__(self):
        self.executor = ThreadPoolExecutor()

    def compile_program(self, program):
        """并行编译程序中的函数"""
        futures = []

        for function in program.functions:
            future = self.executor.submit(self.compile_function, function)
            futures.append(future)

        # 等待所有函数编译完成
        compiled_functions = [f.result() for f in futures]

        return self.link_functions(compiled_functions)
```

### 10.6 增量编译（Incremental Compilation）

#### 10.6.1 依赖跟踪

```python
class IncrementalCompiler:
    def __init__(self):
        self.dependency_graph = {}
        self.timestamps = {}

    def build(self, target):
        """增量构建目标"""
        # 检查依赖是否需要重新编译
        if self.needs_rebuild(target):
            # 先构建依赖
            for dep in self.dependency_graph.get(target, []):
                self.build(dep)

            # 编译目标
            self.compile(target)
            self.timestamps[target] = time.time()

    def needs_rebuild(self, target):
        """检查是否需要重新构建"""
        if target not in self.timestamps:
            return True

        target_time = self.timestamps[target]

        # 检查依赖是否更新
        for dep in self.dependency_graph.get(target, []):
            if dep in self.timestamps:
                if self.timestamps[dep] > target_time:
                    return True

        return False
```

### 10.7 链接时优化（LTO）

#### 10.7.1 全程序优化

```python
class LinkTimeOptimizer:
    def __init__(self):
        self.modules = []

    def optimize(self, object_files):
        """链接时优化"""
        # 1. 加载所有模块的 IR
        for obj_file in object_files:
            ir = self.load_ir(obj_file)
            self.modules.append(ir)

        # 2. 全程序分析
        call_graph = self.build_call_graph(self.modules)

        # 3. 跨模块优化
        self.inline_across_modules(call_graph)
        self.dead_code_elimination_global()

        # 4. 生成最终代码
        return self.generate_code(self.modules)

    def inline_across_modules(self, call_graph):
        """跨模块内联"""
        for caller, callees in call_graph.items():
            for callee in callees:
                if self.should_inline(callee):
                    self.inline_function(caller, callee)
```

### 10.8 配置文件引导优化（PGO）

#### 10.8.1 PGO 工作流程

```text
1. 插桩编译
源代码 → 编译器（插入性能计数器）→ 可执行文件（带插桩）

2. 运行程序收集数据
可执行文件（带插桩）→ 运行 → 生成配置文件（.profdata）

3. 优化编译
源代码 + 配置文件 → 编译器（基于配置优化）→ 优化的可执行文件
```

#### 10.8.2 PGO 实现示例

```python
class ProfileGuidedOptimizer:
    def __init__(self):
        self.profile_data = {}

    def instrument_code(self, code):
        """插入性能计数器"""
        instrumented = []

        for block in code.basic_blocks:
            # 在每个基本块开始插入计数器
            instrumented.append(f"increment_counter({block.id})")
            instrumented.extend(block.instructions)

        return instrumented

    def optimize_with_profile(self, code, profile_file):
        """基于配置文件优化"""
        # 加载配置数据
        self.profile_data = self.load_profile(profile_file)

        # 识别热点代码
        hot_blocks = self.identify_hot_blocks()

        # 针对热点优化
        for block in hot_blocks:
            self.aggressive_optimize(block)

        # 冷代码优化（优化代码大小）
        cold_blocks = self.identify_cold_blocks()
        for block in cold_blocks:
            self.optimize_for_size(block)
```

---

## 第十一章：特定领域编译技术

### 11.1 领域特定语言（DSL）

#### 11.1.1 DSL 编译器设计

**示例：简单的 SQL 编译器**

```python
class SQLCompiler:
    def __init__(self):
        self.query_plan = None

    def compile(self, sql_query):
        """编译 SQL 查询"""
        # 1. 解析 SQL
        ast = self.parse_sql(sql_query)

        # 2. 查询优化
        optimized_plan = self.optimize_query(ast)

        # 3. 生成执行计划
        execution_plan = self.generate_plan(optimized_plan)

        return execution_plan

    def optimize_query(self, ast):
        """查询优化"""
        # 谓词下推
        ast = self.push_down_predicates(ast)

        # 连接重排序
        ast = self.reorder_joins(ast)

        # 选择索引
        ast = self.select_indexes(ast)

        return ast
```

### 11.2 神经网络编译器

#### 11.2.1 计算图优化

```python
class NeuralNetworkCompiler:
    def __init__(self):
        self.graph = None

    def compile(self, model):
        """编译神经网络模型"""
        # 1. 构建计算图
        self.graph = self.build_graph(model)

        # 2. 图优化
        self.graph = self.optimize_graph(self.graph)

        # 3. 算子融合
        self.graph = self.fuse_operators(self.graph)

        # 4. 内存优化
        self.graph = self.optimize_memory(self.graph)

        # 5. 生成代码
        return self.generate_code(self.graph)

    def fuse_operators(self, graph):
        """算子融合"""
        # 融合 Conv + BatchNorm + ReLU
        for node in graph.nodes:
            if node.op == 'Conv':
                next_node = node.next
                if next_node and next_node.op == 'BatchNorm':
                    relu_node = next_node.next
                    if relu_node and relu_node.op == 'ReLU':
                        # 融合三个算子
                        fused = FusedNode('Conv-BN-ReLU', [node, next_node, relu_node])
                        graph.replace_nodes([node, next_node, relu_node], fused)

        return graph
```

### 11.3 正则表达式编译

#### 11.3.1 正则表达式到 NFA/DFA

```python
class RegexCompiler:
    def __init__(self):
        self.nfa = None
        self.dfa = None

    def compile(self, regex):
        """编译正则表达式"""
        # 1. 解析正则表达式
        ast = self.parse_regex(regex)

        # 2. 构造 NFA
        self.nfa = self.regex_to_nfa(ast)

        # 3. NFA 转 DFA
        self.dfa = self.nfa_to_dfa(self.nfa)

        # 4. DFA 最小化
        self.dfa = self.minimize_dfa(self.dfa)

        # 5. 生成匹配代码
        return self.generate_matcher(self.dfa)

    def regex_to_nfa(self, ast):
        """Thompson 构造法"""
        if ast.type == 'char':
            return self.char_nfa(ast.value)
        elif ast.type == 'concat':
            return self.concat_nfa(ast.left, ast.right)
        elif ast.type == 'union':
            return self.union_nfa(ast.left, ast.right)
        elif ast.type == 'star':
            return self.star_nfa(ast.child)
```

---

## 第十二章：编译器测试与调试

### 12.1 编译器测试策略

#### 12.1.1 单元测试

```python
import unittest

class LexerTests(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()

    def test_tokenize_numbers(self):
        """测试数字词法分析"""
        tokens = self.lexer.tokenize("123 456")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, 'NUMBER')
        self.assertEqual(tokens[0].value, 123)

    def test_tokenize_identifiers(self):
        """测试标识符词法分析"""
        tokens = self.lexer.tokenize("foo bar")
        self.assertEqual(tokens[0].type, 'IDENTIFIER')
        self.assertEqual(tokens[0].value, 'foo')

    def test_tokenize_keywords(self):
        """测试关键字识别"""
        tokens = self.lexer.tokenize("if while")
        self.assertEqual(tokens[0].type, 'IF')
        self.assertEqual(tokens[1].type, 'WHILE')

class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_expression(self):
        """测试表达式解析"""
        ast = self.parser.parse("1 + 2 * 3")
        self.assertEqual(ast.op, '+')
        self.assertEqual(ast.right.op, '*')
```

#### 12.1.2 端到端测试

```python
class EndToEndTests(unittest.TestCase):
    def test_compile_and_run(self):
        """编译并运行程序"""
        source = """
        int main() {
            int a = 5;
            int b = 10;
            return a + b;
        }
        """

        # 编译
        executable = self.compiler.compile(source)

        # 运行
        result = self.run_executable(executable)

        # 验证结果
        self.assertEqual(result, 15)

    def test_fibonacci(self):
        """测试斐波那契数列程序"""
        source = """
        int fib(int n) {
            if (n <= 1) return n;
            return fib(n-1) + fib(n-2);
        }

        int main() {
            return fib(10);
        }
        """

        executable = self.compiler.compile(source)
        result = self.run_executable(executable)

        self.assertEqual(result, 55)
```

#### 12.1.3 差分测试（Differential Testing）

```python
class DifferentialTester:
    def __init__(self, compilers):
        self.compilers = compilers  # 多个编译器

    def test(self, source_code):
        """对比多个编译器的输出"""
        results = []

        for compiler in self.compilers:
            try:
                executable = compiler.compile(source_code)
                output = self.run(executable)
                results.append((compiler.name, output))
            except Exception as e:
                results.append((compiler.name, f"Error: {e}"))

        # 检查所有输出是否一致
        outputs = [r[1] for r in results]
        if len(set(outputs)) > 1:
            print(f"Discrepancy found!")
            for name, output in results:
                print(f"{name}: {output}")
            return False

        return True
```

### 12.2 模糊测试（Fuzz Testing）

```python
import random
import string

class CompilerFuzzer:
    def __init__(self, compiler):
        self.compiler = compiler

    def generate_random_program(self):
        """生成随机程序"""
        program = "int main() {\n"

        # 随机生成变量声明
        num_vars = random.randint(1, 5)
        for i in range(num_vars):
            program += f"    int var{i} = {random.randint(0, 100)};\n"

        # 随机生成表达式
        num_exprs = random.randint(1, 10)
        for i in range(num_exprs):
            var1 = f"var{random.randint(0, num_vars-1)}"
            var2 = f"var{random.randint(0, num_vars-1)}"
            op = random.choice(['+', '-', '*', '/'])
            program += f"    int result{i} = {var1} {op} {var2};\n"

        program += "    return 0;\n}\n"
        return program

    def fuzz(self, iterations=1000):
        """模糊测试"""
        crashes = []

        for i in range(iterations):
            program = self.generate_random_program()

            try:
                self.compiler.compile(program)
            except Exception as e:
                # 发现崩溃
                crashes.append((program, str(e)))
                print(f"Crash found in iteration {i}")

        return crashes
```

### 12.3 性能测试

#### 12.3.1 编译时间测试

```python
import time

class PerformanceTester:
    def __init__(self, compiler):
        self.compiler = compiler

    def benchmark_compile_time(self, source_files):
        """测试编译时间"""
        results = {}

        for source_file in source_files:
            with open(source_file) as f:
                source = f.read()

            start_time = time.time()
            self.compiler.compile(source)
            end_time = time.time()

            compile_time = end_time - start_time
            results[source_file] = compile_time

            print(f"{source_file}: {compile_time:.3f}s")

        return results

    def benchmark_generated_code(self, source):
        """测试生成代码的性能"""
        executable = self.compiler.compile(source)

        start_time = time.time()
        for _ in range(1000):
            self.run(executable)
        end_time = time.time()

        avg_time = (end_time - start_time) / 1000
        print(f"Average execution time: {avg_time:.6f}s")

        return avg_time
```

### 12.4 调试技术

#### 12.4.1 编译器调试输出

```python
class DebugCompiler:
    def __init__(self):
        self.debug_mode = True

    def compile(self, source):
        """带调试输出的编译"""
        if self.debug_mode:
            print("=== Lexical Analysis ===")
        tokens = self.lexer.tokenize(source)
        if self.debug_mode:
            print(f"Tokens: {tokens}")

        if self.debug_mode:
            print("\n=== Syntax Analysis ===")
        ast = self.parser.parse(tokens)
        if self.debug_mode:
            print(f"AST: {ast}")

        if self.debug_mode:
            print("\n=== Semantic Analysis ===")
        self.semantic_analyzer.analyze(ast)

        if self.debug_mode:
            print("\n=== Code Generation ===")
        code = self.code_generator.generate(ast)
        if self.debug_mode:
            print(f"Generated code:\n{code}")

        return code
```

---

## 总结

本文档全面介绍了编译原理的核心概念和实现技术，涵盖了从词法分析到代码生成的完整编译流程，以及现代编译器的高级优化技术。通过大量的代码示例和实践案例，帮助读者深入理解编译器的工作原理。

### 关键要点

1. **编译器结构：** 前端（词法、语法、语义分析）→ 中间表示 → 后端（优化、代码生成）
2. **优化技术：** 数据流分析、常量折叠、死代码删除、循环优化等
3. **现代技术：** JIT 编译、LLVM、向量化、并行编译
4. **测试方法：** 单元测试、端到端测试、模糊测试、差分测试

### 进一步学习

- 阅读经典教材：《编译原理》（龙书）、《现代编译原理》（虎书）
- 实践项目：实现一个简单的编译器
- 研究开源编译器：GCC、Clang/LLVM、V8
- 探索领域特定编译器：TensorFlow XLA、PyTorch JIT

---

**文档版本：** v2.0
**最后更新：** 2025-11-01
**作者：** SAST C++ 课程组
