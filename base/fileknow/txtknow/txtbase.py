# -*- coding:utf-8 -*-
# 键盘输入往文件写入文本
def write_to_file(path):
    F = open(path, "a")
    while True:
        text = input("(输入n终止):")
        if text == "n":
            break
        F.write(text + "\n")  # write function takes exactly 1 arguement so concatenation
    F.close()


if __name__ == '__main__':
    write_to_file('./test.txt')
