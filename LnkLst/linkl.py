
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
    
    def addEl(self, *elements:Node)->int:
        """This method adds the element at the last index."""
        for element in elements:
            newEL = Node(element)
            if not self.first:
                self.first = newEL
            else:
                self.last.next = newEL
            self.last = newEL
            self.size += 1

        return 0 # went well
    
    def __str__(self) -> str:
        """This method will print the content of the LinkedList."""
        content = []
        current = self.first
        while current:
            content.append(current.data)
            current = current.next

        if len(content):
            return str(content)
        else:
            return "Empty"
    
    def delEl(self, element:Node)->int:
        """THis method will delete the element from the first 
        occurence."""
        if self.first and self.first.data == element and \
            self.first.next:
            self.first = self.first.next
        current = self.first
        previous = current
        while current:
            if current.data == element and current.next:
                previous.next = current.next
                self.size -= 1
            elif current.data == element:
                print("It is the last")
                self.last = previous
                self.size -= 1
            else:
                previous = current
            current = current.next

    def __len__(self)->int:
        """This method returns the size of the LinkedList."""
        return self.size


# initializing the LinkedList
lklst = LinkedList()
lklst.addEl(4) #adding the element
lklst.addEl(7, 10)
lklst.addEl(3, 'jove')
lklst.addEl(0, 3, 8)
print(f"Now we want to print the content: {lklst} \
       and its size is {len(lklst)}")

# Now to delete one element
lklst.delEl(3)
lklst.delEl(8)
print(f"The rest is { lklst} and size of {len(lklst)}")