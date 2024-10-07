from typing import Callable
from typing import Union
from typing import TypeVar

_CustomType = TypeVar("_CustomType", str, int, Callable, bytes)
_T = TypeVar("_T")

class TypeChecker(object):

    def __init__(self, cls) -> None:
        self.cls = cls

    def __get__(self, instance: _T | None = None, owner: type[_T] | None = None, /):
        obj_attrs = getattr(self.cls)
        print(obj_attrs, "in get method-()")

    def __call__(self, *args, **kwargs):
        # obj_attrs = getattr(self.cls)
        # print(obj_attrs, "in get method-()")
        print(dir(self.cls))
        return self.cls(*args, **kwargs)

@TypeChecker
class TestTypeChecker:
    def __init__(self, any_value:any) -> None:
        self._any_value = any_value

    def __getstate__(self) -> object:
        pass

class Encapsulation(object):

    def __init__(self) -> None:
        self.__protected_var = 10
        self._private_var = 50

    @classmethod
    def my_function(cls, value:str):
        return f"My name is {value}"

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.custom_name = "NewClass"
        cls.func:Callable = cls.my_function
        setattr(cls, "my_function", cls.func)
        print(f"Subclass created {cls.__name__}")

    def __repr__(self) -> str:
        return f"Class is {self.custom_name}" 
    
    def __str__(self) -> str:
        return f"MyClass is good"


class MyClass(Encapsulation):
    def __init__(self) -> None:
        super().__init__()
        self.value_private = self._Encapsulation__protected_var + self._private_var


if __name__ == '__main__':
    obj = MyClass()
    # print(obj)
    # print(obj.custom_name)
    # print(obj.func("Philippe"))

    obj = TestTypeChecker(any_value=12)
    print(obj)
