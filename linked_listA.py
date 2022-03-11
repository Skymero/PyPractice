""" Merge Two sorted lists 
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

    1. The number of nodes in both lists is in the range [0, 50].
    2. -100 <= Node.val <= 100
    3. Both list1 and list2 are sorted in non-decreasing order.

Solved here without returning the head of a linked list
"""

#Nodes are not built in to python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        #both of the same if nothing in the list
        
    def __repr__(self):
        node = self.head
        nodes = [] # where to add nodes to
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        nodes.append("None")
        return " -> ".join(nodes)
            
    def insert_begin(self,data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else: 
            new_node = Node(data, self.head)
            self.head = new_node
    
    def insert_end(self, data):

        if self.head is None:
            link.insert_begin(data)
        else:
            self.last_node.next_node= Node(data)
            self.last_node = self.last_node.next_node
    
    def return_head(self):
        if self.head is None:
            print("Linked list is empty")
        else: 
            current_node = self.head
            return current_node.data

def merged_list(lista, listb):
    listc = []
    if len(lista) > len(listb):
        num = int(len(lista))
    else: num = int(len(listb))
    print(num)

    for i in range(num):
        listc.append(lista[i])
        listc.append(listb[i])
    
    listc.sort()
    print(listc)
    return listc


list1 = [2,4,1]
list2 = [1,3,4]
        
data = merged_list(list1, list2)
num = len(data)

link = LinkedList()
for i in range(num):
    value = str(data[i])
    link.insert_end(value)
print(link)

head_data = link.return_head()
print(head_data)






