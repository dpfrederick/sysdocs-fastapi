# Guidelines

All classes should either be an abstract base class or be sealed and non-iheritable. This will prevent confusion and inheritance hell as we progress.

## Classes

All classes should be defined in their own file. The file name should be the same as the class name, but in snake case. For example, the `Person` class should be defined in a file named `person.py`.

## Inheritance

### Abstract Base Classes

To create an abstract class, we use the Abstract Base Class (`ABC`)from the built-in `abc` module. This is a metaclass that allows us to define abstract methods and properties. Any class that inherits from an abstract class must implement all abstract methods and properties.

Abstract methods are defined using the `@abstractmethod` decorator. This decorator can be used on both methods and properties and should be the last decorator before the method or property definition.

All abstract class definitions should be named `ABC<Type>` and be defined in a file named `abc_<type>.py`. For example, the `Person` class should be defined in a file named `abc_person.py`.

Example Abstract Base Class in file `abc_person.py`:
```python

from abc import ABC, abstractmethod

class ABCPerson(ABC):
    @property
    @abstractmethod
    def role(self) -> str:
        pass

    @abstractmethod
    def get_message(self) -> str:
        pass
```

### Concrete Classes

Concrete classes can inherit from one or base classes. Class that inherit from Abstract Base Classes essentially implement an interface pattern and can use the ABC as an interface. This will make it easier to use the classes in a polymorphic way.

All concerte class should also be marked as `final` using the `@final` decorator from the `final` module. This will prevent the class from being inherited from.

Example usage in file `manager.py`:
```python
from abc_person import ABCPerson

from typing import final

@final
class Manager(ABCPerson):
    def __init__(self, name: str):
        self.name = name

    @property
    def role(self) -> str:
        return "Manager"

    def get_message(self) -> str:
        return f"Hello, my name is {self.name} and I am a {self.role}."
```

### Data classes

Data classes are classes that are used to store data. They should be used in place of dictionaries or tuples. Data classes should inherit from `dataclass` from the built-in `dataclasses` module. This will allow us to define the class fields using type hints. This will also allow us to define the `__init__` method and `__repr__` method.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    role: str


person = Person("John", 30, "Manager")
```