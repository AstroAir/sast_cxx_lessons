# 曼波带你速通C++

## 目录

1. [C++基础](#第1章-c基础)
2. [输入输出](#第2章-输入输出操作)
3. [变量和运算符](#第3章-变量和运算符)
4. [字符串](#第4章-字符串处理)
5. [控制流](#第5章-控制流)
6. [函数](#第6章-函数)
7. [数组和集合](#第7章-数组和集合)
8. [引用](#第8章-引用)
9. [指针](#第9章-指针简介)
10. [类和对象](#第10章-类和对象简介)
11. [构造和析构](#第11章-构造函数和析构函数)
12. [拷贝语义](#第12章-拷贝语义)
13. [动态内存](#第13章-动态内存管理)
14. [类型转换](#第14章-类型转换)
15. [内联函数](#第15章-内联函数)
16. [Lambda表达式](#第16章-lambda表达式)
17. [左值和右值](#第17章-左值和右值)

---

## 第1章 C++基础

### 1.1 你的第一个C++程序

每个C++程序都从一个简单的结构开始。C++是一种编译型语言，这意味着你编写的源代码需要先被编译器转换成机器代码，然后才能在计算机上运行。让我们从经典的"Hello, World!"程序开始，这是学习任何编程语言的传统第一步。

**完整的Hello World程序：**

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

**程序结构详解：**

| 代码行 | 说明 |
|------|------|
| `#include <iostream>` | 预处理器指令，包含输入/输出流库。这个库提供了cout和cin等对象 |
| `int main()` | 程序的入口点（执行从这里开始）。操作系统调用这个函数来运行你的程序 |
| `std::cout << "Hello, World!"` | 向控制台输出文本。cout是"字符输出"的缩写，<<是流插入运算符 |
| `std::endl` | 输出换行符并刷新缓冲区。也可以使用"\n"来换行 |
| `return 0;` | 表示程序成功完成。返回0告诉操作系统程序正常结束，非零值表示错误 |

**关键概念**：

- 每个C++程序必须有且仅有一个`main()`函数。这是程序执行的起点
- `#include`指令告诉预处理器在编译前将指定的头文件内容插入到当前文件中
- `std::`是命名空间前缀，表示cout来自标准库（standard library）
- 每条语句以分号`;`结束
- 花括号`{}`定义了代码块的范围

**更详细的示例程序：**

```cpp
#include <iostream>  // 包含输入输出流库

// 这是程序的主函数，程序从这里开始执行
int main() {
    // 输出欢迎信息
    std::cout << "欢迎来到C++世界！" << std::endl;

    // 可以连续输出多行
    std::cout << "这是第二行" << std::endl;
    std::cout << "这是第三行" << std::endl;

    // 也可以在一行中输出多个内容
    std::cout << "数字: " << 42 << ", 文本: " << "C++" << std::endl;

    // 返回0表示程序成功执行
    return 0;
}
```

**预期输出：**

```txt
欢迎来到C++世界！
这是第二行
这是第三行
数字: 42, 文本: C++
```

### 1.2 编译和运行

C++是编译型语言，源代码需要经过编译才能运行。编译过程将人类可读的C++代码转换为计算机可以执行的机器代码。

**编译过程的四个阶段：**

1. **预处理**：处理#include、#define等预处理指令
2. **编译**：将C++代码转换为汇编代码
3. **汇编**：将汇编代码转换为机器代码（目标文件）
4. **链接**：将多个目标文件和库文件链接成可执行文件

**使用g++编译器（Linux/Mac/Windows with MinGW）：**

```bash
# 基本编译命令
g++ -o hello hello.cpp

# 运行程序
./hello          # Linux/Mac
hello.exe        # Windows

# 带优化和警告的编译（推荐）
g++ -Wall -Wextra -std=c++17 -o hello hello.cpp

# 编译多个源文件
g++ -o program main.cpp utils.cpp helper.cpp
```

**使用clang++编译器（跨平台）：**

```bash
clang++ -o hello hello.cpp
./hello
```

**使用Visual Studio（Windows）：**

1. 打开Visual Studio
2. 创建新项目 → 选择"控制台应用程序"
3. 用你的程序代码替换现有代码
4. 按Ctrl+F5运行（不调试）或F5运行（调试模式）

**使用Visual Studio Code（跨平台）：**

1. 安装C++扩展
2. 创建.cpp文件
3. 配置tasks.json和launch.json
4. 按F5运行

**常见编译错误及解决方法：**

```cpp
// 错误示例1：缺少分号
#include <iostream>

int main() {
    std::cout << "Hello"  // 错误：缺少分号
    return 0;
}
// 解决：在语句末尾添加分号

// 错误示例2：拼写错误
#include <iostream>

int main() {
    std::cuot << "Hello" << std::endl;  // 错误：cout拼写错误
    return 0;
}
// 解决：改为std::cout

// 正确的程序
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### 1.3 基本数据类型

C++是一种强类型语言，这意味着每个变量都必须有明确的类型。C++提供了多种基本数据类型用于存储不同类型的信息。选择正确的数据类型对于程序的效率和正确性至关重要。

**基本数据类型详解：**

| 类型 | 大小 | 范围 | 用途 | 示例 |
|------|------|------|------|------|
| `int` | 4字节 | -2,147,483,648 到 2,147,483,647 | 整数 | `int age = 25;` |
| `short` | 2字节 | -32,768 到 32,767 | 小整数 | `short year = 2024;` |
| `long` | 4/8字节 | 取决于系统 | 大整数 | `long population = 1000000L;` |
| `long long` | 8字节 | ±9,223,372,036,854,775,807 | 超大整数 | `long long distance = 9999999999LL;` |
| `float` | 4字节 | ±3.4e±38（约7位精度） | 单精度浮点数 | `float height = 5.9f;` |
| `double` | 8字节 | ±1.7e±308（约15位精度） | 双精度浮点数 | `double pi = 3.14159265359;` |
| `char` | 1字节 | -128 到 127 或 0 到 255 | 单个字符 | `char grade = 'A';` |
| `bool` | 1字节 | true 或 false | 布尔值 | `bool isStudent = true;` |
| `std::string` | 可变 | 任意文本 | 字符串 | `std::string name = "Alice";` |

**完整示例程序 - 展示所有基本类型：**

```cpp
#include <iostream>
#include <string>

int main() {
    // 整数类型
    int age = 25;                    // 标准整数
    short year = 2024;               // 短整数
    long population = 8000000000L;   // 长整数（注意L后缀）
    long long bigNumber = 9999999999999LL;  // 超长整数（注意LL后缀）

    // 浮点类型
    float height = 5.9f;             // 单精度（注意f后缀）
    double pi = 3.14159265359;       // 双精度

    // 字符和布尔类型
    char grade = 'A';                // 单个字符（用单引号）
    bool isStudent = true;           // 布尔值

    // 字符串类型（需要#include <string>）
    std::string name = "Alice";      // 字符串（用双引号）

    // 输出所有变量
    std::cout << "=== 基本数据类型示例 ===" << std::endl;
    std::cout << "姓名: " << name << std::endl;
    std::cout << "年龄: " << age << std::endl;
    std::cout << "年份: " << year << std::endl;
    std::cout << "人口: " << population << std::endl;
    std::cout << "大数字: " << bigNumber << std::endl;
    std::cout << "身高: " << height << " 英尺" << std::endl;
    std::cout << "圆周率: " << pi << std::endl;
    std::cout << "成绩等级: " << grade << std::endl;
    std::cout << "是学生: " << (isStudent ? "是" : "否") << std::endl;

    // 显示数据类型的大小
    std::cout << "\n=== 数据类型大小（字节） ===" << std::endl;
    std::cout << "int: " << sizeof(int) << " 字节" << std::endl;
    std::cout << "short: " << sizeof(short) << " 字节" << std::endl;
    std::cout << "long: " << sizeof(long) << " 字节" << std::endl;
    std::cout << "long long: " << sizeof(long long) << " 字节" << std::endl;
    std::cout << "float: " << sizeof(float) << " 字节" << std::endl;
    std::cout << "double: " << sizeof(double) << " 字节" << std::endl;
    std::cout << "char: " << sizeof(char) << " 字节" << std::endl;
    std::cout << "bool: " << sizeof(bool) << " 字节" << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 基本数据类型示例 ===
姓名: Alice
年龄: 25
年份: 2024
人口: 800000000
大数字: 9999999999999
身高: 5.9 英尺
圆周率: 3.14159
成绩等级: A
是学生: 是

=== 数据类型大小（字节） ===
int: 4 字节
short: 2 字节
long: 4 字节
long long: 8 字节
float: 4 字节
double: 8 字节
char: 1 字节
bool: 1 字节
```

**重要提示：**

- 整数字面量默认是`int`类型，使用`L`后缀表示`long`，`LL`表示`long long`
- 浮点字面量默认是`double`类型，使用`f`后缀表示`float`
- 字符用单引号`'A'`，字符串用双引号`"Hello"`
- `sizeof()`运算符返回类型或变量占用的字节数

### 1.4 注释和命名空间

#### 1.4.1 注释

注释是程序中不会被编译器执行的文本，用于解释代码的功能和逻辑。良好的注释习惯能让代码更易于理解和维护。

**单行注释：**

```cpp
// 这是单行注释，从//开始到行尾都是注释
int x = 10;  // 可以在代码后面添加注释

// 单行注释常用于简短说明
int age = 25;  // 用户年龄
```

**多行注释：**

```cpp
/* 这是多行注释
   可以跨越多行
   用于更详细的说明
   常用于函数或类的文档说明 */

/*
 * 这种格式更美观
 * 每行开头加星号
 * 便于阅读
 */
```

**完整示例 - 注释的使用：**

```cpp
#include <iostream>

/*
 * 程序功能：演示注释的使用
 * 作者：学习者
 * 日期：2024-10-31
 */

int main() {
    // 声明并初始化变量
    int score = 95;  // 学生分数

    /*
     * 根据分数判断等级
     * 90-100: A
     * 80-89: B
     * 其他: C
     */
    if (score >= 90) {
        std::cout << "等级: A" << std::endl;  // 优秀
    } else if (score >= 80) {
        std::cout << "等级: B" << std::endl;  // 良好
    } else {
        std::cout << "等级: C" << std::endl;  // 及格
    }

    // 程序结束
    return 0;
}
```

**注释最佳实践：**

- ✅ 解释"为什么"而不是"是什么"
- ✅ 在复杂逻辑前添加注释
- ✅ 保持注释与代码同步更新
- ❌ 不要注释显而易见的代码
- ❌ 不要用注释替代清晰的代码

#### 1.4.2 命名空间

命名空间（namespace）用于组织代码，避免名称冲突。C++标准库的所有内容都在`std`命名空间中。

**方法1：使用std::前缀（推荐）**

```cpp
#include <iostream>

int main() {
    std::cout << "Hello" << std::endl;  // 明确指定使用std命名空间的cout
    return 0;
}
```

**优点：** 代码清晰，不会产生命名冲突

**方法2：使用using声明**

```cpp
#include <iostream>

using std::cout;  // 只引入cout
using std::endl;  // 只引入endl

int main() {
    cout << "Hello" << endl;  // 可以直接使用cout和endl
    return 0;
}
```

**优点：** 选择性引入，相对安全

**方法3：using namespace（不推荐用于大型项目）**

```cpp
#include <iostream>

using namespace std;  // 引入整个std命名空间

int main() {
    cout << "Hello" << endl;  // 可以直接使用所有std内容
    return 0;
}
```

**缺点：** 可能导致命名冲突

**完整示例 - 命名空间的使用：**

```cpp
#include <iostream>
#include <string>

// 方法1：使用std::前缀（最安全）
void method1() {
    std::cout << "方法1：使用std::前缀" << std::endl;
    std::string name = "Alice";
    std::cout << "姓名: " << name << std::endl;
}

// 方法2：使用using声明
void method2() {
    using std::cout;
    using std::endl;
    using std::string;

    cout << "方法2：使用using声明" << endl;
    string name = "Bob";
    cout << "姓名: " << name << endl;
}

// 方法3：using namespace（仅在小程序中使用）
void method3() {
    using namespace std;

    cout << "方法3：using namespace" << endl;
    string name = "Charlie";
    cout << "姓名: " << name << endl;
}

int main() {
    method1();
    std::cout << std::endl;

    method2();
    std::cout << std::endl;

    method3();

    return 0;
}
```

**预期输出：**

```
方法1：使用std::前缀
姓名: Alice

方法2：使用using声明
姓名: Bob

方法3：using namespace
姓名: Charlie
```

**最佳实践：**

- 对于初学者和小程序，使用方法1（`std::`前缀）最安全
- 在函数内部可以使用`using`声明
- 避免在头文件中使用`using namespace`
- 大型项目中坚持使用`std::`前缀

---

## 第2章 输入输出操作

C++使用流（stream）进行输入输出操作。主要的流包括cin（输入）、cout（输出）和文件流。

### 2.1 基本输入输出

**完整示例 - 基本输入输出：**

```cpp
#include <iostream>
#include <string>

int main() {
    std::cout << "=== 基本输入输出示例 ===" << std::endl;

    // 输出
    std::cout << "Hello, World!" << std::endl;
    std::cout << "我的第一个C++程序" << std::endl;

    // 输入
    std::string name;
    int age;

    std::cout << "\n请输入你的名字: ";
    std::cin >> name;

    std::cout << "请输入你的年龄: ";
    std::cin >> age;

    // 输出结果
    std::cout << "\n你好, " << name << "!" << std::endl;
    std::cout << "你今年 " << age << " 岁" << std::endl;

    // 多个值的输入输出
    int a, b, c;
    std::cout << "\n请输入三个整数（用空格分隔）: ";
    std::cin >> a >> b >> c;
    std::cout << "你输入的数字是: " << a << ", " << b << ", " << c << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 基本输入输出示例 ===
Hello, World!
我的第一个C++程序

请输入你的名字: Alice
请输入你的年龄: 25

你好, Alice!
你今年 25 岁

请输入三个整数（用空格分隔）: 10 20 30
你输入的数字是: 10, 20, 30
```

### 2.2 格式化输出

**完整示例 - 格式化输出：**

```cpp
#include <iostream>
#include <iomanip>  // 用于格式化

int main() {
    std::cout << "=== 格式化输出示例 ===" << std::endl;

    // 设置精度
    double pi = 3.14159265359;
    std::cout << "默认精度: " << pi << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "保留2位小数: " << pi << std::endl;
    std::cout << std::setprecision(5);
    std::cout << "保留5位小数: " << pi << std::endl;

    // 设置宽度和对齐
    std::cout << "\n表格输出:" << std::endl;
    std::cout << std::setw(10) << "姓名" << std::setw(10) << "年龄" << std::setw(15) << "分数" << std::endl;
    std::cout << std::setw(10) << "Alice" << std::setw(10) << 25 << std::setw(15) << 95.5 << std::endl;
    std::cout << std::setw(10) << "Bob" << std::setw(10) << 30 << std::setw(15) << 87.3 << std::endl;

    // 进制转换
    int num = 255;
    std::cout << "\n进制转换:" << std::endl;
    std::cout << "十进制: " << std::dec << num << std::endl;
    std::cout << "十六进制: " << std::hex << num << std::endl;
    std::cout << "八进制: " << std::oct << num << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 格式化输出示例 ===
默认精度: 3.14159
保留2位小数: 3.14
保留5位小数: 3.14159

表格输出:
      姓名      年龄           分数
     Alice        25          95.50
       Bob        30          87.30

进制转换:
十进制: 255
十六进制: ff
八进制: 377
```

### 2.3 文件输入输出

**完整示例 - 文件操作：**

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::cout << "=== 文件输入输出示例 ===" << std::endl;

    // 写入文件
    std::ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "第一行文本" << std::endl;
        outFile << "第二行文本" << std::endl;
        outFile << "数字: " << 42 << std::endl;
        outFile.close();
        std::cout << "文件写入成功" << std::endl;
    } else {
        std::cout << "无法打开文件进行写入" << std::endl;
    }

    // 读取文件
    std::ifstream inFile("example.txt");
    if (inFile.is_open()) {
        std::string line;
        std::cout << "\n文件内容:" << std::endl;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "无法打开文件进行读取" << std::endl;
    }

    return 0;
}
```

**预期输出：**

```
=== 文件输入输出示例 ===
文件写入成功

文件内容:
第一行文本
第二行文本
数字: 42
```

**文件操作模式：**

| 模式 | 说明 |
|------|------|
| `std::ios::in` | 读取模式 |
| `std::ios::out` | 写入模式 |
| `std::ios::app` | 追加模式 |
| `std::ios::binary` | 二进制模式 |
| `std::ios::trunc` | 截断模式（清空文件） |

---

## 第3章 变量和运算符

### 3.1 变量声明和初始化

变量是程序中用于存储数据的命名内存位置。每个变量都有名称、类型和值。理解变量的声明和初始化是编程的基础。

**变量的三个要素：**

1. **类型**：决定变量可以存储什么样的数据
2. **名称**：用于在程序中引用变量
3. **值**：变量存储的实际数据

**变量声明和初始化的方式：**

```cpp
// 方式1：先声明，后赋值
int age;              // 声明（此时age的值未定义）
age = 25;             // 赋值（初始化）

// 方式2：声明时初始化（推荐）
int score = 95;       // 使用等号初始化

// 方式3：使用花括号初始化（C++11，推荐）
int count{10};        // 统一初始化语法
int value{};          // 初始化为0

// 方式4：使用括号初始化
int number(42);       // 函数式初始化
```

**完整示例 - 变量声明和初始化：**

```cpp
#include <iostream>
#include <string>

int main() {
    // 未初始化的变量（危险！）
    int uninitializedVar;  // 包含垃圾值

    // 正确的初始化方式
    int age = 25;                    // 传统初始化
    double salary{50000.50};         // 统一初始化
    std::string name = "Alice";      // 字符串初始化
    bool isEmployed{true};           // 布尔值初始化

    // 多个变量声明
    int x = 10, y = 20, z = 30;      // 同时声明多个变量

    // 常量（不可修改）
    const double PI = 3.14159;       // 常量必须初始化
    const int MAX_SCORE{100};        // 使用花括号初始化常量

    // 输出变量值
    std::cout << "=== 变量值 ===" << std::endl;
    std::cout << "年龄: " << age << std::endl;
    std::cout << "薪水: " << salary << std::endl;
    std::cout << "姓名: " << name << std::endl;
    std::cout << "是否在职: " << (isEmployed ? "是" : "否") << std::endl;
    std::cout << "x, y, z: " << x << ", " << y << ", " << z << std::endl;
    std::cout << "圆周率: " << PI << std::endl;
    std::cout << "最高分: " << MAX_SCORE << std::endl;

    // 变量可以被重新赋值（常量除外）
    age = 26;
    std::cout << "\n更新后的年龄: " << age << std::endl;

    // PI = 3.14;  // 错误！常量不能被修改

    return 0;
}
```

**预期输出：**

```txt
=== 变量值 ===
年龄: 25
薪水: 50000.5
姓名: Alice
是否在职: 是
x, y, z: 10, 20, 30
圆周率: 3.14159
最高分: 100

更新后的年龄: 26
```

**变量命名规则：**

- ✅ 必须以字母或下划线开头
- ✅ 可以包含字母、数字和下划线
- ✅ 区分大小写（`age`和`Age`是不同的变量）
- ❌ 不能使用C++关键字（如`int`、`return`等）
- ❌ 不能包含空格或特殊字符

**良好的命名习惯：**

```cpp
#include <iostream>

int main() {
    // 好的命名（描述性强）
    int studentAge = 20;
    double accountBalance = 1000.50;
    bool isLoggedIn = true;

    // 不好的命名（难以理解）
    int a = 20;
    double b = 1000.50;
    bool c = true;

    // 使用驼峰命名法或下划线命名法
    int myVariableName = 10;      // 驼峰命名法
    int my_variable_name = 10;    // 下划线命名法

    std::cout << "学生年龄: " << studentAge << std::endl;
    std::cout << "账户余额: " << accountBalance << std::endl;
    std::cout << "是否登录: " << (isLoggedIn ? "是" : "否") << std::endl;

    return 0;
}
```

**重要提示：**

- ⚠️ 始终在使用变量前初始化它。未初始化的变量包含不可预测的垃圾值
- ⚠️ 使用`const`关键字声明不会改变的值
- ⚠️ 选择有意义的变量名，让代码自解释

### 3.2 变量作用域

变量的作用域（scope）决定了变量在程序中的可见性和生命周期。理解作用域对于编写正确的程序至关重要。

**作用域的类型：**

1. **全局作用域**：在所有函数外部声明，整个程序都可访问
2. **局部作用域**：在函数内部声明，只在函数内可访问
3. **块作用域**：在代码块`{}`内声明，只在块内可访问

**完整示例 - 变量作用域：**

```cpp
#include <iostream>

// 全局变量（在所有函数外部）
int globalVar = 100;
const double PI = 3.14159;  // 全局常量

// 函数声明
void demonstrateScope();

int main() {
    std::cout << "=== 变量作用域演示 ===" << std::endl;

    // 局部变量（只在main函数内可见）
    int localVar = 50;

    std::cout << "main函数中：" << std::endl;
    std::cout << "  全局变量: " << globalVar << std::endl;
    std::cout << "  局部变量: " << localVar << std::endl;
    std::cout << "  全局常量PI: " << PI << std::endl;

    // 块作用域
    {
        int blockVar = 25;  // 只在这个块内可见
        std::cout << "\n代码块内：" << std::endl;
        std::cout << "  块变量: " << blockVar << std::endl;
        std::cout << "  局部变量: " << localVar << std::endl;  // 可以访问外层变量
        std::cout << "  全局变量: " << globalVar << std::endl;

        // 可以修改外层变量
        localVar = 60;
        globalVar = 200;
    }

    // std::cout << blockVar << std::endl;  // 错误！blockVar超出作用域

    std::cout << "\n代码块后：" << std::endl;
    std::cout << "  局部变量（已修改）: " << localVar << std::endl;
    std::cout << "  全局变量（已修改）: " << globalVar << std::endl;

    // 调用其他函数
    demonstrateScope();

    return 0;
}

void demonstrateScope() {
    std::cout << "\ndemonstrateScope函数中：" << std::endl;
    std::cout << "  全局变量: " << globalVar << std::endl;
    // std::cout << localVar << std::endl;  // 错误！localVar在main函数中，这里不可见

    int localVar = 999;  // 这是一个新的局部变量，与main中的localVar不同
    std::cout << "  本函数的局部变量: " << localVar << std::endl;
}
```

**预期输出：**

```txt
=== 变量作用域演示 ===
main函数中：
  全局变量: 100
  局部变量: 50
  全局常量PI: 3.14159

代码块内：
  块变量: 25
  局部变量: 50
  全局变量: 100

代码块后：
  局部变量（已修改）: 60
  全局变量（已修改）: 200

demonstrateScope函数中：
  全局变量: 200
  本函数的局部变量: 999
```

**变量遮蔽（Shadowing）示例：**

```cpp
#include <iostream>

int value = 100;  // 全局变量

int main() {
    std::cout << "全局变量: " << value << std::endl;  // 输出100

    int value = 50;  // 局部变量，遮蔽了全局变量
    std::cout << "局部变量: " << value << std::endl;  // 输出50

    {
        int value = 25;  // 块变量，遮蔽了局部变量
        std::cout << "块变量: " << value << std::endl;  // 输出25

        // 使用::访问全局变量
        std::cout << "全局变量（使用::）: " << ::value << std::endl;  // 输出100
    }

    std::cout << "块外的局部变量: " << value << std::endl;  // 输出50

    return 0;
}
```

**预期输出：**

```
全局变量: 100
局部变量: 50
块变量: 25
全局变量（使用::）: 100
块外的局部变量: 50
```

**作用域最佳实践：**

- ✅ 使用最小的作用域（在需要的地方声明变量）
- ✅ 尽可能避免全局变量（难以维护和调试）
- ✅ 在循环中声明循环变量：`for (int i = 0; i < 10; i++)`
- ❌ 避免变量遮蔽（容易引起混淆）
- ❌ 不要过度使用全局变量

**变量生命周期：**

```cpp
#include <iostream>

int globalCounter = 0;  // 程序开始时创建，程序结束时销毁

void incrementCounter() {
    static int staticCounter = 0;  // 静态局部变量，只初始化一次
    int localCounter = 0;          // 每次调用都重新创建

    staticCounter++;
    localCounter++;
    globalCounter++;

    std::cout << "静态计数器: " << staticCounter
              << ", 局部计数器: " << localCounter
              << ", 全局计数器: " << globalCounter << std::endl;
}

int main() {
    std::cout << "=== 变量生命周期演示 ===" << std::endl;

    incrementCounter();  // 静态:1, 局部:1, 全局:1
    incrementCounter();  // 静态:2, 局部:1, 全局:2
    incrementCounter();  // 静态:3, 局部:1, 全局:3

    return 0;
}
```

**预期输出：**

```txt
=== 变量生命周期演示 ===
静态计数器: 1, 局部计数器: 1, 全局计数器: 1
静态计数器: 2, 局部计数器: 1, 全局计数器: 2
静态计数器: 3, 局部计数器: 1, 全局计数器: 3
```

**关键要点：**

- **局部变量**：函数每次调用时创建，函数结束时销毁
- **静态局部变量**：第一次调用时创建，程序结束时销毁，保持值不变
- **全局变量**：程序开始时创建，程序结束时销毁

### 3.3 运算符

运算符是用于执行特定操作的符号。C++提供了丰富的运算符，包括算术、比较、逻辑、赋值等多种类型。

#### 3.3.1 算术运算符

算术运算符用于执行基本的数学运算。

**完整示例 - 算术运算符：**

```cpp
#include <iostream>

int main() {
    int a = 10, b = 3;
    double x = 10.0, y = 3.0;

    std::cout << "=== 算术运算符 ===" << std::endl;
    std::cout << "整数运算：" << std::endl;
    std::cout << "a + b = " << (a + b) << std::endl;  // 13（加法）
    std::cout << "a - b = " << (a - b) << std::endl;  // 7（减法）
    std::cout << "a * b = " << (a * b) << std::endl;  // 30（乘法）
    std::cout << "a / b = " << (a / b) << std::endl;  // 3（整数除法，舍弃小数）
    std::cout << "a % b = " << (a % b) << std::endl;  // 1（取模，余数）

    std::cout << "\n浮点数运算：" << std::endl;
    std::cout << "x / y = " << (x / y) << std::endl;  // 3.33333（浮点除法）
    // std::cout << (x % y) << std::endl;  // 错误！%不能用于浮点数

    // 自增和自减运算符
    int count = 5;
    std::cout << "\n自增自减运算符：" << std::endl;
    std::cout << "count初始值: " << count << std::endl;
    std::cout << "count++（后缀）: " << count++ << std::endl;  // 输出5，然后count变为6
    std::cout << "count现在是: " << count << std::endl;        // 6
    std::cout << "++count（前缀）: " << ++count << std::endl;  // count先变为7，然后输出7
    std::cout << "count现在是: " << count << std::endl;        // 7

    // 复合赋值运算符
    int num = 10;
    std::cout << "\n复合赋值运算符：" << std::endl;
    std::cout << "num初始值: " << num << std::endl;
    num += 5;  // 等价于 num = num + 5
    std::cout << "num += 5: " << num << std::endl;  // 15
    num -= 3;  // 等价于 num = num - 3
    std::cout << "num -= 3: " << num << std::endl;  // 12
    num *= 2;  // 等价于 num = num * 2
    std::cout << "num *= 2: " << num << std::endl;  // 24
    num /= 4;  // 等价于 num = num / 4
    std::cout << "num /= 4: " << num << std::endl;  // 6
    num %= 4;  // 等价于 num = num % 4
    std::cout << "num %= 4: " << num << std::endl;  // 2

    return 0;
}
```

**预期输出：**

```txt
=== 算术运算符 ===
整数运算：
a + b = 13
a - b = 7
a * b = 30
a / b = 3
a % b = 1

浮点数运算：
x / y = 3.33333

自增自减运算符：
count初始值: 5
count++（后缀）: 5
count现在是: 6
++count（前缀）: 7
count现在是: 7

复合赋值运算符：
num初始值: 10
num += 5: 15
num -= 3: 12
num *= 2: 24
num /= 4: 6
num %= 4: 2
```

#### 3.3.2 比较运算符

比较运算符用于比较两个值，返回布尔值（true或false）。

**完整示例 - 比较运算符：**

```cpp
#include <iostream>

int main() {
    int x = 10, y = 20, z = 10;

    std::cout << "=== 比较运算符 ===" << std::endl;
    std::cout << "x = " << x << ", y = " << y << ", z = " << z << std::endl;
    std::cout << std::endl;

    // 在C++中，true显示为1，false显示为0
    std::cout << "x == y: " << (x == y) << " (相等)" << std::endl;        // 0 (false)
    std::cout << "x == z: " << (x == z) << " (相等)" << std::endl;        // 1 (true)
    std::cout << "x != y: " << (x != y) << " (不等)" << std::endl;        // 1 (true)
    std::cout << "x < y: " << (x < y) << " (小于)" << std::endl;          // 1 (true)
    std::cout << "x > y: " << (x > y) << " (大于)" << std::endl;          // 0 (false)
    std::cout << "x <= z: " << (x <= z) << " (小于等于)" << std::endl;    // 1 (true)
    std::cout << "y >= x: " << (y >= x) << " (大于等于)" << std::endl;    // 1 (true)

    // 使用boolalpha让布尔值显示为true/false
    std::cout << std::boolalpha;  // 设置布尔值输出格式
    std::cout << "\n使用boolalpha后：" << std::endl;
    std::cout << "x == y: " << (x == y) << std::endl;  // false
    std::cout << "x < y: " << (x < y) << std::endl;    // true

    return 0;
}
```

**预期输出：**

```txt
=== 比较运算符 ===
x = 10, y = 20, z = 10

x == y: 0 (相等)
x == z: 1 (相等)
x != y: 1 (不等)
x < y: 1 (小于)
x > y: 0 (大于)
x <= z: 1 (小于等于)
y >= x: 1 (大于等于)

使用boolalpha后：
x == y: false
x < y: true
```

#### 3.3.3 逻辑运算符

逻辑运算符用于组合多个条件表达式。

**完整示例 - 逻辑运算符：**

```cpp
#include <iostream>

int main() {
    bool a = true, b = false;
    int age = 25;
    double salary = 50000;

    std::cout << std::boolalpha;  // 显示true/false而不是1/0
    std::cout << "=== 逻辑运算符 ===" << std::endl;

    // 基本逻辑运算
    std::cout << "a = " << a << ", b = " << b << std::endl;
    std::cout << "a && b (与): " << (a && b) << std::endl;  // false（两者都为true才是true）
    std::cout << "a || b (或): " << (a || b) << std::endl;  // true（至少一个为true就是true）
    std::cout << "!a (非): " << (!a) << std::endl;          // false（取反）
    std::cout << "!b (非): " << (!b) << std::endl;          // true（取反）

    // 实际应用示例
    std::cout << "\n实际应用：" << std::endl;
    std::cout << "年龄: " << age << ", 薪水: " << salary << std::endl;

    // 检查是否符合贷款条件（年龄>=18且薪水>=30000）
    bool canGetLoan = (age >= 18) && (salary >= 30000);
    std::cout << "可以获得贷款: " << canGetLoan << std::endl;  // true

    // 检查是否需要缴税（薪水>40000或有其他收入）
    bool hasOtherIncome = false;
    bool needPayTax = (salary > 40000) || hasOtherIncome;
    std::cout << "需要缴税: " << needPayTax << std::endl;  // true

    // 短路求值演示
    std::cout << "\n短路求值：" << std::endl;
    int x = 5;
    // 在&&中，如果第一个条件为false，第二个条件不会被评估
    if (false && (++x > 0)) {
        std::cout << "这不会执行" << std::endl;
    }
    std::cout << "x的值: " << x << " (没有增加)" << std::endl;  // 5

    // 在||中，如果第一个条件为true，第二个条件不会被评估
    if (true || (++x > 0)) {
        std::cout << "这会执行" << std::endl;
    }
    std::cout << "x的值: " << x << " (仍然没有增加)" << std::endl;  // 5

    return 0;
}
```

**预期输出：**

```
=== 逻辑运算符 ===
a = true, b = false
a && b (与): false
a || b (或): true
!a (非): false
!b (非): true

实际应用：
年龄: 25, 薪水: 50000
可以获得贷款: true
需要缴税: true

短路求值：
x的值: 5 (没有增加)
这会执行
x的值: 5 (仍然没有增加)
```

**运算符优先级（从高到低）：**

| 优先级 | 运算符 | 说明 |
|--------|--------|------|
| 1 | `()` | 括号 |
| 2 | `!` `++` `--` | 逻辑非、自增、自减 |
| 3 | `*` `/` `%` | 乘、除、取模 |
| 4 | `+` `-` | 加、减 |
| 5 | `<` `<=` `>` `>=` | 比较运算符 |
| 6 | `==` `!=` | 相等、不等 |
| 7 | `&&` | 逻辑与 |
| 8 | `||` | 逻辑或 |
| 9 | `=` `+=` `-=` 等 | 赋值运算符 |

**优先级示例：**

```cpp
#include <iostream>

int main() {
    int result;

    // 没有括号
    result = 5 + 3 * 2;  // 先乘后加：5 + 6 = 11
    std::cout << "5 + 3 * 2 = " << result << std::endl;

    // 使用括号改变优先级
    result = (5 + 3) * 2;  // 先加后乘：8 * 2 = 16
    std::cout << "(5 + 3) * 2 = " << result << std::endl;

    // 复杂表达式
    bool condition = 10 > 5 && 20 < 30 || false;
    // 等价于：((10 > 5) && (20 < 30)) || false
    std::cout << std::boolalpha;
    std::cout << "10 > 5 && 20 < 30 || false = " << condition << std::endl;  // true

    return 0;
}
```

**最佳实践：**

- ✅ 使用括号明确表达式的计算顺序，即使不是必需的
- ✅ 一行代码不要包含太多运算符，保持可读性
- ✅ 理解短路求值的特性
- ❌ 不要在一个表达式中多次修改同一个变量（如`x = x++ + ++x`）

---

## 第4章 字符串处理

C++提供两种字符串：C风格字符串（字符数组）和C++风格字符串（std::string类）。

### 4.1 C风格字符串

C风格字符串是以空字符`\0`结尾的字符数组。

**完整示例 - C风格字符串：**

```cpp
#include <iostream>
#include <cstring>  // C字符串函数库

int main() {
    std::cout << "=== C风格字符串示例 ===" << std::endl;

    // 声明和初始化
    char str1[] = "Hello";  // 自动添加\0
    char str2[20] = "World";
    char str3[50];

    std::cout << "str1: " << str1 << std::endl;
    std::cout << "str2: " << str2 << std::endl;

    // 字符串长度
    std::cout << "\nstr1长度: " << strlen(str1) << std::endl;

    // 字符串复制
    strcpy(str3, str1);
    std::cout << "复制后str3: " << str3 << std::endl;

    // 字符串连接
    strcat(str3, " ");
    strcat(str3, str2);
    std::cout << "连接后str3: " << str3 << std::endl;

    // 字符串比较
    if (strcmp(str1, str2) == 0) {
        std::cout << "\nstr1和str2相同" << std::endl;
    } else {
        std::cout << "\nstr1和str2不同" << std::endl;
    }

    return 0;
}
```

### 4.2 C++风格字符串（std::string）

`std::string`是C++标准库提供的字符串类，比C风格字符串更安全、更易用。

**完整示例 - std::string：**

```cpp
#include <iostream>
#include <string>

int main() {
    std::cout << "=== std::string示例 ===" << std::endl;

    // 声明和初始化
    std::string s1 = "Hello";
    std::string s2("World");
    std::string s3;

    std::cout << "s1: " << s1 << std::endl;
    std::cout << "s2: " << s2 << std::endl;

    // 字符串连接
    std::string s4 = s1 + " " + s2;
    std::cout << "\n连接: " << s4 << std::endl;

    // 字符串长度
    std::cout << "s4长度: " << s4.length() << std::endl;
    std::cout << "s4大小: " << s4.size() << std::endl;

    // 访问字符
    std::cout << "\n第一个字符: " << s4[0] << std::endl;
    std::cout << "最后一个字符: " << s4[s4.length() - 1] << std::endl;

    // 子字符串
    std::string sub = s4.substr(0, 5);  // 从位置0开始，长度5
    std::cout << "\n子字符串: " << sub << std::endl;

    // 查找
    size_t pos = s4.find("World");
    if (pos != std::string::npos) {
        std::cout << "找到'World'在位置: " << pos << std::endl;
    }

    // 替换
    s4.replace(0, 5, "Hi");
    std::cout << "\n替换后: " << s4 << std::endl;

    // 插入和删除
    s4.insert(2, "!!!");
    std::cout << "插入后: " << s4 << std::endl;

    s4.erase(2, 3);
    std::cout << "删除后: " << s4 << std::endl;

    return 0;
}
```

**C风格字符串 vs std::string：**

| 特性 | C风格字符串 | std::string |
|------|------------|-------------|
| 声明 | `char str[100]` | `std::string str` |
| 安全性 | 容易溢出 | 自动管理内存 |
| 易用性 | 需要手动管理 | 提供丰富方法 |
| 性能 | 稍快 | 快 |
| 推荐使用 | ❌ 否 | ✅ 是 |

---

## 第5章 控制流

控制流语句决定程序的执行顺序。通过条件语句和循环，我们可以让程序根据不同情况做出不同的决策，或重复执行某些操作。

### 5.1 条件语句

条件语句允许程序根据条件的真假来选择不同的执行路径。

#### 5.1.1 if语句

最基本的条件语句，当条件为真时执行代码块。

**完整示例 - if语句：**

```cpp
#include <iostream>

int main() {
    int age = 18;
    double temperature = 25.5;
    bool hasLicense = true;

    std::cout << "=== if语句示例 ===" << std::endl;

    // 简单if语句
    if (age >= 18) {
        std::cout << "你是成年人" << std::endl;
    }

    // 多个独立的if语句
    if (temperature > 30) {
        std::cout << "天气很热" << std::endl;
    }

    if (temperature >= 20 && temperature <= 30) {
        std::cout << "天气适宜" << std::endl;
    }

    if (temperature < 20) {
        std::cout << "天气有点冷" << std::endl;
    }

    // 组合条件
    if (age >= 18 && hasLicense) {
        std::cout << "你可以开车" << std::endl;
    }

    // 单行if语句（不推荐，但合法）
    if (age >= 18) std::cout << "成年人（单行）" << std::endl;

    return 0;
}
```

**预期输出：**

```
=== if语句示例 ===
你是成年人
天气适宜
你可以开车
成年人（单行）
```

#### 5.1.2 if-else语句

提供两个执行路径：条件为真时执行一个，为假时执行另一个。

**完整示例 - if-else语句：**

```cpp
#include <iostream>

int main() {
    int score = 75;
    int age = 16;

    std::cout << "=== if-else语句示例 ===" << std::endl;

    // 简单if-else
    std::cout << "分数: " << score << std::endl;
    if (score >= 60) {
        std::cout << "及格" << std::endl;
    } else {
        std::cout << "不及格" << std::endl;
    }

    // if-else if-else链
    std::cout << "\n成绩等级: ";
    if (score >= 90) {
        std::cout << "A (优秀)" << std::endl;
    } else if (score >= 80) {
        std::cout << "B (良好)" << std::endl;
    } else if (score >= 70) {
        std::cout << "C (中等)" << std::endl;
    } else if (score >= 60) {
        std::cout << "D (及格)" << std::endl;
    } else {
        std::cout << "F (不及格)" << std::endl;
    }

    // 嵌套if-else
    std::cout << "\n年龄: " << age << std::endl;
    if (age >= 18) {
        if (age >= 65) {
            std::cout << "老年人" << std::endl;
        } else {
            std::cout << "成年人" << std::endl;
        }
    } else {
        if (age >= 13) {
            std::cout << "青少年" << std::endl;
        } else {
            std::cout << "儿童" << std::endl;
        }
    }

    return 0;
}
```

**预期输出：**

```
=== if-else语句示例 ===
分数: 75
及格

成绩等级: C (中等)

年龄: 16
青少年
```

#### 5.1.3 三元运算符

三元运算符是if-else的简洁形式：`条件 ? 值1 : 值2`

**完整示例 - 三元运算符：**

```cpp
#include <iostream>
#include <string>

int main() {
    int a = 10, b = 20;
    int age = 25;

    std::cout << "=== 三元运算符示例 ===" << std::endl;

    // 基本用法
    int max = (a > b) ? a : b;
    std::cout << "较大的数: " << max << std::endl;

    // 用于字符串
    std::string status = (age >= 18) ? "成年人" : "未成年人";
    std::cout << "状态: " << status << std::endl;

    // 嵌套三元运算符（不推荐，难以阅读）
    int score = 85;
    std::string grade = (score >= 90) ? "A" :
                        (score >= 80) ? "B" :
                        (score >= 70) ? "C" : "F";
    std::cout << "等级: " << grade << std::endl;

    // 在输出中直接使用
    std::cout << "数字 " << a << " 是"
              << ((a % 2 == 0) ? "偶数" : "奇数") << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 三元运算符示例 ===
较大的数: 20
状态: 成年人
等级: B
数字 10 是偶数
```

#### 5.1.4 switch语句

switch语句用于多路分支，比多个if-else更清晰。

**完整示例 - switch语句：**

```cpp
#include <iostream>

int main() {
    int day = 3;
    char grade = 'B';
    int choice = 2;

    std::cout << "=== switch语句示例 ===" << std::endl;

    // 基本switch语句
    std::cout << "今天是: ";
    switch (day) {
        case 1:
            std::cout << "星期一" << std::endl;
            break;
        case 2:
            std::cout << "星期二" << std::endl;
            break;
        case 3:
            std::cout << "星期三" << std::endl;
            break;
        case 4:
            std::cout << "星期四" << std::endl;
            break;
        case 5:
            std::cout << "星期五" << std::endl;
            break;
        case 6:
        case 7:
            std::cout << "周末" << std::endl;
            break;
        default:
            std::cout << "无效的日期" << std::endl;
    }

    // 使用字符
    std::cout << "\n成绩等级 " << grade << ": ";
    switch (grade) {
        case 'A':
            std::cout << "优秀 (90-100)" << std::endl;
            break;
        case 'B':
            std::cout << "良好 (80-89)" << std::endl;
            break;
        case 'C':
            std::cout << "中等 (70-79)" << std::endl;
            break;
        case 'D':
            std::cout << "及格 (60-69)" << std::endl;
            break;
        case 'F':
            std::cout << "不及格 (<60)" << std::endl;
            break;
        default:
            std::cout << "无效等级" << std::endl;
    }

    // 演示穿透效果（fall-through）
    std::cout << "\n菜单选择 " << choice << ": ";
    switch (choice) {
        case 1:
            std::cout << "选项1被选中" << std::endl;
            // 注意：没有break，会继续执行下一个case
        case 2:
            std::cout << "选项2被选中" << std::endl;
            // 没有break
        case 3:
            std::cout << "选项3被选中" << std::endl;
            break;
        default:
            std::cout << "无效选项" << std::endl;
    }

    return 0;
}
```

**预期输出：**

```
=== switch语句示例 ===
今天是: 星期三

成绩等级 B: 良好 (80-89)

菜单选择 2: 选项2被选中
选项3被选中
```

**switch语句的重要规则：**

- ✅ case后面的值必须是常量表达式
- ✅ 每个case后通常需要break语句
- ✅ default分支是可选的，但建议添加
- ✅ 可以有多个case共享同一个代码块
- ❌ 不能使用浮点数或字符串作为case值（C++17之前）
- ❌ case值不能重复

**switch vs if-else选择指南：**

```cpp
#include <iostream>

int main() {
    int value = 5;

    // 使用switch（当有多个离散值时）
    switch (value) {
        case 1: std::cout << "一" << std::endl; break;
        case 2: std::cout << "二" << std::endl; break;
        case 3: std::cout << "三" << std::endl; break;
        default: std::cout << "其他" << std::endl;
    }

    // 使用if-else（当有范围判断时）
    if (value < 0) {
        std::cout << "负数" << std::endl;
    } else if (value >= 0 && value <= 10) {
        std::cout << "0到10之间" << std::endl;
    } else {
        std::cout << "大于10" << std::endl;
    }

    return 0;
}
```

**关键点**：

- 使用switch：当比较的是离散的、确定的值（如1, 2, 3或'A', 'B', 'C'）
- 使用if-else：当需要范围判断或复杂条件时

### 5.2 循环

循环允许程序重复执行一段代码，直到满足某个条件。C++提供了多种循环结构。

#### 5.2.1 for循环

for循环是最常用的循环，适合已知循环次数的情况。

**for循环结构：**

```
for (初始化; 条件; 更新) {
    // 循环体
}
```

**完整示例 - for循环：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== for循环示例 ===" << std::endl;

    // 基本for循环
    std::cout << "数字0到4: ";
    for (int i = 0; i < 5; i++) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 倒序循环
    std::cout << "倒数: ";
    for (int i = 5; i > 0; i--) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 步长为2
    std::cout << "偶数0到10: ";
    for (int i = 0; i <= 10; i += 2) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 嵌套for循环（打印乘法表）
    std::cout << "\n3x3乘法表:" << std::endl;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            std::cout << i << "x" << j << "=" << (i*j) << "\t";
        }
        std::cout << std::endl;
    }

    // 计算总和
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        sum += i;
    }
    std::cout << "\n1到10的和: " << sum << std::endl;

    // 多个变量
    std::cout << "多变量循环: ";
    for (int i = 0, j = 10; i < 5; i++, j--) {
        std::cout << "(" << i << "," << j << ") ";
    }
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== for循环示例 ===
数字0到4: 0 1 2 3 4
倒数: 5 4 3 2 1
偶数0到10: 0 2 4 6 8 10

3x3乘法表:
1x1=1 1x2=2 1x3=3
2x1=2 2x2=4 2x3=6
3x1=3 3x2=6 3x3=9

1到10的和: 55
多变量循环: (0,10) (1,9) (2,8) (3,7) (4,6)
```

#### 5.2.2 while循环

while循环在条件为真时重复执行，适合不知道确切循环次数的情况。

**完整示例 - while循环：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== while循环示例 ===" << std::endl;

    // 基本while循环
    std::cout << "数字0到4: ";
    int i = 0;
    while (i < 5) {
        std::cout << i << " ";
        i++;
    }
    std::cout << std::endl;

    // 用户输入验证（模拟）
    int password = 0;
    int attempts = 0;
    const int correctPassword = 1234;

    std::cout << "\n密码验证示例（正确密码是1234）:" << std::endl;
    // 在实际程序中，这里会从用户输入读取
    // 这里我们模拟几次错误尝试
    int testPasswords[] = {1111, 2222, 1234};
    int testIndex = 0;

    while (password != correctPassword && attempts < 3) {
        password = testPasswords[testIndex++];
        attempts++;
        std::cout << "尝试 " << attempts << ": 输入密码 " << password;

        if (password == correctPassword) {
            std::cout << " - 正确！" << std::endl;
        } else {
            std::cout << " - 错误！" << std::endl;
        }
    }

    if (password == correctPassword) {
        std::cout << "登录成功！" << std::endl;
    } else {
        std::cout << "登录失败，尝试次数过多。" << std::endl;
    }

    // 计算阶乘
    int n = 5;
    int factorial = 1;
    int counter = n;

    while (counter > 0) {
        factorial *= counter;
        counter--;
    }
    std::cout << "\n" << n << "的阶乘是: " << factorial << std::endl;

    return 0;
}
```

**预期输出：**

```
=== while循环示例 ===
数字0到4: 0 1 2 3 4

密码验证示例（正确密码是1234）:
尝试 1: 输入密码 1111 - 错误！
尝试 2: 输入密码 2222 - 错误！
尝试 3: 输入密码 1234 - 正确！
登录成功！

5的阶乘是: 120
```

#### 5.2.3 do-while循环

do-while循环至少执行一次，然后检查条件。

**完整示例 - do-while循环：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== do-while循环示例 ===" << std::endl;

    // 基本do-while循环
    std::cout << "数字0到4: ";
    int i = 0;
    do {
        std::cout << i << " ";
        i++;
    } while (i < 5);
    std::cout << std::endl;

    // 至少执行一次的特性
    std::cout << "\ndo-while至少执行一次:" << std::endl;
    int x = 10;
    do {
        std::cout << "x = " << x << " (条件为假，但仍执行了一次)" << std::endl;
    } while (x < 5);  // 条件为假

    // 对比：while循环不会执行
    std::cout << "\nwhile循环不会执行:" << std::endl;
    int y = 10;
    while (y < 5) {  // 条件为假，不执行
        std::cout << "这不会被打印" << std::endl;
    }
    std::cout << "while循环体没有执行" << std::endl;

    // 菜单系统示例
    std::cout << "\n菜单系统示例:" << std::endl;
    int choice;
    int menuCount = 0;

    do {
        std::cout << "\n--- 菜单 ---" << std::endl;
        std::cout << "1. 选项1" << std::endl;
        std::cout << "2. 选项2" << std::endl;
        std::cout << "3. 选项3" << std::endl;
        std::cout << "0. 退出" << std::endl;

        // 模拟用户选择
        int choices[] = {1, 2, 0};
        choice = choices[menuCount++];
        std::cout << "选择: " << choice << std::endl;

        switch (choice) {
            case 1:
                std::cout << "执行选项1" << std::endl;
                break;
            case 2:
                std::cout << "执行选项2" << std::endl;
                break;
            case 3:
                std::cout << "执行选项3" << std::endl;
                break;
            case 0:
                std::cout << "退出程序" << std::endl;
                break;
            default:
                std::cout << "无效选择" << std::endl;
        }
    } while (choice != 0);

    return 0;
}
```

**预期输出：**

```
=== do-while循环示例 ===
数字0到4: 0 1 2 3 4

do-while至少执行一次:
x = 10 (条件为假，但仍执行了一次)

while循环不会执行:
while循环体没有执行

菜单系统示例:

--- 菜单 ---
1. 选项1
2. 选项2
3. 选项3
0. 退出
选择: 1
执行选项1

--- 菜单 ---
1. 选项1
2. 选项2
3. 选项3
0. 退出
选择: 2
执行选项2

--- 菜单 ---
1. 选项1
2. 选项2
3. 选项3
0. 退出
选择: 0
退出程序
```

#### 5.2.4 基于范围的for循环（C++11）

现代C++提供了更简洁的遍历容器的方式。

**完整示例 - 基于范围的for循环：**

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::cout << "=== 基于范围的for循环 ===" << std::endl;

    // 遍历数组
    int numbers[] = {1, 2, 3, 4, 5};
    std::cout << "数组元素: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 遍历vector
    std::vector<std::string> fruits = {"苹果", "香蕉", "橙子"};
    std::cout << "\n水果列表:" << std::endl;
    for (std::string fruit : fruits) {
        std::cout << "- " << fruit << std::endl;
    }

    // 使用引用修改元素
    int scores[] = {85, 90, 78, 92, 88};
    std::cout << "\n原始分数: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 给每个分数加5分
    for (int& score : scores) {  // 注意：使用引用&
        score += 5;
    }

    std::cout << "加分后: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 使用const引用（只读，效率高）
    std::vector<std::string> cities = {"北京", "上海", "广州", "深圳"};
    std::cout << "\n城市列表:" << std::endl;
    for (const std::string& city : cities) {  // const引用，避免拷贝
        std::cout << "城市: " << city << std::endl;
    }

    // 使用auto自动推导类型
    std::cout << "\n使用auto:" << std::endl;
    for (auto num : numbers) {  // auto自动推导为int
        std::cout << num * 2 << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 基于范围的for循环 ===
数组元素: 1 2 3 4 5

水果列表:
- 苹果
- 香蕉
- 橙子

原始分数: 85 90 78 92 88
加分后: 90 95 83 97 93

城市列表:
城市: 北京
城市: 上海
城市: 广州
城市: 深圳

使用auto:
2 4 6 8 10
```

**循环类型选择指南：**

| 循环类型 | 适用场景 | 示例 |
|---------|---------|------|
| for | 已知循环次数 | 遍历0到n |
| while | 未知循环次数，先判断后执行 | 等待用户输入 |
| do-while | 至少执行一次 | 菜单系统 |
| 范围for | 遍历容器 | 遍历数组、vector |

### 5.3 循环控制

循环控制语句允许我们改变循环的正常执行流程。

#### 5.3.1 break语句

break语句立即终止循环，跳出循环体。

**完整示例 - break语句：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== break语句示例 ===" << std::endl;

    // 在for循环中使用break
    std::cout << "查找第一个大于50的数:" << std::endl;
    int numbers[] = {10, 25, 35, 60, 75, 90};

    for (int i = 0; i < 6; i++) {
        std::cout << "检查: " << numbers[i];
        if (numbers[i] > 50) {
            std::cout << " - 找到了！" << std::endl;
            break;  // 找到后立即退出循环
        }
        std::cout << " - 继续查找" << std::endl;
    }

    // 在while循环中使用break
    std::cout << "\n猜数字游戏:" << std::endl;
    int secretNumber = 7;
    int guesses[] = {3, 5, 7, 9};  // 模拟用户猜测
    int guessIndex = 0;
    int attempts = 0;

    while (true) {  // 无限循环
        if (guessIndex >= 4) {
            std::cout << "没有更多猜测了" << std::endl;
            break;
        }

        int guess = guesses[guessIndex++];
        attempts++;
        std::cout << "第 " << attempts << " 次猜测: " << guess;

        if (guess == secretNumber) {
            std::cout << " - 正确！" << std::endl;
            break;  // 猜对了，退出循环
        } else {
            std::cout << " - 错误，再试一次" << std::endl;
        }
    }

    std::cout << "游戏结束，共猜了 " << attempts << " 次" << std::endl;

    // 在嵌套循环中使用break（只退出内层循环）
    std::cout << "\n嵌套循环中的break:" << std::endl;
    for (int i = 1; i <= 3; i++) {
        std::cout << "外层循环 i = " << i << std::endl;
        for (int j = 1; j <= 5; j++) {
            if (j == 3) {
                std::cout << "  内层循环在 j = " << j << " 时break" << std::endl;
                break;  // 只退出内层循环
            }
            std::cout << "  内层循环 j = " << j << std::endl;
        }
    }

    return 0;
}
```

**预期输出：**

```
=== break语句示例 ===
查找第一个大于50的数:
检查: 10 - 继续查找
检查: 25 - 继续查找
检查: 35 - 继续查找
检查: 60 - 找到了！

猜数字游戏:
第 1 次猜测: 3 - 错误，再试一次
第 2 次猜测: 5 - 错误，再试一次
第 3 次猜测: 7 - 正确！
游戏结束，共猜了 3 次

嵌套循环中的break:
外层循环 i = 1
  内层循环 j = 1
  内层循环 j = 2
  内层循环在 j = 3 时break
外层循环 i = 2
  内层循环 j = 1
  内层循环 j = 2
  内层循环在 j = 3 时break
外层循环 i = 3
  内层循环 j = 1
  内层循环 j = 2
  内层循环在 j = 3 时break
```

#### 5.3.2 continue语句

continue语句跳过当前迭代的剩余部分，直接进入下一次迭代。

**完整示例 - continue语句：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== continue语句示例 ===" << std::endl;

    // 跳过偶数
    std::cout << "只打印奇数 (1-10):" << std::endl;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // 跳过偶数
        }
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 跳过特定值
    std::cout << "\n跳过3的倍数 (1-15):" << std::endl;
    for (int i = 1; i <= 15; i++) {
        if (i % 3 == 0) {
            continue;  // 跳过3的倍数
        }
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 处理数组，跳过负数
    std::cout << "\n只处理正数:" << std::endl;
    int values[] = {5, -3, 8, -1, 12, -7, 15};
    int sum = 0;

    for (int value : values) {
        if (value < 0) {
            std::cout << "跳过负数: " << value << std::endl;
            continue;
        }
        std::cout << "处理正数: " << value << std::endl;
        sum += value;
    }
    std::cout << "正数总和: " << sum << std::endl;

    // 在while循环中使用continue
    std::cout << "\n在while循环中使用continue:" << std::endl;
    int count = 0;
    while (count < 10) {
        count++;
        if (count == 5) {
            std::cout << "跳过 " << count << std::endl;
            continue;
        }
        std::cout << count << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== continue语句示例 ===
只打印奇数 (1-10):
1 3 5 7 9

跳过3的倍数 (1-15):
1 2 4 5 7 8 10 11 13 14

只处理正数:
处理正数: 5
跳过负数: -3
处理正数: 8
跳过负数: -1
处理正数: 12
跳过负数: -7
处理正数: 15
正数总和: 40

在while循环中使用continue:
1 2 3 4 跳过 5
6 7 8 9 10
```

#### 5.3.3 break和continue的组合使用

**完整示例 - break和continue组合：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== break和continue组合使用 ===" << std::endl;

    // 示例1：打印1-20之间的奇数，但遇到15就停止
    std::cout << "打印奇数，遇到15停止:" << std::endl;
    for (int i = 1; i <= 20; i++) {
        if (i == 15) {
            std::cout << "\n遇到15，停止循环" << std::endl;
            break;
        }
        if (i % 2 == 0) {
            continue;  // 跳过偶数
        }
        std::cout << i << " ";
    }

    // 示例2：查找数组中的特定模式
    std::cout << "\n\n查找连续的正数序列:" << std::endl;
    int data[] = {-1, -2, 3, 4, 5, -3, 6, 7, 8, 9, -5};
    int consecutiveCount = 0;
    int maxConsecutive = 0;

    for (int value : data) {
        if (value < 0) {
            std::cout << "遇到负数 " << value << "，重置计数" << std::endl;
            consecutiveCount = 0;
            continue;
        }

        consecutiveCount++;
        std::cout << "正数 " << value << "，连续计数: " << consecutiveCount << std::endl;

        if (consecutiveCount > maxConsecutive) {
            maxConsecutive = consecutiveCount;
        }

        if (consecutiveCount >= 4) {
            std::cout << "找到4个连续正数，停止搜索" << std::endl;
            break;
        }
    }

    std::cout << "最大连续正数个数: " << maxConsecutive << std::endl;

    return 0;
}
```

**预期输出：**

```
=== break和continue组合使用 ===
打印奇数，遇到15停止:
1 3 5 7 9 11 13
遇到15，停止循环

查找连续的正数序列:
遇到负数 -1，重置计数
遇到负数 -2，重置计数
正数 3，连续计数: 1
正数 4，连续计数: 2
正数 5，连续计数: 3
遇到负数 -3，重置计数
正数 6，连续计数: 1
正数 7，连续计数: 2
正数 8，连续计数: 3
正数 9，连续计数: 4
找到4个连续正数，停止搜索
最大连续正数个数: 4
```

**循环控制最佳实践：**

- ✅ 使用break提前退出循环，避免不必要的迭代
- ✅ 使用continue跳过不需要处理的情况
- ✅ 在无限循环中必须有break条件
- ❌ 避免过度使用break和continue，可能使代码难以理解
- ❌ 在嵌套循环中使用break时要小心，它只退出最内层循环

**goto语句（不推荐）：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== goto语句（不推荐使用） ===" << std::endl;

    // goto可以跳转到标签位置，但会使代码难以理解
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == 1 && j == 1) {
                std::cout << "在 (" << i << "," << j << ") 处跳出所有循环" << std::endl;
                goto end_loops;  // 跳出所有嵌套循环
            }
            std::cout << "(" << i << "," << j << ") ";
        }
        std::cout << std::endl;
    }

end_loops:
    std::cout << "已跳出循环" << std::endl;

    // 更好的替代方案：使用函数和return
    std::cout << "\n推荐：使用函数替代goto" << std::endl;
    std::cout << "（将嵌套循环放在函数中，使用return退出）" << std::endl;

    return 0;
}
```

**关键要点：**

- **break**：立即终止循环
- **continue**：跳过当前迭代，继续下一次迭代
- **goto**：可以跳转到任意标签，但强烈不推荐使用
- 在嵌套循环中，break和continue只影响最内层循环

---

## 第6章 函数

函数是C++程序的基本构建块。它们允许我们将代码组织成可重用的模块，使程序更易于理解、测试和维护。

### 6.1 函数基础

函数是执行特定任务的命名代码块。函数可以接收输入（参数），执行操作，并返回结果。

**函数的组成部分：**

```cpp
返回类型 函数名(参数类型 参数1, 参数类型 参数2) {
    // 函数体：执行的代码
    return 值;  // 如果返回类型不是void
}
```

**完整示例 - 函数基础：**

```cpp
#include <iostream>

// 函数声明（原型）- 告诉编译器函数的存在
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
double divide(double a, double b);

int main() {
    std::cout << "=== 函数基础示例 ===" << std::endl;

    // 调用函数
    int sum = add(10, 5);
    int difference = subtract(10, 5);
    int product = multiply(10, 5);
    double quotient = divide(10.0, 5.0);

    std::cout << "10 + 5 = " << sum << std::endl;
    std::cout << "10 - 5 = " << difference << std::endl;
    std::cout << "10 * 5 = " << product << std::endl;
    std::cout << "10 / 5 = " << quotient << std::endl;

    // 直接在表达式中使用函数
    int result = add(multiply(3, 4), subtract(20, 5));
    std::cout << "\n(3 * 4) + (20 - 5) = " << result << std::endl;

    return 0;
}

// 函数定义 - 实现函数的功能
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        std::cout << "错误：除数不能为0" << std::endl;
        return 0.0;
    }
}
```

**预期输出：**

```
=== 函数基础示例 ===
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

(3 * 4) + (20 - 5) = 27
```

**函数声明 vs 函数定义：**

```cpp
#include <iostream>

// 方法1：先声明，后定义（推荐用于大型程序）
int square(int n);  // 声明

int main() {
    std::cout << "5的平方是: " << square(5) << std::endl;
    return 0;
}

int square(int n) {  // 定义
    return n * n;
}

// 方法2：在main之前直接定义（适合小程序）
/*
int square(int n) {
    return n * n;
}

int main() {
    std::cout << "5的平方是: " << square(5) << std::endl;
    return 0;
}
*/
```

**为什么需要函数声明？**

- 允许函数在定义之前被调用
- 可以将声明放在头文件中，定义放在源文件中
- 提高代码的组织性和可维护性

**完整示例 - 实用函数：**

```cpp
#include <iostream>
#include <cmath>

// 计算圆的面积
double calculateCircleArea(double radius) {
    const double PI = 3.14159265359;
    return PI * radius * radius;
}

// 计算圆的周长
double calculateCircleCircumference(double radius) {
    const double PI = 3.14159265359;
    return 2 * PI * radius;
}

// 判断是否为质数
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// 计算阶乘
int factorial(int n) {
    if (n <= 1) return 1;
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    std::cout << "=== 实用函数示例 ===" << std::endl;

    // 圆的计算
    double radius = 5.0;
    std::cout << "半径为 " << radius << " 的圆：" << std::endl;
    std::cout << "  面积: " << calculateCircleArea(radius) << std::endl;
    std::cout << "  周长: " << calculateCircleCircumference(radius) << std::endl;

    // 质数判断
    std::cout << "\n质数判断：" << std::endl;
    for (int i = 1; i <= 10; i++) {
        std::cout << i << (isPrime(i) ? " 是质数" : " 不是质数") << std::endl;
    }

    // 阶乘计算
    std::cout << "\n阶乘计算：" << std::endl;
    for (int i = 1; i <= 5; i++) {
        std::cout << i << "! = " << factorial(i) << std::endl;
    }

    return 0;
}
```

**预期输出：**

```
=== 实用函数示例 ===
半径为 5 的圆：
  面积: 78.5398
  周长: 31.4159

质数判断：
1 不是质数
2 是质数
3 是质数
4 不是质数
5 是质数
6 不是质数
7 是质数
8 不是质数
9 不是质数
10 不是质数

阶乘计算：
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

**函数设计原则：**

- ✅ 每个函数应该只做一件事，并做好
- ✅ 函数名应该清楚地描述其功能
- ✅ 保持函数简短（通常不超过50行）
- ✅ 避免副作用（除非函数的目的就是产生副作用）
- ✅ 使用有意义的参数名

### 6.2 无返回值的函数

void函数不返回值，用于执行操作而不产生结果。

**完整示例 - void函数：**

```cpp
#include <iostream>
#include <string>

// 打印问候语
void greet(std::string name) {
    std::cout << "你好, " << name << "!" << std::endl;
}

// 打印分隔线
void printSeparator(int length = 40) {
    for (int i = 0; i < length; i++) {
        std::cout << "=";
    }
    std::cout << std::endl;
}

// 打印数组
void printArray(int arr[], int size) {
    std::cout << "[";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i];
        if (i < size - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

// 打印表格
void printTable(int rows, int cols) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            std::cout << (i * j) << "\t";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::cout << "=== void函数示例 ===" << std::endl;

    greet("Alice");
    greet("Bob");
    greet("Charlie");

    printSeparator();

    int numbers[] = {1, 2, 3, 4, 5};
    std::cout << "数组内容: ";
    printArray(numbers, 5);

    printSeparator();
    std::cout << "3x3乘法表:" << std::endl;
    printTable(3, 3);

    return 0;
}
```

### 6.3 函数参数传递

C++有三种参数传递方式：按值传递、按引用传递和按指针传递。

**完整示例 - 参数传递方式：**

```cpp
#include <iostream>

// 按值传递：复制参数，不影响原始变量
void incrementByValue(int x) {
    x++;
    std::cout << "  函数内部（按值）: x = " << x << std::endl;
}

// 按引用传递：直接操作原始变量
void incrementByReference(int& x) {
    x++;
    std::cout << "  函数内部（按引用）: x = " << x << std::endl;
}

// 按指针传递：通过指针操作原始变量
void incrementByPointer(int* x) {
    (*x)++;
    std::cout << "  函数内部（按指针）: *x = " << *x << std::endl;
}

// 按const引用传递：只读，不能修改，但避免拷贝（效率高）
void printByConstReference(const int& x) {
    std::cout << "  值: " << x << std::endl;
    // x++;  // 错误！不能修改const引用
}

// 交换两个数（使用引用）
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    std::cout << "=== 参数传递方式 ===" << std::endl;

    // 按值传递
    int num1 = 5;
    std::cout << "\n按值传递:" << std::endl;
    std::cout << "调用前: num1 = " << num1 << std::endl;
    incrementByValue(num1);
    std::cout << "调用后: num1 = " << num1 << " (未改变)" << std::endl;

    // 按引用传递
    int num2 = 5;
    std::cout << "\n按引用传递:" << std::endl;
    std::cout << "调用前: num2 = " << num2 << std::endl;
    incrementByReference(num2);
    std::cout << "调用后: num2 = " << num2 << " (已改变)" << std::endl;

    // 按指针传递
    int num3 = 5;
    std::cout << "\n按指针传递:" << std::endl;
    std::cout << "调用前: num3 = " << num3 << std::endl;
    incrementByPointer(&num3);
    std::cout << "调用后: num3 = " << num3 << " (已改变)" << std::endl;

    // const引用
    int num4 = 100;
    std::cout << "\nconst引用传递:" << std::endl;
    printByConstReference(num4);

    // 交换示例
    int x = 10, y = 20;
    std::cout << "\n交换前: x = " << x << ", y = " << y << std::endl;
    swap(x, y);
    std::cout << "交换后: x = " << x << ", y = " << y << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 参数传递方式 ===

按值传递:
调用前: num1 = 5
  函数内部（按值）: x = 6
调用后: num1 = 5 (未改变)

按引用传递:
调用前: num2 = 5
  函数内部（按引用）: x = 6
调用后: num2 = 6 (已改变)

按指针传递:
调用前: num3 = 5
  函数内部（按指针）: *x = 6
调用后: num3 = 6 (已改变)

const引用传递:
  值: 100

交换前: x = 10, y = 20
交换后: x = 20, y = 10
```

### 6.4 函数重载

函数重载允许多个函数使用相同的名称，但参数列表不同。

**完整示例 - 函数重载：**

```cpp
#include <iostream>
#include <string>

// 重载add函数 - 不同参数类型
int add(int a, int b) {
    std::cout << "调用 int add(int, int)" << std::endl;
    return a + b;
}

double add(double a, double b) {
    std::cout << "调用 double add(double, double)" << std::endl;
    return a + b;
}

// 重载add函数 - 不同参数数量
int add(int a, int b, int c) {
    std::cout << "调用 int add(int, int, int)" << std::endl;
    return a + b + c;
}

// 重载print函数
void print(int value) {
    std::cout << "整数: " << value << std::endl;
}

void print(double value) {
    std::cout << "浮点数: " << value << std::endl;
}

void print(std::string value) {
    std::cout << "字符串: " << value << std::endl;
}

void print(int arr[], int size) {
    std::cout << "数组: [";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i];
        if (i < size - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

int main() {
    std::cout << "=== 函数重载示例 ===" << std::endl;

    // 调用不同版本的add
    std::cout << "\nadd函数重载:" << std::endl;
    std::cout << "结果: " << add(5, 3) << std::endl;
    std::cout << "结果: " << add(5.5, 3.2) << std::endl;
    std::cout << "结果: " << add(1, 2, 3) << std::endl;

    // 调用不同版本的print
    std::cout << "\nprint函数重载:" << std::endl;
    print(42);
    print(3.14);
    print("Hello, World!");

    int numbers[] = {1, 2, 3, 4, 5};
    print(numbers, 5);

    return 0;
}
```

**预期输出：**

```
=== 函数重载示例 ===

add函数重载:
调用 int add(int, int)
结果: 8
调用 double add(double, double)
结果: 8.7
调用 int add(int, int, int)
结果: 6

print函数重载:
整数: 42
浮点数: 3.14
字符串: Hello, World!
数组: [1, 2, 3, 4, 5]
```

**函数重载规则：**

- ✅ 参数数量不同
- ✅ 参数类型不同
- ✅ 参数顺序不同
- ❌ 仅返回类型不同（不允许）
- ❌ 仅参数名不同（不允许）

### 6.5 默认参数

默认参数允许函数在调用时省略某些参数。

**完整示例 - 默认参数：**

```cpp
#include <iostream>
#include <string>

// 单个默认参数
void greet(std::string name = "朋友") {
    std::cout << "你好, " << name << "!" << std::endl;
}

// 多个默认参数（从右到左）
void printInfo(std::string name, int age = 0, std::string city = "未知") {
    std::cout << "姓名: " << name
              << ", 年龄: " << age
              << ", 城市: " << city << std::endl;
}

// 计算矩形面积（默认为正方形）
double calculateArea(double length, double width = 0) {
    if (width == 0) {
        width = length;  // 如果没有提供宽度，使用长度（正方形）
    }
    return length * width;
}

// 打印重复字符
void printRepeated(char ch = '*', int count = 10) {
    for (int i = 0; i < count; i++) {
        std::cout << ch;
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "=== 默认参数示例 ===" << std::endl;

    // 使用默认参数
    std::cout << "\ngreet函数:" << std::endl;
    greet();              // 使用默认值
    greet("Alice");       // 提供参数

    // 部分使用默认参数
    std::cout << "\nprintInfo函数:" << std::endl;
    printInfo("Bob");                    // 使用两个默认值
    printInfo("Charlie", 25);            // 使用一个默认值
    printInfo("David", 30, "北京");      // 不使用默认值

    // 计算面积
    std::cout << "\ncalculateArea函数:" << std::endl;
    std::cout << "正方形(边长5): " << calculateArea(5) << std::endl;
    std::cout << "矩形(5x3): " << calculateArea(5, 3) << std::endl;

    // 打印字符
    std::cout << "\nprintRepeated函数:" << std::endl;
    printRepeated();           // 使用所有默认值
    printRepeated('-');        // 只改变字符
    printRepeated('#', 20);    // 改变字符和数量

    return 0;
}
```

**预期输出：**

```
=== 默认参数示例 ===

greet函数:
你好, 朋友!
你好, Alice!

printInfo函数:
姓名: Bob, 年龄: 0, 城市: 未知
姓名: Charlie, 年龄: 25, 城市: 未知
姓名: David, 年龄: 30, 城市: 北京

calculateArea函数:
正方形(边长5): 25
矩形(5x3): 15

printRepeated函数:
**********
----------
####################
```

**默认参数规则：**

- ✅ 默认参数必须从右到左连续
- ✅ 默认参数只能在函数声明或定义中指定一次
- ❌ 不能在中间跳过参数
- ❌ 默认参数不能在函数声明和定义中都指定

```cpp
// 正确
void func1(int a, int b = 10, int c = 20);

// 错误：默认参数不连续
// void func2(int a = 10, int b, int c = 20);

// 错误：默认参数在左边
// void func3(int a = 10, int b = 20, int c);
```

---

## 第7章 数组和集合

数组和集合是存储多个相同类型数据的容器。C++提供了传统的C风格数组和现代的STL容器（如vector）。

### 7.1 C风格数组

数组是存储固定数量相同类型元素的连续内存块。

**完整示例 - C风格数组基础：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== C风格数组示例 ===" << std::endl;

    // 声明并初始化数组
    int scores[5];  // 声明5个整数的数组

    // 逐个赋值
    scores[0] = 85;
    scores[1] = 90;
    scores[2] = 78;
    scores[3] = 92;
    scores[4] = 88;

    // 访问数组元素
    std::cout << "第一个分数: " << scores[0] << std::endl;
    std::cout << "第三个分数: " << scores[2] << std::endl;
    std::cout << "最后一个分数: " << scores[4] << std::endl;

    // 修改数组元素
    scores[2] = 95;
    std::cout << "修改后的第三个分数: " << scores[2] << std::endl;

    // 遍历数组
    std::cout << "\n所有分数: ";
    for (int i = 0; i < 5; i++) {
        std::cout << scores[i] << " ";
    }
    std::cout << std::endl;

    // 计算总分和平均分
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += scores[i];
    }
    double average = static_cast<double>(sum) / 5;
    std::cout << "总分: " << sum << std::endl;
    std::cout << "平均分: " << average << std::endl;

    return 0;
}
```

**重要提示：**

- ⚠️ 数组索引从0开始，不是1！
- ⚠️ 访问超出范围的索引会导致未定义行为
- ⚠️ 数组大小必须是编译时常量

### 7.2 数组初始化

**完整示例 - 数组初始化方式：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 数组初始化方式 ===" << std::endl;

    // 方式1：声明时完全初始化
    int numbers1[5] = {10, 20, 30, 40, 50};

    // 方式2：部分初始化（其余元素自动初始化为0）
    int numbers2[5] = {1, 2, 3};  // {1, 2, 3, 0, 0}

    // 方式3：让编译器推导大小
    int numbers3[] = {5, 10, 15, 20};  // 大小自动为4

    // 方式4：现代C++统一初始化（C++11）
    int numbers4[5]{1, 2, 3, 4, 5};

    // 方式5：全部初始化为0
    int numbers5[5] = {0};  // 或 int numbers5[5]{};

    // 打印各个数组
    std::cout << "numbers1: ";
    for (int i = 0; i < 5; i++) std::cout << numbers1[i] << " ";
    std::cout << std::endl;

    std::cout << "numbers2: ";
    for (int i = 0; i < 5; i++) std::cout << numbers2[i] << " ";
    std::cout << std::endl;

    std::cout << "numbers3: ";
    for (int i = 0; i < 4; i++) std::cout << numbers3[i] << " ";
    std::cout << std::endl;

    std::cout << "numbers4: ";
    for (int i = 0; i < 5; i++) std::cout << numbers4[i] << " ";
    std::cout << std::endl;

    std::cout << "numbers5: ";
    for (int i = 0; i < 5; i++) std::cout << numbers5[i] << " ";
    std::cout << std::endl;

    // 字符数组（字符串）
    char greeting[] = "Hello";  // 自动添加'\0'
    std::cout << "\n字符数组: " << greeting << std::endl;
    std::cout << "数组大小: " << sizeof(greeting) << " 字节" << std::endl;

    return 0;
}
```

### 7.3 遍历数组

**完整示例 - 数组遍历方法：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 数组遍历方法 ===" << std::endl;

    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);  // 计算数组大小

    // 方法1：使用索引的for循环
    std::cout << "方法1 - 索引for循环: ";
    for (int i = 0; i < size; i++) {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    // 方法2：基于范围的for循环（C++11，推荐）
    std::cout << "方法2 - 范围for循环: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 方法3：使用指针
    std::cout << "方法3 - 使用指针: ";
    for (int* ptr = numbers; ptr < numbers + size; ptr++) {
        std::cout << *ptr << " ";
    }
    std::cout << std::endl;

    // 查找最大值和最小值
    int max = numbers[0];
    int min = numbers[0];
    for (int num : numbers) {
        if (num > max) max = num;
        if (num < min) min = num;
    }
    std::cout << "\n最大值: " << max << std::endl;
    std::cout << "最小值: " << min << std::endl;

    return 0;
}
```

### 7.4 多维数组

**完整示例 - 二维数组：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 多维数组示例 ===" << std::endl;

    // 2D数组：3行4列
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // 访问单个元素
    std::cout << "matrix[0][0] = " << matrix[0][0] << std::endl;
    std::cout << "matrix[1][2] = " << matrix[1][2] << std::endl;
    std::cout << "matrix[2][3] = " << matrix[2][3] << std::endl;

    // 遍历2D数组
    std::cout << "\n完整矩阵:" << std::endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            std::cout << matrix[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    // 计算每行的和
    std::cout << "\n每行的和:" << std::endl;
    for (int i = 0; i < 3; i++) {
        int rowSum = 0;
        for (int j = 0; j < 4; j++) {
            rowSum += matrix[i][j];
        }
        std::cout << "第" << (i+1) << "行: " << rowSum << std::endl;
    }

    // 3D数组示例
    int cube[2][3][4] = {
        {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}},
        {{13,14,15,16}, {17,18,19,20}, {21,22,23,24}}
    };

    std::cout << "\n3D数组元素 cube[1][2][3] = " << cube[1][2][3] << std::endl;

    return 0;
}
```

### 7.5 向量（动态数组）

vector是C++标准库提供的动态数组，大小可以在运行时改变。

**完整示例 - vector基础：**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>  // for sort

int main() {
    std::cout << "=== vector示例 ===" << std::endl;

    // 创建空vector
    std::vector<int> scores;

    // 添加元素
    scores.push_back(85);
    scores.push_back(90);
    scores.push_back(78);
    scores.push_back(92);
    scores.push_back(88);

    std::cout << "分数: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 访问元素
    std::cout << "第一个分数: " << scores[0] << std::endl;
    std::cout << "最后一个分数: " << scores[scores.size()-1] << std::endl;
    std::cout << "使用at()访问: " << scores.at(2) << std::endl;

    // 获取大小
    std::cout << "\nvector大小: " << scores.size() << std::endl;
    std::cout << "vector容量: " << scores.capacity() << std::endl;
    std::cout << "是否为空: " << (scores.empty() ? "是" : "否") << std::endl;

    // 修改元素
    scores[2] = 95;
    std::cout << "\n修改后的分数: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 删除最后一个元素
    scores.pop_back();
    std::cout << "删除最后一个后: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 插入元素
    scores.insert(scores.begin() + 2, 100);  // 在索引2处插入100
    std::cout << "插入100后: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 排序
    std::sort(scores.begin(), scores.end());
    std::cout << "排序后: ";
    for (int score : scores) {
        std::cout << score << " ";
    }
    std::cout << std::endl;

    // 清空vector
    scores.clear();
    std::cout << "\n清空后大小: " << scores.size() << std::endl;

    // 使用初始化列表创建vector（C++11）
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::cout << "使用初始化列表: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 创建指定大小的vector
    std::vector<int> zeros(10, 0);  // 10个0
    std::cout << "10个0: ";
    for (int z : zeros) {
        std::cout << z << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

**数组 vs 向量对比：**

| 特性 | C风格数组 | std::vector |
|------|----------|-------------|
| 大小 | 固定（编译时） | 动态（运行时） |
| 内存分配 | 栈 | 堆 |
| 大小调整 | 不可以 | 可以 |
| 边界检查 | 无 | at()有检查 |
| 性能 | 略快 | 略慢 |
| 易用性 | 低 | 高 |
| 推荐使用 | 简单场景 | 大多数场景 |

**最佳实践：**

- ✅ 优先使用`std::vector`而不是C风格数组
- ✅ 使用`at()`而不是`[]`进行边界检查
- ✅ 使用范围for循环遍历
- ✅ 预留空间`reserve()`以提高性能
- ❌ 避免访问超出范围的索引

---

## 第8章 引用

引用是C++中非常重要的特性，它提供了一种更安全、更方便的方式来操作变量。

### 8.1 什么是引用？

引用是变量的别名，它与原变量共享同一块内存。引用必须在声明时初始化，且一旦绑定就不能改变。

**完整示例 - 引用基础：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 引用基础示例 ===" << std::endl;

    int x = 10;
    int& ref = x;  // ref是x的引用（别名）

    std::cout << "x = " << x << std::endl;
    std::cout << "ref = " << ref << std::endl;

    // 修改引用会影响原变量
    ref = 20;
    std::cout << "\n修改ref后:" << std::endl;
    std::cout << "x = " << x << std::endl;
    std::cout << "ref = " << ref << std::endl;

    // 引用和原变量的地址相同
    std::cout << "\n地址比较:" << std::endl;
    std::cout << "x的地址: " << &x << std::endl;
    std::cout << "ref的地址: " << &ref << std::endl;

    return 0;
}
```

### 8.2 引用作为函数参数

引用最常用于函数参数传递，可以避免复制大型对象，同时允许函数修改原始数据。

**完整示例 - 引用参数：**

```cpp
#include <iostream>

// 按值传递（复制）
void incrementByValue(int x) {
    x++;
    std::cout << "函数内部（按值）: " << x << std::endl;
}

// 按引用传递（不复制）
void incrementByReference(int& x) {
    x++;
    std::cout << "函数内部（按引用）: " << x << std::endl;
}

// const引用（只读）
void printByConstReference(const int& x) {
    std::cout << "const引用: " << x << std::endl;
    // x++;  // 错误！不能修改const引用
}

int main() {
    std::cout << "=== 引用作为函数参数 ===" << std::endl;

    int num = 10;

    std::cout << "原始值: " << num << std::endl;

    incrementByValue(num);
    std::cout << "调用按值传递后: " << num << " (未改变)" << std::endl;

    std::cout << std::endl;
    incrementByReference(num);
    std::cout << "调用按引用传递后: " << num << " (已改变)" << std::endl;

    std::cout << std::endl;
    printByConstReference(num);

    return 0;
}
```

### 8.3 引用 vs 指针

**对比表：**

| 特性 | 引用 | 指针 |
|------|------|------|
| 语法 | `int& ref = x` | `int* ptr = &x` |
| 必须初始化 | 是 | 否 |
| 可以重新绑定 | 否 | 是 |
| 可以为空 | 否 | 是（nullptr） |
| 访问值 | 直接使用 | 需要解引用`*ptr` |
| 安全性 | 更安全 | 较危险 |
| 推荐 | ✅ 优先使用 | 必要时使用 |

---

## 第9章 指针简介

指针是C++中最强大但也最容易出错的特性之一。理解指针对于掌握C++至关重要。

### 9.1 什么是指针？

指针是存储内存地址的变量。它允许我们通过地址间接访问或修改对象。

常用概念：
- &（取地址）获取变量的地址
- *（解引用）访问指针指向的值
- nullptr 表示空指针

### 9.2 指针语法

**完整示例 - 指针声明和使用：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 指针语法示例 ===" << std::endl;

    int x = 10;
    int y = 20;

    // 声明并初始化指针
    int* ptr1 = &x;  // ptr1 指向 x
    int* ptr2 = &y;  // ptr2 指向 y

    std::cout << "ptr1 指向的值: " << *ptr1 << std::endl;
    std::cout << "ptr2 指向的值: " << *ptr2 << std::endl;

    // 改变指针指向
    ptr1 = &y;  // 现在 ptr1 也指向 y
    std::cout << "\nptr1 改变指向后: " << *ptr1 << std::endl;

    // 通过指针修改值
    *ptr2 = 30;
    std::cout << "修改 *ptr2 后, y = " << y << std::endl;

    // 空指针
    int* ptr3 = nullptr;  // C++11推荐使用nullptr
    // int* ptr4 = NULL;   // 旧式写法
    // int* ptr5 = 0;      // 更旧的写法

    if (ptr3 == nullptr) {
        std::cout << "\nptr3 是空指针" << std::endl;
    }

    // 指针算术
    int arr[] = {1, 2, 3, 4, 5};
    int* p = arr;  // 数组名是指向第一个元素的指针

    std::cout << "\n指针算术:" << std::endl;
    std::cout << "*p = " << *p << std::endl;       // 1
    std::cout << "*(p+1) = " << *(p+1) << std::endl;  // 2
    std::cout << "*(p+2) = " << *(p+2) << std::endl;  // 3

    return 0;
}
```

**预期输出：**

```
=== 指针语法示例 ===
ptr1 指向的值: 10
ptr2 指向的值: 20

ptr1 改变指向后: 20
修改 *ptr2 后, y = 30

ptr3 是空指针

指针算术:
*p = 1
*(p+1) = 2
*(p+2) = 3
```

**关键概念：**

- `&` = 取地址运算符（"地址是多少？"）
- `*` = 解引用运算符（"地址处的值是什么？"）
- `int* ptr` = "ptr是指向int的指针"


### 9.3 指针与数组

数组名本质上是指向第一个元素的指针。

**完整示例 - 指针与数组：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 指针与数组示例 ===" << std::endl;

    int numbers[5] = {10, 20, 30, 40, 50};

    // 数组名是指向第一个元素的指针
    int* ptr = numbers;  // 等价于 int* ptr = &numbers[0];

    std::cout << "使用指针访问数组元素:" << std::endl;
    std::cout << "*ptr = " << *ptr << std::endl;           // 10
    std::cout << "*(ptr+1) = " << *(ptr+1) << std::endl;   // 20
    std::cout << "*(ptr+2) = " << *(ptr+2) << std::endl;   // 30

    // 指针算术
    std::cout << "\n指针算术:" << std::endl;
    std::cout << "ptr指向: " << *ptr << std::endl;  // 10
    ptr++;  // 移动到下一个元素
    std::cout << "ptr++后指向: " << *ptr << std::endl;  // 20
    ptr += 2;  // 再移动两个元素
    std::cout << "ptr+=2后指向: " << *ptr << std::endl;  // 40

    // 使用指针遍历数组
    std::cout << "\n使用指针遍历数组: ";
    ptr = numbers;  // 重置指针
    for (int i = 0; i < 5; i++) {
        std::cout << *(ptr + i) << " ";
    }
    std::cout << std::endl;

    // 数组下标实际上是指针运算
    std::cout << "\nnumbers[2] = " << numbers[2] << std::endl;
    std::cout << "*(numbers+2) = " << *(numbers+2) << std::endl;
    std::cout << "两者相同！" << std::endl;

    return 0;
}
```

### 9.4 指向对象的指针

**完整示例 - 指向对象的指针：**

```cpp
#include <iostream>
#include <string>

class Person {
public:
    std::string name;
    int age;

    void greet() {
        std::cout << "你好，我是 " << name << "，今年 " << age << " 岁" << std::endl;
    }

    void celebrateBirthday() {
        age++;
        std::cout << name << " 过生日了！现在 " << age << " 岁" << std::endl;
    }
};

int main() {
    std::cout << "=== 指向对象的指针示例 ===" << std::endl;

    Person person;
    person.name = "Alice";
    person.age = 25;

    // 创建指向对象的指针
    Person* ptr = &person;

    // 两种访问成员的方式
    std::cout << "使用点运算符: " << person.name << std::endl;
    std::cout << "使用箭头运算符: " << ptr->name << std::endl;

    // 通过指针调用方法
    ptr->greet();
    ptr->celebrateBirthday();

    // (*ptr).name 等价于 ptr->name
    std::cout << "\n(*ptr).age = " << (*ptr).age << std::endl;
    std::cout << "ptr->age = " << ptr->age << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 指向对象的指针示例 ===
使用点运算符: Alice
使用箭头运算符: Alice
你好，我是 Alice，今年 25 岁
Alice 过生日了！现在 26 岁

(*ptr).age = 26
ptr->age = 26
```

### 9.5 常见指针错误

**完整示例 - 指针错误和最佳实践：**

```cpp
#include <iostream>

// 错误示例1：未初始化的指针
void uninitializedPointerExample() {
    // int* ptr;  // 危险！指向随机内存
    // *ptr = 10;  // 未定义行为，可能崩溃

    // 正确做法
    int* ptr = nullptr;
    if (ptr != nullptr) {
        *ptr = 10;
    } else {
        std::cout << "指针为空，不能解引用" << std::endl;
    }
}

// 错误示例2：悬空指针
int* getDanglingPointer() {
    int x = 42;
    return &x;  // 危险！x在函数结束时被销毁
}

// 正确做法：返回值而不是指针
int getValue() {
    int x = 42;
    return x;
}

// 错误示例3：空指针解引用
void nullPointerExample() {
    int* ptr = nullptr;

    // 错误：解引用空指针
    // std::cout << *ptr << std::endl;  // 崩溃！

    // 正确：先检查
    if (ptr != nullptr) {
        std::cout << *ptr << std::endl;
    } else {
        std::cout << "指针为空" << std::endl;
    }
}

int main() {
    std::cout << "=== 指针错误示例 ===" << std::endl;

    uninitializedPointerExample();
    nullPointerExample();

    // 使用正确的函数
    int value = getValue();
    std::cout << "正确获取的值: " << value << std::endl;

    return 0;
}
```

**指针最佳实践：**

- ✅ 总是初始化指针（使用nullptr或有效地址）
- ✅ 使用前检查指针是否为nullptr
- ✅ 避免返回局部变量的地址
- ✅ 使用智能指针（std::unique_ptr, std::shared_ptr）代替原始指针
- ❌ 不要解引用空指针
- ❌ 不要使用未初始化的指针

---

## 第10章 类和对象简介

面向对象编程（OOP）是C++的核心特性之一。类和对象允许将数据与操作绑定在一起，支持抽象、封装、继承和多态。

### 10.1 什么是类？

类是创建对象的蓝图或模板。它定义了对象将拥有什么数据（成员变量/属性）和行为（成员函数/方法）。对象是类的具体实例。

**简短示例：**

```cpp
class Point {
public:
    int x, y;
    Point(int x, int y): x(x), y(y) {}
    void move(int dx, int dy) { x += dx; y += dy; }
};
```

### 10.2 简单的类示例

**完整示例 - 基本类定义和使用：**

```cpp
#include <iostream>
#include <string>

// 类定义
class Student {
public:  // 公有成员，可以从类外部访问
    // 成员变量（属性）
    std::string name;
    int age;
    double gpa;

    // 成员函数（方法）
    void displayInfo() {
        std::cout << "=== 学生信息 ===" << std::endl;
        std::cout << "姓名: " << name << std::endl;
        std::cout << "年龄: " << age << std::endl;
        std::cout << "GPA: " << gpa << std::endl;
    }

    // 另一个成员函数
    void study(std::string subject) {
        std::cout << name << " 正在学习 " << subject << std::endl;
    }

    // 判断是否优秀
    bool isExcellent() {
        return gpa >= 3.5;
    }
};

int main() {
    std::cout << "=== 类和对象示例 ===" << std::endl;

    // 创建对象（实例化）
    Student student1;

    // 设置对象的属性
    student1.name = "Alice";
    student1.age = 20;
    student1.gpa = 3.8;

    // 调用对象的方法
    student1.displayInfo();
    student1.study("C++编程");

    if (student1.isExcellent()) {
        std::cout << student1.name << " 是优秀学生！" << std::endl;
    }

    std::cout << std::endl;

    // 创建第二个对象
    Student student2;
    student2.name = "Bob";
    student2.age = 21;
    student2.gpa = 3.2;

    student2.displayInfo();
    student2.study("数据结构");

    if (!student2.isExcellent()) {
        std::cout << student2.name << " 需要继续努力！" << std::endl;
    }

    return 0;
}
```

**预期输出：**

```
=== 类和对象示例 ===
=== 学生信息 ===
姓名: Alice
年龄: 20
GPA: 3.8
Alice 正在学习 C++编程
Alice 是优秀学生！

=== 学生信息 ===
姓名: Bob
年龄: 21
GPA: 3.2
Bob 正在学习 数据结构
Bob 需要继续努力！
```

**更多类的示例：**

```cpp
#include <iostream>
#include <string>

// 矩形类
class Rectangle {
public:
    double width;
    double height;

    // 计算面积
    double getArea() {
        return width * height;
    }

    // 计算周长
    double getPerimeter() {
        return 2 * (width + height);
    }

    // 显示信息
    void display() {
        std::cout << "矩形: " << width << " x " << height << std::endl;
        std::cout << "面积: " << getArea() << std::endl;
        std::cout << "周长: " << getPerimeter() << std::endl;
    }
};

// 银行账户类
class BankAccount {
public:
    std::string accountNumber;
    std::string ownerName;
    double balance;

    // 存款
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            std::cout << "存入 " << amount << " 元，当前余额: " << balance << " 元" << std::endl;
        }
    }

    // 取款
    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            std::cout << "取出 " << amount << " 元，当前余额: " << balance << " 元" << std::endl;
        } else {
            std::cout << "余额不足或金额无效！" << std::endl;
        }
    }

    // 显示账户信息
    void displayAccount() {
        std::cout << "账户: " << accountNumber << std::endl;
        std::cout << "户主: " << ownerName << std::endl;
        std::cout << "余额: " << balance << " 元" << std::endl;
    }
};

int main() {
    std::cout << "=== 矩形类示例 ===" << std::endl;
    Rectangle rect;
    rect.width = 5.0;
    rect.height = 3.0;
    rect.display();

    std::cout << "\n=== 银行账户类示例 ===" << std::endl;
    BankAccount account;
    account.accountNumber = "123456789";
    account.ownerName = "张三";
    account.balance = 1000.0;

    account.displayAccount();
    std::cout << std::endl;

    account.deposit(500);
    account.withdraw(300);
    account.withdraw(2000);  // 余额不足

    std::cout << std::endl;
    account.displayAccount();

    return 0;
}
```

**预期输出：**

```
=== 矩形类示例 ===
矩形: 5 x 3
面积: 15
周长: 16

=== 银行账户类示例 ===
账户: 123456789
户主: 张三
余额: 1000 元

存入 500 元，当前余额: 1500 元
取出 300 元，当前余额: 1200 元
余额不足或金额无效！

账户: 123456789
户主: 张三
余额: 1200 元
```

### 10.3 访问修饰符

访问修饰符控制类成员的可见性和访问权限，是封装的关键。

**完整示例 - 访问修饰符：**

```cpp
#include <iostream>
#include <string>

class BankAccount {
private:  // 私有成员：只能在类内部访问
    double balance;
    std::string password;

    // 私有辅助函数
    bool verifyPassword(std::string pwd) const {
        return pwd == password;
    }

public:  // 公有成员：可以从任何地方访问
    std::string accountNumber;
    std::string ownerName;

    // 初始化账户
    void initialize(std::string accNum, std::string owner, std::string pwd) {
        accountNumber = accNum;
        ownerName = owner;
        password = pwd;
        balance = 0.0;
    }

    // 存款
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            std::cout << "存入成功！当前余额: " << balance << " 元" << std::endl;
        }
    }

    // 取款（需要密码）
    void withdraw(double amount, std::string pwd) {
        if (!verifyPassword(pwd)) {
            std::cout << "密码错误！" << std::endl;
            return;
        }
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            std::cout << "取款成功！当前余额: " << balance << " 元" << std::endl;
        } else {
            std::cout << "余额不足！" << std::endl;
        }
    }

    // 查询余额
    double getBalance() const {
        return balance;
    }
};

int main() {
    std::cout << "=== 访问修饰符示例 ===" << std::endl;

    BankAccount account;
    account.initialize("123456", "李四", "secret123");

    // 可以访问public成员
    std::cout << "账户: " << account.accountNumber << std::endl;

    // 不能直接访问private成员
    // account.balance = 1000;  // 错误！balance是私有的

    account.deposit(1000);
    account.withdraw(300, "secret123");
    account.withdraw(300, "wrong");  // 密码错误

    std::cout << "最终余额: " << account.getBalance() << " 元" << std::endl;

    return 0;
}
```

**访问级别：**

| 修饰符 | 类内部 | 派生类 | 类外部 |
|--------|--------|--------|--------|
| `public` | ✅ | ✅ | ✅ |
| `private` | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ❌ |

**最佳实践**：保持数据private，提供public函数访问。这称为**封装**。

### 10.4 构造函数和析构函数简介

构造函数在创建对象时自动调用，用于初始化对象。析构函数在对象销毁时自动调用，用于清理资源。

**完整示例 - 构造函数和析构函数：**

```cpp
#include <iostream>
#include <string>

class Rectangle {
private:
    double width;
    double height;
    std::string name;

public:
    // 构造函数 - 使用初始化列表
    Rectangle(double w, double h, std::string n) : width(w), height(h), name(n) {
        std::cout << "矩形 '" << name << "' 已创建 (" << width << "x" << height << ")" << std::endl;
    }

    // 默认构造函数
    Rectangle() : width(1.0), height(1.0), name("默认矩形") {
        std::cout << "默认矩形已创建" << std::endl;
    }

    // 析构函数 - 对象销毁时调用
    ~Rectangle() {
        std::cout << "矩形 '" << name << "' 已销毁" << std::endl;
    }

    double getArea() const {
        return width * height;
    }

    void display() const {
        std::cout << name << ": " << width << "x" << height
                  << ", 面积=" << getArea() << std::endl;
    }
};

int main() {
    std::cout << "=== 构造函数和析构函数示例 ===" << std::endl;

    Rectangle rect1(5.0, 3.0, "矩形1");
    rect1.display();

    std::cout << std::endl;

    Rectangle rect2;  // 调用默认构造函数
    rect2.display();

    std::cout << "\n程序结束，对象将被销毁..." << std::endl;

    return 0;
    // 析构函数在这里自动调用
}
```

**预期输出：**

```
=== 构造函数和析构函数示例 ===
矩形 '矩形1' 已创建 (5x3)
矩形1: 5x3, 面积=15

默认矩形已创建
默认矩形: 1x1, 面积=1

程序结束，对象将被销毁...
默认矩形 '默认矩形' 已销毁
矩形 '矩形1' 已销毁
```

**关键点：**

- 构造函数名与类名相同，无返回类型
- 析构函数名是`~类名`，无参数，无返回类型
- 对象离开作用域时自动调用析构函数
- 析构顺序与构造顺序相反（后进先出）

---

## 第11章 构造函数和析构函数

构造函数和析构函数是类的特殊成员函数，用于对象的初始化和清理。

### 11.1 构造函数

构造函数是在创建对象时自动调用的特殊成员函数，用于初始化对象的状态；析构函数在对象生命周期结束时自动调用，用于清理资源。

**完整示例 - 构造函数基本用法：**

```cpp
#include <iostream>

class Point {
public:
    int x, y;
    // 构造函数，用于初始化成员
    Point(int x, int y) : x(x), y(y) {}
};

int main() {
    Point p(1, 2);  // 调用构造函数
    std::cout << p.x << "," << p.y << std::endl;  // 输出 1,2
    return 0;
}
```


### 11.2 析构函数

析构函数在对象销毁时自动调用，用于清理资源（如释放内存、关闭文件等）。

**完整示例 - 析构函数：**

```cpp
#include <iostream>
#include <string>

class Resource {
private:
    std::string name;
    int* data;

public:
    // 构造函数
    Resource(std::string n, int size) : name(n) {
        data = new int[size];
        std::cout << "Resource '" << name << "' 创建，分配了 " << size << " 个整数" << std::endl;
    }

    // 析构函数
    ~Resource() {
        delete[] data;
        std::cout << "Resource '" << name << "' 销毁，内存已释放" << std::endl;
    }

    void setData(int index, int value) {
        data[index] = value;
    }

    int getData(int index) const {
        return data[index];
    }
};

void demonstrateLifetime() {
    std::cout << "进入函数" << std::endl;
    Resource r1("局部资源", 10);
    r1.setData(0, 42);
    std::cout << "数据: " << r1.getData(0) << std::endl;
    std::cout << "离开函数" << std::endl;
}  // r1在这里被销毁，析构函数自动调用

int main() {
    std::cout << "=== 析构函数示例 ===" << std::endl;

    {
        Resource r1("块作用域资源", 5);
    }  // r1离开作用域，析构函数调用

    std::cout << "\n调用函数:" << std::endl;
    demonstrateLifetime();

    std::cout << "\n创建多个对象:" << std::endl;
    Resource* r2 = new Resource("动态资源", 20);
    delete r2;  // 手动删除，调用析构函数

    std::cout << "\n程序结束" << std::endl;
    return 0;
}
```

**预期输出：**

```
=== 析构函数示例 ===
Resource '块作用域资源' 创建，分配了 5 个整数
Resource '块作用域资源' 销毁，内存已释放

调用函数:
进入函数
Resource '局部资源' 创建，分配了 10 个整数
数据: 42
离开函数
Resource '局部资源' 销毁，内存已释放

创建多个对象:
Resource '动态资源' 创建，分配了 20 个整数
Resource '动态资源' 销毁，内存已释放

程序结束
```

### 11.3 初始化列表

初始化列表是初始化成员变量的推荐方式，比在构造函数体内赋值更高效。

**完整示例 - 初始化列表：**

```cpp
#include <iostream>
#include <string>

class Point {
private:
    const int id;  // const成员必须用初始化列表
    double x, y;

public:
    // 使用初始化列表（推荐）
    Point(int i, double x_val, double y_val) : id(i), x(x_val), y(y_val) {
        std::cout << "Point " << id << " 创建于 (" << x << ", " << y << ")" << std::endl;
    }

    void display() const {
        std::cout << "Point " << id << ": (" << x << ", " << y << ")" << std::endl;
    }
};

class Rectangle {
private:
    Point topLeft;
    Point bottomRight;

public:
    // 初始化成员对象
    Rectangle(int id1, double x1, double y1, int id2, double x2, double y2)
        : topLeft(id1, x1, y1), bottomRight(id2, x2, y2) {
        std::cout << "Rectangle 创建" << std::endl;
    }

    void display() const {
        std::cout << "矩形:" << std::endl;
        topLeft.display();
        bottomRight.display();
    }
};

int main() {
    std::cout << "=== 初始化列表示例 ===" << std::endl;

    Point p1(1, 10.0, 20.0);
    p1.display();

    std::cout << std::endl;
    Rectangle rect(2, 0.0, 10.0, 3, 20.0, 0.0);
    rect.display();

    return 0;
}
```

**预期输出：**

```
=== 初始化列表示例 ===
Point 1 创建于 (10, 20)
Point 1: (10, 20)

Point 2 创建于 (0, 10)
Point 3 创建于 (20, 0)
Rectangle 创建
矩形:
Point 2: (0, 10)
Point 3: (20, 0)
```


## 第12章 拷贝语义

拷贝语义定义了对象如何被复制。理解浅拷贝和深拷贝对于管理动态内存至关重要。

### 12.1 浅拷贝 vs 深拷贝

**完整示例 - 浅拷贝问题：**

```cpp
#include <iostream>
#include <cstring>

class ShallowString {
private:
    char* data;

public:
    ShallowString(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
        std::cout << "构造: " << data << std::endl;
    }

    // 使用默认拷贝构造函数（浅拷贝）
    // ShallowString(const ShallowString& other) = default;

    ~ShallowString() {
        std::cout << "析构: " << data << std::endl;
        delete[] data;
    }

    void print() const {
        std::cout << "数据: " << data << std::endl;
    }
};

void demonstrateShallowCopy() {
    std::cout << "=== 浅拷贝问题 ===" << std::endl;
    ShallowString s1("Hello");
    // ShallowString s2 = s1;  // 浅拷贝！两个对象共享同一个data指针
    // 当s1和s2销毁时，会尝试两次delete同一块内存！（崩溃）
}

int main() {
    demonstrateShallowCopy();
    return 0;
}
```

**完整示例 - 深拷贝解决方案：**

```cpp
#include <iostream>
#include <cstring>

class DeepString {
private:
    char* data;
    int length;

public:
    // 构造函数
    DeepString(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        std::cout << "构造: '" << data << "'" << std::endl;
    }

    // 拷贝构造函数（深拷贝）
    DeepString(const DeepString& other) {
        length = other.length;
        data = new char[length + 1];  // 分配新内存
        strcpy(data, other.data);     // 复制数据
        std::cout << "拷贝构造: '" << data << "'" << std::endl;
    }

    // 拷贝赋值运算符（深拷贝）
    DeepString& operator=(const DeepString& other) {
        std::cout << "拷贝赋值: '" << other.data << "'" << std::endl;

        if (this != &other) {  // 检查自赋值
            delete[] data;  // 释放旧内存

            length = other.length;
            data = new char[length + 1];  // 分配新内存
            strcpy(data, other.data);     // 复制数据
        }
        return *this;
    }

    // 析构函数
    ~DeepString() {
        std::cout << "析构: '" << data << "'" << std::endl;
        delete[] data;
    }

    void print() const {
        std::cout << "数据: '" << data << "', 长度: " << length << std::endl;
    }

    void modify(char newChar) {
        if (length > 0) {
            data[0] = newChar;
        }
    }
};

int main() {
    std::cout << "=== 深拷贝示例 ===" << std::endl;

    DeepString s1("Hello");
    s1.print();

    std::cout << "\n拷贝构造:" << std::endl;
    DeepString s2 = s1;  // 调用拷贝构造函数
    s2.print();

    std::cout << "\n修改s2:" << std::endl;
    s2.modify('J');
    s1.print();  // s1不受影响
    s2.print();  // s2被修改

    std::cout << "\n拷贝赋值:" << std::endl;
    DeepString s3("World");
    s3 = s1;  // 调用拷贝赋值运算符
    s3.print();

    std::cout << "\n程序结束，对象将被销毁:" << std::endl;
    return 0;
}
```

**预期输出：**

```
=== 深拷贝示例 ===
构造: 'Hello'
数据: 'Hello', 长度: 5

拷贝构造:
拷贝构造: 'Hello'
数据: 'Hello', 长度: 5

修改s2:
数据: 'Hello', 长度: 5
数据: 'Jello', 长度: 5

拷贝赋值:
构造: 'World'
拷贝赋值: 'Hello'
数据: 'Hello', 长度: 5

程序结束，对象将被销毁:
析构: 'Hello'
析构: 'Jello'
析构: 'Hello'
```

### 12.2 三法则（Rule of Three）

如果一个类需要自定义以下任何一个，通常需要自定义全部三个：

1. 析构函数
2. 拷贝构造函数
3. 拷贝赋值运算符

**完整示例 - 三法则：**

```cpp
#include <iostream>
#include <cstring>

class DynamicArray {
private:
    int* data;
    int size;

public:
    // 1. 构造函数
    DynamicArray(int s) : size(s) {
        data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = 0;
        }
        std::cout << "构造函数: 创建大小为 " << size << " 的数组" << std::endl;
    }

    // 2. 析构函数
    ~DynamicArray() {
        std::cout << "析构函数: 释放大小为 " << size << " 的数组" << std::endl;
        delete[] data;
    }

    // 3. 拷贝构造函数（深拷贝）
    DynamicArray(const DynamicArray& other) : size(other.size) {
        data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
        std::cout << "拷贝构造函数: 复制大小为 " << size << " 的数组" << std::endl;
    }

    // 4. 拷贝赋值运算符（深拷贝）
    DynamicArray& operator=(const DynamicArray& other) {
        std::cout << "拷贝赋值运算符" << std::endl;

        if (this != &other) {  // 防止自赋值
            // 释放旧资源
            delete[] data;

            // 分配新资源
            size = other.size;
            data = new int[size];

            // 复制数据
            for (int i = 0; i < size; i++) {
                data[i] = other.data[i];
            }
        }
        return *this;
    }

    void set(int index, int value) {
        if (index >= 0 && index < size) {
            data[index] = value;
        }
    }

    int get(int index) const {
        if (index >= 0 && index < size) {
            return data[index];
        }
        return -1;
    }

    void print() const {
        std::cout << "数组: [";
        for (int i = 0; i < size; i++) {
            std::cout << data[i];
            if (i < size - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

int main() {
    std::cout << "=== 三法则示例 ===" << std::endl;

    DynamicArray arr1(5);
    arr1.set(0, 10);
    arr1.set(1, 20);
    arr1.set(2, 30);
    arr1.print();

    std::cout << "\n拷贝构造:" << std::endl;
    DynamicArray arr2 = arr1;
    arr2.print();

    std::cout << "\n修改arr2:" << std::endl;
    arr2.set(0, 99);
    arr1.print();  // arr1不受影响
    arr2.print();

    std::cout << "\n拷贝赋值:" << std::endl;
    DynamicArray arr3(3);
    arr3 = arr1;
    arr3.print();

    std::cout << "\n程序结束:" << std::endl;
    return 0;
}
```

**预期输出：**

```
=== 三法则示例 ===
构造函数: 创建大小为 5 的数组
数组: [10, 20, 30, 0, 0]

拷贝构造:
拷贝构造函数: 复制大小为 5 的数组
数组: [10, 20, 30, 0, 0]

修改arr2:
数组: [10, 20, 30, 0, 0]
数组: [99, 20, 30, 0, 0]

拷贝赋值:
构造函数: 创建大小为 3 的数组
拷贝赋值运算符
数组: [10, 20, 30, 0, 0]

程序结束:
析构函数: 释放大小为 5 的数组
析构函数: 释放大小为 5 的数组
析构函数: 释放大小为 5 的数组
```

**浅拷贝 vs 深拷贝对比：**

| 特性 | 浅拷贝 | 深拷贝 |
|------|--------|--------|
| 指针复制 | 复制指针值 | 复制指针指向的数据 |
| 内存 | 共享同一块内存 | 各自独立的内存 |
| 修改影响 | 互相影响 | 互不影响 |
| 析构问题 | 重复释放（崩溃） | 各自释放（安全） |
| 默认行为 | 是 | 否（需手动实现） |

**最佳实践：**

- ✅ 遵循三法则：定义析构函数时，也定义拷贝构造和拷贝赋值
- ✅ 在拷贝赋值中检查自赋值
- ✅ 使用智能指针避免手动内存管理
- ✅ C++11后考虑五法则（增加移动构造和移动赋值）
- ❌ 不要依赖默认拷贝行为处理动态内存

---

## 第13章 动态内存管理

动态内存管理允许程序在运行时分配和释放内存，提供了更大的灵活性。

### 13.1 new和delete

`new`和`delete`运算符用于在堆上动态分配和释放内存。

**完整示例 - 动态内存分配：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== 动态内存分配示例 ===" << std::endl;

    // 分配单个整数
    int* ptr = new int;  // 分配内存
    *ptr = 42;           // 赋值
    std::cout << "动态分配的整数: " << *ptr << std::endl;
    delete ptr;          // 释放内存

    // 分配并初始化
    int* ptr2 = new int(100);
    std::cout << "初始化的整数: " << *ptr2 << std::endl;
    delete ptr2;

    // 分配数组
    int size = 5;
    int* arr = new int[size];  // 分配数组
    for (int i = 0; i < size; i++) {
        arr[i] = i * 10;
    }

    std::cout << "\n动态数组: ";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    delete[] arr;  // 释放数组（注意使用delete[]）

    // 分配对象
    class Point {
    public:
        int x, y;
        Point(int x, int y) : x(x), y(y) {
            std::cout << "Point构造: (" << x << ", " << y << ")" << std::endl;
        }
        ~Point() {
            std::cout << "Point析构: (" << x << ", " << y << ")" << std::endl;
        }
    };

    Point* p = new Point(10, 20);
    std::cout << "Point: (" << p->x << ", " << p->y << ")" << std::endl;
    delete p;

    return 0;
}
```

**预期输出：**

```
=== 动态内存分配示例 ===
动态分配的整数: 42
初始化的整数: 100

动态数组: 0 10 20 30 40
Point构造: (10, 20)
Point: (10, 20)
Point析构: (10, 20)
```

### 13.2 内存泄漏

内存泄漏发生在分配的内存没有被正确释放时。

**完整示例 - 内存泄漏和正确做法：**

```cpp
#include <iostream>

// 错误：内存泄漏
void memoryLeak() {
    int* ptr = new int(42);
    std::cout << "分配内存: " << *ptr << std::endl;
    // 忘记delete！内存泄漏
}

// 正确：释放内存
void noLeak() {
    int* ptr = new int(42);
    std::cout << "分配内存: " << *ptr << std::endl;
    delete ptr;  // 正确释放
    std::cout << "内存已释放" << std::endl;
}

// 错误：循环中的内存泄漏
void leakInLoop() {
    for (int i = 0; i < 5; i++) {
        int* ptr = new int(i);
        // 每次循环都分配新内存，但从不释放
    }
    // 泄漏了5个int的内存
}

// 正确：在循环中正确管理内存
void noLeakInLoop() {
    for (int i = 0; i < 5; i++) {
        int* ptr = new int(i);
        std::cout << *ptr << " ";
        delete ptr;  // 每次循环都释放
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "=== 内存泄漏示例 ===" << std::endl;

    std::cout << "\n正确的内存管理:" << std::endl;
    noLeak();

    std::cout << "\n循环中的正确做法:" << std::endl;
    noLeakInLoop();

    // memoryLeak();  // 不要调用，会泄漏内存
    // leakInLoop();  // 不要调用，会泄漏内存

    return 0;
}
```

**常见内存错误：**

1. **内存泄漏**：分配后忘记释放
2. **重复释放**：对同一指针多次delete
3. **悬空指针**：使用已释放的内存
4. **数组释放错误**：用delete释放new[]分配的数组

### 13.3 智能指针

智能指针自动管理内存，避免内存泄漏和悬空指针问题。

**完整示例 - 智能指针：**

```cpp
#include <iostream>
#include <memory>
#include <string>

class Person {
public:
    std::string name;
    Person(std::string n) : name(n) {
        std::cout << "Person '" << name << "' 创建" << std::endl;
    }
    ~Person() {
        std::cout << "Person '" << name << "' 销毁" << std::endl;
    }
};

int main() {
    std::cout << "=== 智能指针示例 ===" << std::endl;

    // 1. unique_ptr - 独占所有权
    std::cout << "\n1. unique_ptr（独占所有权）:" << std::endl;
    {
        std::unique_ptr<Person> p1(new Person("Alice"));
        // 或使用make_unique（C++14）
        auto p2 = std::make_unique<Person>("Bob");

        std::cout << "p1: " << p1->name << std::endl;
        std::cout << "p2: " << p2->name << std::endl;

        // unique_ptr不能复制
        // std::unique_ptr<Person> p3 = p1;  // 错误！

        // 但可以移动
        std::unique_ptr<Person> p3 = std::move(p1);
        std::cout << "p3: " << p3->name << std::endl;
        // p1现在为空

    }  // 离开作用域，自动delete

    // 2. shared_ptr - 共享所有权
    std::cout << "\n2. shared_ptr（共享所有权）:" << std::endl;
    {
        std::shared_ptr<Person> s1 = std::make_shared<Person>("Charlie");
        std::cout << "引用计数: " << s1.use_count() << std::endl;

        {
            std::shared_ptr<Person> s2 = s1;  // 可以复制
            std::cout << "引用计数: " << s1.use_count() << std::endl;
            std::cout << "s1: " << s1->name << std::endl;
            std::cout << "s2: " << s2->name << std::endl;
        }  // s2销毁，引用计数减1

        std::cout << "引用计数: " << s1.use_count() << std::endl;
    }  // s1销毁，引用计数为0，对象被delete

    // 3. weak_ptr - 弱引用
    std::cout << "\n3. weak_ptr（弱引用）:" << std::endl;
    {
        std::shared_ptr<Person> s1 = std::make_shared<Person>("David");
        std::weak_ptr<Person> w1 = s1;  // 弱引用，不增加引用计数

        std::cout << "shared_ptr引用计数: " << s1.use_count() << std::endl;

        if (auto temp = w1.lock()) {  // 尝试获取shared_ptr
            std::cout << "对象仍然存在: " << temp->name << std::endl;
        }
    }

    std::cout << "\n程序结束" << std::endl;
    return 0;
}
```

**预期输出：**

```
=== 智能指针示例 ===

1. unique_ptr（独占所有权）:
Person 'Alice' 创建
Person 'Bob' 创建
p1: Alice
p2: Bob
p3: Alice
Person 'Bob' 销毁
Person 'Alice' 销毁

2. shared_ptr（共享所有权）:
Person 'Charlie' 创建
引用计数: 1
引用计数: 2
s1: Charlie
s2: Charlie
引用计数: 1
Person 'Charlie' 销毁

3. weak_ptr（弱引用）:
Person 'David' 创建
shared_ptr引用计数: 1
对象仍然存在: David
Person 'David' 销毁

程序结束
```

**智能指针选择指南：**

| 智能指针 | 使用场景 |
|---------|---------|
| `unique_ptr` | 独占所有权，最常用 |
| `shared_ptr` | 需要共享所有权时 |
| `weak_ptr` | 打破循环引用 |

**最佳实践：**

- ✅ 优先使用`unique_ptr`
- ✅ 使用`make_unique`和`make_shared`
- ✅ 使用`weak_ptr`打破循环引用
- ❌ 避免混用智能指针和原始指针
| 重绑定 | 不可以 | 可以 |
| 初始化 | 必须 | 可选 |
| 安全性 | 更安全 | 较危险 |
| 推荐 | ✅ 优先使用 | 必要时使用 |

---

## 第14章 类型转换

C++提供了四种类型转换运算符，比C风格的强制转换更安全、更明确。

### 14.1 static_cast

`static_cast`用于编译时已知的类型转换，是最常用的转换方式。

**完整示例 - static_cast：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== static_cast 示例 ===" << std::endl;

    // 1. 基本类型转换
    std::cout << "\n1. 基本类型转换:" << std::endl;
    int i = 10;
    double d = static_cast<double>(i);  // int转double
    std::cout << "int: " << i << " -> double: " << d << std::endl;

    double pi = 3.14159;
    int truncated = static_cast<int>(pi);  // double转int（截断）
    std::cout << "double: " << pi << " -> int: " << truncated << std::endl;

    // 2. 指针类型转换（相关类型）
    std::cout << "\n2. 指针类型转换:" << std::endl;
    int num = 42;
    void* voidPtr = &num;  // int*隐式转换为void*
    int* intPtr = static_cast<int*>(voidPtr);  // void*转回int*
    std::cout << "通过void*转换: " << *intPtr << std::endl;

    // 3. 类层次结构中的向上转换（安全）
    std::cout << "\n3. 类层次结构转换:" << std::endl;
    class Base {
    public:
        virtual void show() { std::cout << "Base" << std::endl; }
    };

    class Derived : public Base {
    public:
        void show() override { std::cout << "Derived" << std::endl; }
    };

    Derived d_obj;
    Base* basePtr = static_cast<Base*>(&d_obj);  // 向上转换（安全）
    basePtr->show();

    return 0;
}
```

**预期输出：**

```
=== static_cast 示例 ===

1. 基本类型转换:
int: 10 -> double: 10
double: 3.14159 -> int: 3

2. 指针类型转换:
通过void*转换: 42

3. 类层次结构转换:
Derived
```

### 14.2 dynamic_cast

`dynamic_cast`用于继承层次中的安全向下转换，在运行时进行类型检查。

**完整示例 - dynamic_cast：**

```cpp
#include <iostream>
#include <string>

class Animal {
public:
    std::string name;
    Animal(std::string n) : name(n) {}
    virtual ~Animal() {}  // 需要虚析构函数才能使用dynamic_cast
    virtual void speak() { std::cout << "Some sound" << std::endl; }
};

class Dog : public Animal {
public:
    Dog(std::string n) : Animal(n) {}
    void speak() override { std::cout << name << ": Woof!" << std::endl; }
    void fetch() { std::cout << name << " is fetching!" << std::endl; }
};

class Cat : public Animal {
public:
    Cat(std::string n) : Animal(n) {}
    void speak() override { std::cout << name << ": Meow!" << std::endl; }
    void climb() { std::cout << name << " is climbing!" << std::endl; }
};

int main() {
    std::cout << "=== dynamic_cast 示例 ===" << std::endl;

    Dog dog("Buddy");
    Cat cat("Whiskers");

    Animal* animal1 = &dog;
    Animal* animal2 = &cat;

    // 尝试向下转换
    std::cout << "\n尝试将animal1转换为Dog:" << std::endl;
    Dog* dogPtr = dynamic_cast<Dog*>(animal1);
    if (dogPtr) {
        std::cout << "转换成功！" << std::endl;
        dogPtr->fetch();
    } else {
        std::cout << "转换失败" << std::endl;
    }

    std::cout << "\n尝试将animal2转换为Dog:" << std::endl;
    Dog* dogPtr2 = dynamic_cast<Dog*>(animal2);
    if (dogPtr2) {
        std::cout << "转换成功！" << std::endl;
    } else {
        std::cout << "转换失败（animal2实际是Cat）" << std::endl;
    }

    std::cout << "\n尝试将animal2转换为Cat:" << std::endl;
    Cat* catPtr = dynamic_cast<Cat*>(animal2);
    if (catPtr) {
        std::cout << "转换成功！" << std::endl;
        catPtr->climb();
    }

    return 0;
}
```

**预期输出：**

```
=== dynamic_cast 示例 ===

尝试将animal1转换为Dog:
转换成功！
Buddy is fetching!

尝试将animal2转换为Dog:
转换失败（animal2实际是Cat）

尝试将animal2转换为Cat:
转换成功！
Whiskers is climbing!
```

### 14.3 const_cast

`const_cast`用于添加或移除const限定符。通常用于与旧代码接口交互。

**完整示例 - const_cast：**

```cpp
#include <iostream>
#include <cstring>

void processString(char* str) {
    // 旧式API，需要非const指针
    std::cout << "处理字符串: " << str << std::endl;
}

int main() {
    std::cout << "=== const_cast 示例 ===" << std::endl;

    const char* constStr = "Hello, World!";

    // 移除const（危险！仅用于与旧API交互）
    char* nonConstStr = const_cast<char*>(constStr);
    processString(nonConstStr);

    // 注意：修改原本const的数据是未定义行为！
    // nonConstStr[0] = 'h';  // 危险！可能崩溃

    // 更安全的做法：复制到可修改的缓冲区
    char buffer[50];
    strcpy(buffer, constStr);
    buffer[0] = 'h';
    std::cout << "修改后: " << buffer << std::endl;

    return 0;
}
```

**预期输出：**

```
=== const_cast 示例 ===
处理字符串: Hello, World!
修改后: hello, World!
```

### 14.4 reinterpret_cast

`reinterpret_cast`进行低级的位模式重新解释，非常危险。

**完整示例 - reinterpret_cast：**

```cpp
#include <iostream>
#include <cstdint>

int main() {
    std::cout << "=== reinterpret_cast 示例 ===" << std::endl;

    int num = 42;
    int* ptr = &num;

    // 将指针转换为整数（查看地址）
    std::uintptr_t addr = reinterpret_cast<std::uintptr_t>(ptr);
    std::cout << "指针地址: " << ptr << std::endl;
    std::cout << "地址的整数表示: " << addr << std::endl;

    // 将整数转换回指针
    int* ptr2 = reinterpret_cast<int*>(addr);
    std::cout << "转换回指针: " << ptr2 << std::endl;
    std::cout << "值: " << *ptr2 << std::endl;

    // 危险用法：重新解释内存
    double d = 3.14159;
    long long* llPtr = reinterpret_cast<long long*>(&d);
    std::cout << "\ndouble的位模式（作为long long）: " << *llPtr << std::endl;

    return 0;
}
```

**预期输出：**

```
=== reinterpret_cast 示例 ===
指针地址: 0x7ffc8b2a3c4c
地址的整数表示: 140722635234380
转换回指针: 0x7ffc8b2a3c4c
值: 42

double的位模式（作为long long）: 4614256656552045848
```

### 14.5 转换选择指南

**完整示例 - 转换对比：**

```cpp
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;
    double gpa;

public:
    // 1. 默认构造函数
    Student() : name("Unknown"), age(0), gpa(0.0) {
        std::cout << "默认构造函数调用" << std::endl;
    }

    // 2. 带参数构造函数
    Student(std::string n, int a) : name(n), age(a), gpa(0.0) {
        std::cout << "带参数构造函数调用: " << name << std::endl;
    }

    // 3. 完整参数构造函数
    Student(std::string n, int a, double g) : name(n), age(a), gpa(g) {
        std::cout << "完整构造函数调用: " << name << std::endl;
    }

    // 4. 拷贝构造函数
    Student(const Student& other) : name(other.name), age(other.age), gpa(other.gpa) {
        std::cout << "拷贝构造函数调用: " << name << std::endl;
    }

    void display() const {
        std::cout << "  姓名: " << name << ", 年龄: " << age << ", GPA: " << gpa << std::endl;
    }
};

int main() {
    std::cout << "=== 构造函数示例 ===" << std::endl;

    Student s1;  // 调用默认构造函数
    s1.display();

    std::cout << std::endl;
    Student s2("Alice", 20);  // 调用带参数构造函数
    s2.display();

    std::cout << std::endl;
    Student s3("Bob", 21, 3.8);  // 调用完整构造函数
    s3.display();

    std::cout << std::endl;
    Student s4 = s3;  // 调用拷贝构造函数
    s4.display();

    return 0;
}
```

**预期输出：**

```
=== 构造函数示例 ===
默认构造函数调用
  姓名: Unknown, 年龄: 0, GPA: 0

带参数构造函数调用: Alice
  姓名: Alice, 年龄: 20, GPA: 0

完整构造函数调用: Bob
  姓名: Bob, 年龄: 21, GPA: 3.8

拷贝构造函数调用: Bob
  姓名: Bob, 年龄: 21, GPA: 3.8
```




## 第15章 内联函数

内联函数是C++的一种优化机制，可以减少函数调用开销。

### 15.1 什么是内联函数？

内联函数是对编译器的优化建议：在调用处直接展开函数体，以减少调用开销。是否真正内联由编译器决定。

要点：
- 在类内定义的成员函数天然是内联候选
- 使用 inline 关键字表达意图，但不强制
- 适用于体积小、逻辑简单、频繁调用的函数；递归/复杂控制流通常不会被内联

**完整示例 - 内联自由函数与内联成员：**

```cpp
#include <iostream>

inline int add(int a, int b) { return a + b; }

struct Rect {
    int w{0}, h{0};
    inline int area() const { return w * h; } // 类内定义，内联候选
};

int main() {
    std::cout << "=== 内联函数示例 ===\n";
    std::cout << add(2, 3) << "\n"; // 5
    Rect r{3, 4};
    std::cout << r.area() << "\n";  // 12
}
```

**何时使用内联：**
- 小且频繁调用的工具函数（如访问器、简单计算）
- 不要为追求“零开销”而滥用；现代编译器会自行做更优的决定







## 第16章 Lambda表达式

Lambda表达式（也称为匿名函数）是C++11引入的重要特性，它允许我们在需要函数对象的地方定义内联的、匿名的函数。Lambda表达式使代码更简洁、更易读，特别是在使用STL算法时。

### 16.1 Lambda表达式基础

Lambda表达式的基本语法如下：

```cpp
[捕获列表](参数列表) -> 返回类型 { 函数体 }
```

**语法组成部分：**

| 部分 | 说明 | 是否必需 |
|------|------|---------|
| `[捕获列表]` | 指定如何捕获外部变量 | 必需 |
| `(参数列表)` | 函数参数，类似普通函数 | 可选（无参数时可省略） |
| `-> 返回类型` | 指定返回类型 | 可选（编译器可推导） |
| `{ 函数体 }` | 函数的实现代码 | 必需 |

**完整示例 - Lambda基础：**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::cout << "=== Lambda表达式基础 ===" << std::endl;

    // 最简单的lambda：无参数，无捕获
    auto hello = []() {
        std::cout << "Hello from lambda!" << std::endl;
    };
    hello();  // 调用lambda

    // 带参数的lambda
    auto add = [](int a, int b) {
        return a + b;
    };
    std::cout << "5 + 3 = " << add(5, 3) << std::endl;

    // 显式指定返回类型
    auto divide = [](double a, double b) -> double {
        if (b != 0) {
            return a / b;
        }
        return 0.0;
    };
    std::cout << "10.0 / 3.0 = " << divide(10.0, 3.0) << std::endl;

    // 直接使用lambda（不赋值给变量）
    std::cout << "7 * 6 = " << [](int a, int b) { return a * b; }(7, 6) << std::endl;

    // 在STL算法中使用lambda
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    std::cout << "\n偶数: ";
    std::for_each(numbers.begin(), numbers.end(), [](int n) {
        if (n % 2 == 0) {
            std::cout << n << " ";
        }
    });
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== Lambda表达式基础 ===
Hello from lambda!
5 + 3 = 8
10.0 / 3.0 = 3.33333
7 * 6 = 42

偶数: 2 4 6 8 10
```

### 16.2 捕获列表详解

捕获列表决定了lambda如何访问外部作用域的变量。这是lambda最强大也最重要的特性。

**捕获方式：**

| 捕获语法 | 说明 | 示例 |
|---------|------|------|
| `[]` | 不捕获任何变量 | `[]() { }` |
| `[=]` | 按值捕获所有外部变量 | `[=]() { }` |
| `[&]` | 按引用捕获所有外部变量 | `[&]() { }` |
| `[x]` | 按值捕获变量x | `[x]() { }` |
| `[&x]` | 按引用捕获变量x | `[&x]() { }` |
| `[=, &x]` | 按值捕获所有变量，但x按引用捕获 | `[=, &x]() { }` |
| `[&, x]` | 按引用捕获所有变量，但x按值捕获 | `[&, x]() { }` |
| `[this]` | 捕获当前对象的this指针 | `[this]() { }` |

**完整示例 - 捕获列表：**

```cpp
#include <iostream>

int main() {
    std::cout << "=== Lambda捕获列表 ===" << std::endl;

    int x = 10;
    int y = 20;

    // 1. 不捕获任何变量
    auto lambda1 = []() {
        std::cout << "不能访问外部变量" << std::endl;
        // std::cout << x << std::endl;  // 错误！
    };
    lambda1();

    // 2. 按值捕获（复制）
    auto lambda2 = [x]() {
        std::cout << "按值捕获 x = " << x << std::endl;
        // x++;  // 错误！按值捕获的变量是const的
    };
    lambda2();

    // 3. 按值捕获，使用mutable关键字允许修改
    auto lambda3 = [x]() mutable {
        x++;  // 可以修改，但不影响外部的x
        std::cout << "lambda内部 x = " << x << std::endl;
    };
    lambda3();
    std::cout << "外部 x = " << x << " (未改变)" << std::endl;

    // 4. 按引用捕获
    auto lambda4 = [&x]() {
        x++;  // 直接修改外部的x
        std::cout << "lambda内部修改后 x = " << x << std::endl;
    };
    lambda4();
    std::cout << "外部 x = " << x << " (已改变)" << std::endl;

    // 5. 捕获多个变量
    auto lambda5 = [x, y]() {
        std::cout << "x = " << x << ", y = " << y << std::endl;
    };
    lambda5();

    // 6. 混合捕获
    auto lambda6 = [=, &y]() {  // 所有变量按值捕获，y按引用捕获
        std::cout << "x(值) = " << x << ", y(引用) = " << y << std::endl;
        y++;  // 可以修改y
    };
    lambda6();
    std::cout << "修改后 y = " << y << std::endl;

    // 7. 按值捕获所有变量
    int a = 1, b = 2, c = 3;
    auto lambda7 = [=]() {
        std::cout << "a = " << a << ", b = " << b << ", c = " << c << std::endl;
    };
    lambda7();

    // 8. 按引用捕获所有变量
    auto lambda8 = [&]() {
        a++; b++; c++;
        std::cout << "全部加1后: a = " << a << ", b = " << b << ", c = " << c << std::endl;
    };
    lambda8();

    return 0;
}
```

**预期输出：**

```
=== Lambda捕获列表 ===
不能访问外部变量
按值捕获 x = 10
lambda内部 x = 11
外部 x = 10 (未改变)
lambda内部修改后 x = 11
外部 x = 11 (已改变)
x = 11, y = 20
x(值) = 11, y(引用) = 20
修改后 y = 21
a = 1, b = 2, c = 3
全部加1后: a = 2, b = 3, c = 4
```

### 16.3 Lambda表达式的实际应用

Lambda表达式在实际编程中非常有用，特别是与STL算法结合使用时。

**完整示例 - Lambda实际应用：**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    std::cout << "=== Lambda实际应用 ===" << std::endl;

    // 示例1：排序
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};

    std::cout << "原始数组: ";
    for (int n : numbers) std::cout << n << " ";
    std::cout << std::endl;

    // 使用lambda进行降序排序
    std::sort(numbers.begin(), numbers.end(), [](int a, int b) {
        return a > b;  // 降序
    });

    std::cout << "降序排序: ";
    for (int n : numbers) std::cout << n << " ";
    std::cout << std::endl;

    // 示例2：查找和计数
    std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // 计算大于5的元素个数
    int count = std::count_if(data.begin(), data.end(), [](int n) {
        return n > 5;
    });
    std::cout << "\n大于5的元素个数: " << count << std::endl;

    // 查找第一个偶数
    auto it = std::find_if(data.begin(), data.end(), [](int n) {
        return n % 2 == 0;
    });
    if (it != data.end()) {
        std::cout << "第一个偶数: " << *it << std::endl;
    }

    // 示例3：转换
    std::vector<int> values = {1, 2, 3, 4, 5};
    std::vector<int> squared(values.size());

    // 计算平方
    std::transform(values.begin(), values.end(), squared.begin(), [](int n) {
        return n * n;
    });

    std::cout << "\n原始值: ";
    for (int n : values) std::cout << n << " ";
    std::cout << "\n平方值: ";
    for (int n : squared) std::cout << n << " ";
    std::cout << std::endl;

    // 示例4：字符串处理
    std::vector<std::string> words = {"apple", "banana", "cherry", "date", "elderberry"};

    // 查找长度大于5的单词
    std::cout << "\n长度大于5的单词: ";
    std::for_each(words.begin(), words.end(), [](const std::string& word) {
        if (word.length() > 5) {
            std::cout << word << " ";
        }
    });
    std::cout << std::endl;

    // 示例5：使用捕获的变量
    int threshold = 50;
    std::vector<int> scores = {45, 67, 89, 34, 78, 56, 90, 23};

    std::cout << "\n分数阈值: " << threshold << std::endl;
    std::cout << "及格的分数: ";
    std::for_each(scores.begin(), scores.end(), [threshold](int score) {
        if (score >= threshold) {
            std::cout << score << " ";
        }
    });
    std::cout << std::endl;

    // 示例6：修改容器元素
    std::vector<int> nums = {1, 2, 3, 4, 5};

    std::cout << "\n原始: ";
    for (int n : nums) std::cout << n << " ";

    // 每个元素乘以2
    std::for_each(nums.begin(), nums.end(), [](int& n) {
        n *= 2;
    });

    std::cout << "\n乘以2后: ";
    for (int n : nums) std::cout << n << " ";
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== Lambda实际应用 ===
原始数组: 5 2 8 1 9 3 7 4 6
降序排序: 9 8 7 6 5 4 3 2 1

大于5的元素个数: 5
第一个偶数: 2

原始值: 1 2 3 4 5
平方值: 1 4 9 16 25

长度大于5的单词: banana cherry elderberry

分数阈值: 50
及格的分数: 67 89 78 56 90

原始: 1 2 3 4 5
乘以2后: 2 4 6 8 10
```

### 16.4 Lambda与函数对象、函数指针的对比

Lambda表达式是函数对象的语法糖，但比传统的函数对象和函数指针更简洁。

**完整示例 - 三种方式对比：**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// 方法1：普通函数
bool isEven(int n) {
    return n % 2 == 0;
}

// 方法2：函数对象（仿函数）
class IsEvenFunctor {
public:
    bool operator()(int n) const {
        return n % 2 == 0;
    }
};

// 方法3：带状态的函数对象
class GreaterThan {
private:
    int threshold;
public:
    GreaterThan(int t) : threshold(t) {}
    bool operator()(int n) const {
        return n > threshold;
    }
};

int main() {
    std::cout << "=== Lambda vs 函数对象 vs 函数指针 ===" << std::endl;

    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // 方法1：使用函数指针
    std::cout << "方法1 - 函数指针，偶数: ";
    std::for_each(numbers.begin(), numbers.end(), [](int n) {
        if (isEven(n)) std::cout << n << " ";
    });
    std::cout << std::endl;

    // 方法2：使用函数对象
    std::cout << "方法2 - 函数对象，偶数: ";
    IsEvenFunctor isEvenFunc;
    std::for_each(numbers.begin(), numbers.end(), [&isEvenFunc](int n) {
        if (isEvenFunc(n)) std::cout << n << " ";
    });
    std::cout << std::endl;

    // 方法3：使用Lambda（最简洁）
    std::cout << "方法3 - Lambda，偶数: ";
    std::for_each(numbers.begin(), numbers.end(), [](int n) {
        if (n % 2 == 0) std::cout << n << " ";
    });
    std::cout << std::endl;

    // 带状态的比较
    int threshold = 5;

    // 使用函数对象
    std::cout << "\n使用函数对象，大于" << threshold << ": ";
    GreaterThan gt(threshold);
    std::for_each(numbers.begin(), numbers.end(), [&gt](int n) {
        if (gt(n)) std::cout << n << " ";
    });
    std::cout << std::endl;

    // 使用Lambda（更简洁）
    std::cout << "使用Lambda，大于" << threshold << ": ";
    std::for_each(numbers.begin(), numbers.end(), [threshold](int n) {
        if (n > threshold) std::cout << n << " ";
    });
    std::cout << std::endl;

    return 0;
}
```

**预期输出：**

```
=== Lambda vs 函数对象 vs 函数指针 ===
方法1 - 函数指针，偶数: 2 4 6 8 10
方法2 - 函数对象，偶数: 2 4 6 8 10
方法3 - Lambda，偶数: 2 4 6 8 10

使用函数对象，大于5: 6 7 8 9 10
使用Lambda，大于5: 6 7 8 9 10
```

**Lambda表达式的优势：**

- ✅ **简洁**：代码更短，更易读
- ✅ **就地定义**：在使用的地方直接定义，无需单独声明
- ✅ **捕获变量**：可以方便地访问外部变量
- ✅ **类型推导**：编译器自动推导返回类型
- ✅ **现代C++风格**：符合现代C++编程习惯

**Lambda表达式最佳实践：**

- ✅ 对于简单的、一次性使用的函数，优先使用lambda
- ✅ 保持lambda简短（通常不超过5行）
- ✅ 明确指定捕获方式，避免使用`[=]`或`[&]`捕获所有变量
- ✅ 对于复杂逻辑，考虑使用命名函数
- ⚠️ 注意按引用捕获的生命周期问题
- ⚠️ 避免在lambda中捕获this指针后，对象已被销毁的情况

---

## 第17章 左值和右值

左值（lvalue）和右值（rvalue）是C++中的基本概念，理解它们对于掌握现代C++的移动语义至关重要。C++11引入的右值引用和移动语义大大提高了程序的性能。

### 17.1 左值和右值的定义

**基本概念：**

- **左值（lvalue）**：可以出现在赋值语句左边的表达式，有持久的内存地址，可以取地址
- **右值（rvalue）**：只能出现在赋值语句右边的表达式，临时的、即将销毁的值，不能取地址

**简单判断方法：**

- 能对表达式取地址（`&`）→ 左值
- 不能对表达式取地址 → 右值

**完整示例 - 左值和右值：**

```cpp
#include <iostream>

int getValue() {
    return 42;
}

int& getReference() {
    static int value = 100;
    return value;
}

int main() {
    std::cout << "=== 左值和右值 ===" << std::endl;

    // 左值示例
    int x = 10;           // x是左值
    int y = 20;           // y是左值
    int* ptr = &x;        // 可以取x的地址，x是左值

    std::cout << "左值示例:" << std::endl;
    std::cout << "x = " << x << ", 地址: " << &x << std::endl;
    std::cout << "y = " << y << ", 地址: " << &y << std::endl;

    // 右值示例
    int z = 5 + 3;        // 5 + 3 是右值（临时值）
    // int* p = &(5 + 3); // 错误！不能取右值的地址

    std::cout << "\n右值示例:" << std::endl;
    std::cout << "z = " << z << std::endl;
    // std::cout << &(x + y) << std::endl;  // 错误！x + y是右值

    // 函数返回值
    int a = getValue();      // getValue()返回右值
    // int* p2 = &getValue(); // 错误！不能取右值的地址

    int& ref = getReference();  // getReference()返回左值引用
    int* p3 = &getReference();  // 可以！返回的是左值
    std::cout << "\ngetReference()返回的值: " << ref << std::endl;

    // 字符串字面量是左值（特殊情况）
    const char* str = "Hello";  // "Hello"是左值
    std::cout << "\n字符串字面量地址: " << (void*)str << std::endl;

    // 更多示例
    std::cout << "\n更多示例:" << std::endl;

    // 左值
    int arr[5] = {1, 2, 3, 4, 5};
    std::cout << "arr[0]是左值，地址: " << &arr[0] << std::endl;

    // 右值
    int result = arr[0] + arr[1];  // arr[0] + arr[1]是右值
    std::cout << "result = " << result << std::endl;

    return 0;
}
```

**预期输出：**

```
=== 左值和右值 ===
左值示例:
x = 10, 地址: 0x...
y = 20, 地址: 0x...

右值示例:
z = 8

getReference()返回的值: 100

字符串字面量地址: 0x...

更多示例:
arr[0]是左值，地址: 0x...
result = 3
```

### 17.2 左值引用和右值引用

C++11引入了右值引用，用`&&`表示，与传统的左值引用`&`相对应。

**引用类型对比：**

| 引用类型 | 语法 | 可以绑定到 | 用途 |
|---------|------|-----------|------|
| 左值引用 | `T&` | 左值 | 传统引用，修改原对象 |
| const左值引用 | `const T&` | 左值和右值 | 只读引用，常用于函数参数 |
| 右值引用 | `T&&` | 右值 | 移动语义，完美转发 |

**完整示例 - 左值引用和右值引用：**

```cpp
#include <iostream>
#include <string>

void processLvalue(int& x) {
    std::cout << "处理左值引用: " << x << std::endl;
    x++;
}

void processConstLvalue(const int& x) {
    std::cout << "处理const左值引用: " << x << std::endl;
    // x++;  // 错误！不能修改const引用
}

void processRvalue(int&& x) {
    std::cout << "处理右值引用: " << x << std::endl;
    x++;  // 可以修改右值引用
}

// 函数重载：区分左值和右值
void process(int& x) {
    std::cout << "调用左值版本" << std::endl;
}

void process(int&& x) {
    std::cout << "调用右值版本" << std::endl;
}

int main() {
    std::cout << "=== 左值引用和右值引用 ===" << std::endl;

    int x = 10;

    // 左值引用
    int& lref = x;           // 可以：绑定到左值
    // int& lref2 = 5;       // 错误！不能绑定到右值

    std::cout << "左值引用: lref = " << lref << std::endl;

    // const左值引用（可以绑定到右值）
    const int& clref = 20;   // 可以：const左值引用可以绑定到右值
    std::cout << "const左值引用: clref = " << clref << std::endl;

    // 右值引用
    // int&& rref = x;       // 错误！不能绑定到左值
    int&& rref = 30;         // 可以：绑定到右值
    std::cout << "右值引用: rref = " << rref << std::endl;

    // 右值引用本身是左值！
    int&& rref2 = 40;
    int& lref3 = rref2;      // 可以：rref2作为表达式是左值
    std::cout << "rref2 = " << rref2 << ", lref3 = " << lref3 << std::endl;

    // 函数调用
    std::cout << "\n函数调用示例:" << std::endl;

    int value = 100;
    processLvalue(value);           // 传递左值
    processConstLvalue(value);      // 传递左值
    processConstLvalue(200);        // 传递右值（const引用可以）
    processRvalue(300);             // 传递右值
    // processRvalue(value);        // 错误！不能传递左值

    // 函数重载
    std::cout << "\n函数重载示例:" << std::endl;
    int num = 50;
    process(num);                   // 调用左值版本
    process(60);                    // 调用右值版本

    return 0;
}
```

**预期输出：**

```
=== 左值引用和右值引用 ===
左值引用: lref = 10
const左值引用: clref = 20
右值引用: rref = 30
rref2 = 40, lref3 = 40

函数调用示例:
处理左值引用: 100
处理const左值引用: 100
处理const左值引用: 200
处理右值引用: 300

函数重载示例:
调用左值版本
调用右值版本
```

### 17.3 移动语义（Move Semantics）

移动语义是C++11最重要的特性之一，它允许资源从一个对象"移动"到另一个对象，而不是复制，从而提高性能。

**为什么需要移动语义？**

传统的拷贝操作会复制所有数据，对于大型对象（如包含大量数据的容器）来说，这是非常昂贵的。移动语义允许我们"窃取"临时对象的资源，避免不必要的复制。

**完整示例 - 移动语义：**

```cpp
#include <iostream>
#include <string>
#include <vector>

class MyString {
private:
    char* data;
    size_t length;

public:
    // 构造函数
    MyString(const char* str = "") {
        length = std::strlen(str);
        data = new char[length + 1];
        std::strcpy(data, str);
        std::cout << "构造: \"" << data << "\"" << std::endl;
    }

    // 拷贝构造函数（深拷贝）
    MyString(const MyString& other) {
        length = other.length;
        data = new char[length + 1];
        std::strcpy(data, other.data);
        std::cout << "拷贝构造: \"" << data << "\"" << std::endl;
    }

    // 移动构造函数（窃取资源）
    MyString(MyString&& other) noexcept {
        data = other.data;        // 窃取指针
        length = other.length;

        other.data = nullptr;     // 将源对象置空
        other.length = 0;

        std::cout << "移动构造: \"" << data << "\"" << std::endl;
    }

    // 拷贝赋值运算符
    MyString& operator=(const MyString& other) {
        if (this != &other) {
            delete[] data;
            length = other.length;
            data = new char[length + 1];
            std::strcpy(data, other.data);
            std::cout << "拷贝赋值: \"" << data << "\"" << std::endl;
        }
        return *this;
    }

    // 移动赋值运算符
    MyString& operator=(MyString&& other) noexcept {
        if (this != &other) {
            delete[] data;

            data = other.data;
            length = other.length;

            other.data = nullptr;
            other.length = 0;

            std::cout << "移动赋值: \"" << data << "\"" << std::endl;
        }
        return *this;
    }

    // 析构函数
    ~MyString() {
        if (data) {
            std::cout << "析构: \"" << data << "\"" << std::endl;
            delete[] data;
        } else {
            std::cout << "析构: (空对象)" << std::endl;
        }
    }

    void print() const {
        if (data) {
            std::cout << "内容: \"" << data << "\"" << std::endl;
        } else {
            std::cout << "内容: (空)" << std::endl;
        }
    }
};

MyString createString() {
    MyString temp("临时字符串");
    return temp;  // 返回临时对象，触发移动
}

int main() {
    std::cout << "=== 移动语义示例 ===" << std::endl;

    // 示例1：拷贝 vs 移动
    std::cout << "\n1. 拷贝构造:" << std::endl;
    MyString s1("Hello");
    MyString s2 = s1;  // 拷贝构造

    std::cout << "\n2. 移动构造:" << std::endl;
    MyString s3 = MyString("World");  // 移动构造（从临时对象）

    std::cout << "\n3. 拷贝赋值:" << std::endl;
    MyString s4;
    s4 = s1;  // 拷贝赋值

    std::cout << "\n4. 移动赋值:" << std::endl;
    MyString s5;
    s5 = MyString("Temporary");  // 移动赋值（从临时对象）

    std::cout << "\n5. 函数返回值（移动）:" << std::endl;
    MyString s6 = createString();  // 移动构造

    std::cout << "\n6. 检查对象状态:" << std::endl;
    s1.print();
    s2.print();
    s3.print();

    std::cout << "\n程序结束，开始析构:" << std::endl;
    return 0;
}
```

**预期输出：**

```
=== 移动语义示例 ===

1. 拷贝构造:
构造: "Hello"
拷贝构造: "Hello"

2. 移动构造:
构造: "World"
移动构造: "World"
析构: (空对象)

3. 拷贝赋值:
构造: ""
拷贝赋值: "Hello"

4. 移动赋值:
构造: ""
构造: "Temporary"
移动赋值: "Temporary"
析构: (空对象)

5. 函数返回值（移动）:
构造: "临时字符串"
移动构造: "临时字符串"
析构: (空对象)

6. 检查对象状态:
内容: "Hello"
内容: "Hello"
内容: "World"

程序结束，开始析构:
析构: "临时字符串"
析构: "Temporary"
析构: ""
析构: "World"
析构: "Hello"
析构: "Hello"
```

✅ **基础知识**：变量、数据类型、运算符、控制流
✅ **函数**：声明、定义、参数传递、重载
✅ **数据结构**：数组、vector、字符串
✅ **面向对象**：类、对象、封装、构造/析构函数
✅ **指针和引用**：内存管理、动态分配
✅ **高级特性**：智能指针、拷贝语义、类型转换、内联函数

### 下一步学习建议

1. **深入学习**：继承、多态、虚函数、抽象类
2. **现代C++**：C++11/14/17/20新特性（auto、lambda、移动语义等）
3. **标准库**：STL容器、算法、迭代器
4. **实践项目**：通过实际项目巩固知识
5. **最佳实践**：代码规范、设计模式、性能优化

**记住**：编程是一门实践的艺术，多写代码、多思考、多总结！

祝你在C++学习之路上越走越远！🚀
