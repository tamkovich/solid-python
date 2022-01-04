"""The Liskov substitution principle (LSP)

Functions that use pointers or references to base classes must be able
to use objects of derived classes without knowing it
"""
from typing import List


class SortedStrategy:
    def do_algorithm(self, data: List) -> List:
        """This method sorts items in the data sequence with an alphabetical order"""
        return sorted(data)


class ReversedSortedStrategy(SortedStrategy):
    def do_algorithm(self, data: List) -> List:
        """This method sorts items in the data sequence with an reversed-alphabetical order

        Note:
            - this method still has the List as an input and returns List as an output
            - the idea wasn't changed, only solution
            - DON'T .pop values here because this method was created only to sort sequence w/o any side effect
        """
        return sorted(data)[::-1]
