"""The Single-Responsibility Principle (SRP)

A class should have one, and only one, reason to change
"""

import numpy as np


def math_operations(list_):
    """BAD version"""
    # Compute Average
    print(f"the mean is {np.mean(list_)}")
    # Compute Max
    print(f"the max is {np.max(list_)}")


math_operations(list_=[1, 2, 3, 4, 5])
