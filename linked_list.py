""" Implementing Linked lists

# https://towardsdatascience.com/python-linked-lists-c3622205da81

##   They are typically preferred over standard arrays when:
###     you need a constant time when adding or removing elements from the sequence
###     manage memory more efficiently, especially when the number of elements is unknown
###     you want to insert items in the middlw point more efficiently
##  Python DOES NOT have a built-in implementation of linked lists

# FIRST: CREATE A USER-DEFINED CLASS FOR INDIVIDUAL NODES IN A LINKED LIST
#   Useful for both single or double linked lists

"""

# USER DEFINED NODE

class Node:
    # when an instance of a Node has next set to None then it means
    #   that it is essentially the tail of the Linked List
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return '->'.join([str(node) for node in self])
# Linked List Class

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    #  iterates over every node of the sequence until we reach the tail of the Linked List.
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    # this method ensures that LinkedList class is iterable
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    # create a property called values so we can access the values of all nodes included in the sequence
    @property
    def values(self):
        return [node.value for node in self]


    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    # adding this method to add a single node to the linked list
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

# Doubly linked lists inherits from LinkedList class and overrides the add_node and add_node_as_head methods
class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head


def merged_list(lista, listb):
    listc = []
    if len(lista) > len(listb):
        num = int(len(lista))
    else: num = int(len(listb))
    print(num)

    for i in range(num):
        listc.append(lista[i])
        listc.append(listb[i])
    
    print(listc)
    listc.sort()
    print(listc)
    return listc

def head_of_link(lista):
    num = int(len(lista))
    linList = LinkedList()

    for i in range(num):
        val = lista[i]
        linList.head.next = Node(val)
    
    return linList.head



list1 = [2,4,1]
list2 = [1,3,4]
list3 = merged_list(list1, list2)
print(list3)
list_head = head_of_link(list3)
print(list_head)
