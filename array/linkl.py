
class Node:
    """This class represents the node of the LinkedList"""
    def __init__(self, data) -> None:
        data = data  #anything
        next = None # will hold that next object(node)

class LinkedList:
    """This class is for linkedList."""
    def __init__(self) -> None:
        first = None  # will hold first object
        last = None
        size = 0
    
    def _addEl(self, element:Node)->int:
        """This method adds the element at the last index."""
        newEL = Node(1)
        if not self.first:
            self.first = newEL
            self.last = newEL
            size += 1
        else:
            self.last =newEL

        return 0 # went well
    


# initializing the LinkedList
lklst = LinkedList()