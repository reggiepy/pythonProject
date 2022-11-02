# -*- coding: utf-8 -*-
import random


class Father:
    def __new__(cls, *args, sub_type=None, **kwargs):
        if sub_type == "Son1":
            subclass = Son1
        elif sub_type == "Son2":
            subclass = Son2
        else:
            subclass = random.choice(cls.__subclasses__())
        return subclass


class Son1(Father):
    _type = "Son1"

    @classmethod
    def type(cls):
        return cls._type


class Son2(Father):
    _type = "Son2"

    @classmethod
    def type(cls):
        return cls._type


if __name__ == '__main__':
    a = Father(sub_type="Son2")
    print(a)
