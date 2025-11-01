#include <iostream>

// 错误示例1：缺少分号
int main() {
    std::cout << "Hello" ; // 错误：缺少分号
    return 0;
}
// 解决：在语句末尾添加分号

// 错误示例2：拼写错误
/*
int main() {
    std::cuot << "Hello" << std::endl;  // 错误：cout拼写错误
    return 0;
}
// 解决：改为std::cout
*/

// 正确的程序
int main() {
  std::cout << "Hello, World!" << std::endl;
  return 0;
}
