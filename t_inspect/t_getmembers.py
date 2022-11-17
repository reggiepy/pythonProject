# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/11/17 14:08
import inspect

import t_inspect.t_class as t_class

if __name__ == '__main__':

    members = inspect.getmembers(t_class.TClass)
    for member in members:
        func_name, func_type = member
        print(f"{inspect.ismethod(func_type)} {func_name}")
        if inspect.isfunction(func_type):
            print("function".center(100, "-"))
            print(func_type.__qualname__)
            sig = inspect.signature(getattr(t_class.TClass, func_name))
            print(sig.parameters)
            print(func_name, func_type)
            print("-" * 100)
        if isinstance(func_type, property):
            print("property".center(100, "-"))
            print(func_name, func_type)
            print("-" * 100)
    for member in members:
        func_name, func_type = member
        if inspect.isfunction(func_type):
            continue
        if func_name in ["show"]:
            print("other".center(100, "-"))
            print(inspect.ismethod(func_type))
            print(inspect.getsource(func_type))
            print(func_name, func_type)
            print("-" * 100)
