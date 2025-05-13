from typing import Callable
from typing import Union
from typing import TypeVar
import struct

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

class Png:
    """ chaining pattern simple example"""
    def __init__(self, path):
        self.path = path

    def open(self):
        self.file = open(self.path, 'rb')
        return self

    def size(self):
        self.file.seek(16)
        head = self.file.read(8)
        width, height = struct.unpack('>ii', head)
        self.file.seek(0)
        return width, height
    
class Plugin:
    """ registry pattern simple example """

    def __init__(self, name):
        self.name = name

    def activated(self):
        print(f"Plugin {self.name} is activated")

    def registered(self):
        print(f"Plugin {self.name} is registered")

    def unregistered(self):
        print(f"Plugin {self.name} is unregistered")

    def disabled(self):
        print(f"Plugin {self.name} is disable")

    def do_stuff(self):
        print(f"Plugin {self.name} is doing something")
    
    def __repr__(self):
        return f'Plugin {self.name}'

class PluginRegistry:
    def __init__(self):
        self.available_plugins = {}
        self.activate_plugins = {}

    def add(self, plugin):
        self.available_plugins[plugin.name] = plugin
        plugin.registered()

    def remove(self, name):
        plugin = self.available_plugins.pop(name, None)
        self.activate_plugins.pop(name, None)
        if plugin:
            plugin.unregistered()
    
    def activate(self, name):
        plugin = self.available_plugins.get(name)
        if plugin:
            self.activate_plugins[name] = plugin
            plugin.activated()

    def deactivate(self, name):
        plugin = self.activate_plugins.pop(name, None)
        if plugin:
            plugin.disabled()
    
    def get(self, name, include_inactive=False):
        if include_inactive:
            return self.available_plugins.get(name)
        return self.activate_plugins.get(name)


class InformalParserInterface:

  def load_data_source(self, path:str, file_name:str) -> str:
    pass

  def extract_text(self, file_name:str) -> dict:
    pass


class PdfParser(InformalParserInterface):
  def load_data_source(self, path:str, file_name:str) -> str:
    """Overrides InformalParserInterface.load_data_source()"""
    pass

  def extract_text(self, file_name:str) -> dict:
    """Overrides InformalParserInterface.extract_text()"""
    pass


class EmailParser(InformalParserInterface):
  def load_data_source(self, path:str, file_name:str) -> str:
    pass

  def extract_text(self, file_name:str) -> dict:
    pass


class ParserMeta(type):
  
  def __instancecheck_(cls, instance):
    return cls.__subclasscheck__(type(instance))

  def __subclasscheck__(cls, subclass):
    return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass


class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))

class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

if __name__ == '__main__':
    obj = MyClass()
    # print(obj)
    # print(obj.custom_name)
    # print(obj.func("Philippe"))

    obj = TestTypeChecker(any_value=12)
    print(obj)

     image = Png("biz.png").open().size()
    print(image)
    registry = PluginRegistry()
    registry.add(Plugin('test'))
    registry.add(Plugin('foo'))

    registry.activate('test')

    plug = registry.get(name='test')
    plug.do_stuff()

    print(registry.available_plugins, registry.activate_plugins)
    registry.deactivate('test')
    print(registry.available_plugins, registry.activate_plugins)
    registry.remove('foo')
    print(registry.available_plugins)
