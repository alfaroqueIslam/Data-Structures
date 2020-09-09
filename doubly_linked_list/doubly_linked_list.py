"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
            print("node inserted")
            return
        new_node = ListNode(value)
        new_node.next = self.head
        new_node.prev = new_node
        self.head = new_node
        self.length = self.length + 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head.next is None:
            n = self.head.value
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return n
        n = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.length = self.length - 1
        return n
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
            print("node inserted")
            return
        n = self.tail
        while n.next is not None:
            n = n.next
        new_node = ListNode(value)
        n.next = new_node
        new_node.prev = n
        self.tail = new_node
        self.length = self.length + 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            print("The list has no element to delete")
            return 
        if self.head.next is None:
            n = self.tail.value
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return n
        n = self.tail.value
        n1 = self.tail
        while n1.next is not None:
            n1 = n1.next
        n.prev.next = None
        self.tail = n1.prev
        self.length = self.length - 1
        return n
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head.next is None:
            if self.head.value == node.value:
                self.head = None
                self.tail = None
                self.length = self.length - 1
            else:
                print("Item not found")
            return 

        if self.head.value == node.value:
            self.head = self.head.next
            self.head.prev = None
            self.length = self.length - 1
            return

        if self.head.next.value == node.value:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head.next
            self.length = self.length - 1


        n = self.tail
        while n.next is not None:
            if n.value == node.value:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.value == node.value:
                n.prev.next = None
                self.length = self.length - 1
            else:
                print("Element not found")

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass