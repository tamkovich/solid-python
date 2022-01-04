"""keep the content of a subclass clean from elements of no use to that subclass"""

from abc import ABC, abstractmethod


class Walker(ABC):
    @staticmethod
    @abstractmethod
    def walk():
        print("Can Walk")


class Swimmer(ABC):
    @staticmethod
    @abstractmethod
    def swim():
        print("Can Swim")


class Human(Walker, Swimmer):
    @staticmethod
    def walk():
        print("Humans can walk")

    @staticmethod
    def swim():
        print("Humans can swim")


class Whale(Swimmer):
    @staticmethod
    def swim():
        print("Whales can swim")


if __name__ == "__main__":
    Human.walk()
    Human.swim()

    Whale.swim()
    Whale.walk()  # error because whale can't swim
