

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
    
    def push(self, element)->int:
        node = State(element)
        if self.latest:
            node.previous = self.latest
        self.latest = node
        return 0
    
    def pop(self)->int:
        """This method remove the item on the top of the stack."""
        if self.latest:
            self.latest = self.latest.previous
        return 0
    
    def peek(self):
        """This method returns the top item of the stack without 
        removing it."""
        if self.latest:
            return self.latest.data
        return 0
    
    def isEmpty(self)->bool:
        """This method tells whether the stack is empty or not."""
        if not self.latest:
            return True
        else:
            return False
    
    def getBack(self):
        self.latest = self.previous
        self.previous = self.previous.previous
    
    def __str__(self) -> str:
        content = []
        current = self.latest
        while current:
            content.append(current.data)
            current = current.previous
        
        return f"{content}"
    

# Now consumming the objects
stack_instance = Stack()
stack_instance.push(2)
stack_instance.push(5)
stack_instance.push(3)
print(f"we have : {stack_instance}")

stack_instance.pop()
print(f"The rest is : {stack_instance}")
print(f"We peek the last element: {stack_instance.peek()}")
print(f"Does the stack empty? {stack_instance.isEmpty()}")

