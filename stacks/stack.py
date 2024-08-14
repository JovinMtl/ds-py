

# import sys

# sys.path.append('../LnkLst')

# from doublelinkl import Node
# # from ..LnkLst.doublelinkl import Node

class State:
    """This will represent any state in the stack."""
    def __init__(self, data) -> None:
        self.data = data
        self.previous = None

class Stack:
    """This class is for implementing the stack behaviour."""
    def __init__(self) -> None:
        self.latest = None # the latest state of the Stack
        self.previous = None # the previous Node of the stack.

        return None
    
    def addState(self, element)->int:
        node = State(element)
        self.previous = self.latest
        self.latest = node
        return 0
    
    def getBack(self):
        self.latest = self.previous
        self.previous = self.previous.previous
    
    def __str__(self) -> str:
        content = []
        current = self.latest
        while current:
            print(f"we can see : {current.data}")
            content.append(current.data)
            current = current.previous
        
        return f"{content}"
    

# Now consumming the objects
stack_instance = Stack()
stack_instance.addState(2)
print(f"we have : {stack_instance}")