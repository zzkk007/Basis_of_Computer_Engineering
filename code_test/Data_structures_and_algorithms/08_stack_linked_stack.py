"""
    Stack based upon linked list

"""

from typing import Optional

class Node(object):
    def __init__(self, data:int, next = None):
        self._data = data
        self._next = next

class LinkedStack(object):
    def __init__(self):
        self._top = None

    def push(self, value:int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self):
        if self._top:
            value = self._top._data
            self._top =self._top._next
            return value

    def Stackprint(self):
        current = self._top
        while current:
            print(current._data)
            current = current._next



if __name__ == "__main__":

    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    stack.Stackprint()
    for _ in range(3):
        stack.pop()

    stack.Stackprint()

