

from ..LnkLst import Node

class Stack:
    """This class is for implementing the stack behaviour."""
    def __init__(self) -> None:
        self.latest = None // the latest state of the Stack
        self.previous = None // the previous Node of the stack.

        return None
    
    def addState(self, node:Node)->int:
        self.previous = self.latest
        self.latest = node
        return 0
    
    