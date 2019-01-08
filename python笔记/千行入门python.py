# _*_ coding: utf-8 _*_

"""类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算"""

#-- 寻求帮助：
    dir(obj)            # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
    help(obj.func)      # 查询obj.func的具体介绍和用法
    
#-- 测试类型的三种方法，推荐第三种
    if type(L) == type([]): print("L is list")
    if type(L) == list: print("L is list")
    if isinstance(L, list): print("L is list")

#-- Python数据类型：哈希类型、不可哈希类型
    # 哈希类型，即在原地不能改变的变量类型，不可变类型。可利用hash函数查看其hash值，也可以作为字典的key
        "数字类型：int, float, decimal.Decimal, fractions.Fraction, complex"
        "字符串类型：str, bytes"
        "元组：tuple"
        "冻结集合：frozenset"
        "布尔类型：True, False"
        "None"
    # 不可hash类型：原地可变类型：list、dict和set。它们不可以作为字典的key。

#-- 数字常量
    1234, -1234, 0, 999999999                    # 整数
    1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
    0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字
    3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
    hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
    int(str, base)                               # 将字符串转化为整数，base为进制数
    # 2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用l或L结尾，迫使一般整数成为长整数
    float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数

#-- 数字的表达式操作符
    yield x                                      # 生成器函数发送协议
    lambda args: expression                      # 生成匿名函数
    x if y else z                                # 三元选择表达式
    x and y, x or y, not x                       # 逻辑与、逻辑或、逻辑非
    x in y, x not in y                           # 成员对象测试
    x is y, x is not y                           # 对象实体测试
    x<y, x<=y, x>y, x>=y, x==y, x!=y             # 大小比较，集合子集或超集值相等性操作符
    1 < a < 3                                    # Python中允许连续比较
    x|y, x&y, x^y                                # 位或、位与、位异或
    x<<y, x>>y                                   # 位操作：x左移、右移y位
    +, -, *, /, //, %, **                        # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
    -x, +x, ~x                                   # 一元减法、识别、按位求补（取反）
    x[i], x[i:j:k], x(……)                        # 索引、分片、调用
    int(3.14),  float(3)                         # 强制类型转换
   