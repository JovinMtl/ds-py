
class Node:
    """This class represents the node of the LinkedList"""
    def __init__(self, data) -> None:
        self.data = data  #anything
        self.next = None # will hold that next object(node)
        self.previous = None
    
    def __str__(self) -> str:
        return f"{self.data}"

class LinkedList:
    """This class is for linkedList."""
    def __init__(self) -> None:
        self.first = None  # will hold first object
        self.last = None
        self.size = 0
    
    def addelements(self, *elements:Node)->int:
        """This method adds the element(s) at the last index."""
        for element in elements:
            newEL = Node(element)
            if not self.first:
                self.first = newEL
            else:
                newEL.previous = self.last
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
        """THis method will delete all occurence of one element 
        in the linkedList."""
        if self.first and self.first.data == element and \
            self.first.next:
            self.first = self.first.next
            self.size -= 1
        current = self.first
        previous = current
        while current:
            if current.data == element and current.next:
                previous.next = current.next
                self.size -= 1
            elif current.data == element:
                # print("It is the last")
                self.last = previous
                previous.next = None
                self.size -= 1
            else:
                previous = current
            current = current.next
        
    def delOneEl(self, *elements:Node)->int:
        """THis method will delete one occurence of the element 
        in the linkedList."""

        for element in elements:
            if self.first and self.first.data == element and \
                self.first.next:
                self.first = self.first.next
                self.size -= 1
                return 0
            current = self.first
            previous = current
            while current:
                if current.data == element and current.next:
                    previous.next = current.next
                    self.size -= 1
                    return 0
                elif current.data == element:
                    # print("It is the last")
                    self.last = previous
                    previous.next = None
                    self.size -= 1
                    return 0
                else:
                    previous = current
                current = current.next
        
    def delements(self, *elements:Node)->int:
        """THis method will delete all occurence of the elements 
        in the linkedList."""

        for element in elements:
            if self.first and self.first.data == element and \
                self.first.next:
                self.first = self.first.next
                self.size -= 1
            current = self.first
            previous = current
            while current:
                if current.data == element and current.next:
                    previous.next = current.next
                    self.size -= 1
                elif current.data == element:
                    # print("It is the last")
                    self.last = previous
                    previous.next = None
                    self.size -= 1
                else:
                    previous = current
                current = current.next
    
    def reverse(self)->int:
        """This method will reverse the linkedList"""
        if self.size < 2:
            return -1
        tempOne = None
        tempEnd = self.first
        current = self.last
        i = 0
        worthy = True
        while worthy:
            if not current.previous:
                worthy = False
                self.last = current
                current.next = None
                continue
            tempOne = current.next
            current.next = current.previous
            if not i :
                self.first = current
                current.previous = None
                i += 1
            else:
                current.previous = tempOne
                i += 1
            current = current.next

        return 0
    
    def getKthfromEnd(self, k:int)->Node:
        """This method will return the Node from the last n index."""
        pOne = self.last
        pTwo = None
        current = pOne
        i = 1
        worth = True
        while worth:
            if i == k:
                worth = False
                pTwo = current
                continue
            current = current.previous
            i += 1
        
        return pTwo


    def __len__(self)->int:
        """This method returns the size of the LinkedList."""
        return self.size


# initializing the LinkedList
lklst = LinkedList()
lklst.addelements(4) #adding the element
lklst.addelements(7, 10)
lklst.addelements(3, 'jove')
lklst.addelements(0, 3, 8)
print(f"Now we want to print the content: {lklst} \
       and its size is {len(lklst)}")

# Now to delete one element
# lklst.delEl(0)
# lklst.delEl(4)
# lklst.delOneEl(8, 0)
# lklst.delements(3, 0, 7, 10)
lklst.reverse()
print(f"The rest is { lklst} and size of {len(lklst)}")
lklst.delements(8, 0)
print(f"The rest is { lklst} and size of {len(lklst)}")