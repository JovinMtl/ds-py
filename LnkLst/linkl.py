
class Node:
    """This class represents the node of the LinkedList"""
    def __init__(self, data) -> None:
        self.data = data  #anything
        self.next = None # will hold that next object(node)
    
    def __str__(self) -> str:
        return self.data

class LinkedList:
    """This class is for linkedList."""
    def __init__(self) -> None:
        self.first = None  # will hold first object
        self.last = None
        self.size = 0
    
    def _addEl(self, element:Node)->int:
        """This method adds the element at the last index."""
        newEL = Node(element)
        if not self.first:
            self.first = newEL
        self.last = newEL
        self.size += 1

        return 0 # went well
    
    def print(self)->str:
        """THis will print the content"""
        return "Hello world"
    
    def __str__(self) -> str:
        """This method will print the content of the LinkedList."""
        content = []
        current = self.first
        while current:
            content.append(current.data)
            print(f"I can see something like {current.data}")
            current = current.next

        if len(content):
            return str(content)
        else:
            return "Empty"


# initializing the LinkedList
lklst = LinkedList()
lklst._addEl(4) #adding the element
lklst._addEl(7)
print(f"Now we want to print the content: {lklst}")