# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/11/14 17:32


class A:
    b = 2

    def __init__(self):
        self.a = 1

    def to_do(self):
        return self.a + self.b


class B:
    def to_do(self):
        result = super().to_do()
        return result * 2


class C(B, A):
    pass


if __name__ == '__main__':
    c = C()
    print(c.to_do())
