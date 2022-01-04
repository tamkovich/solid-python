"""The Interface Segregation Principle (ISP)

Many client-specific interfaces are better than one general-purpose interface
"""

from abc import ABC, abstractmethod


class Mammals(ABC):
    @staticmethod
    @abstractmethod
    def swim():
        print("Can Swim")

    @staticmethod
    @abstractmethod
    def walk():
        print("Can Walk")


class Human(Mammals):
    @staticmethod
    def swim():
        return print("Humans can swim")

    @staticmethod
    def walk():
        return print("Humans can walk")


class Whale(Mammals):
    @staticmethod
    def swim():
        return print("Whales can swim")


if __name__ == '__main__':
    Human.swim()
    Human.walk()

    Whale.swim()
    Whale.walk()
