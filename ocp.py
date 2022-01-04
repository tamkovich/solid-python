"""The Open–closed principle (OCP)

Software entities … should be open for extension but closed for modification
"""

import numpy as np
from abc import ABC, abstractmethod


class Operations(ABC):
    """Operations"""
    @staticmethod
    @abstractmethod
    def operation(*args, **kwargs):
        pass


class Mean(Operations):
    """Compute Max"""

    @staticmethod
    def operation(list_):
        print(f"The mean is {np.mean(list_)}")


class Max(Operations):
    """Compute Max"""

    @staticmethod
    def operation(list_):
        print(f"The max is {np.max(list_)}")


class Main:
    """Main"""

    @staticmethod
    def get_operations(list_):
        # __subclasses__ will found all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(list_)


if __name__ == "__main__":
    Main.get_operations([1, 2, 3, 4, 5])
