import inspect

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say(self):
        print("I speak Booooo")


class Dog(Animal):
    # @classmethod
    def say(self):
        print("I speak Booooo")


if __name__ == '__main__':

    if issubclass(Animal, ABC):
        print("'Animal' is an abstract class")

    if '@abstractmethod' in inspect.getsource(Animal.say):
        print("'say' is an abstract method")

    if issubclass(Dog, Animal):
        print("'Dog' is dervied from 'Animal' class")

    d1 = Dog()
    print("Dog,'d1', says :", d1.say())