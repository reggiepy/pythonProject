# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/11/17 14:06


class TClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        return f"{self.a} {self.b}"

    @property
    def print2(self):
        return self.print()

    @classmethod
    def show(cls):
        print("fasdfsdf")

    @staticmethod
    def show2():
        print("fasdfsdf")
