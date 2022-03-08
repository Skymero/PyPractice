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

# Expected Output 
##  [1,1,2,3,4,4]

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



list1 = [2,4,1]
list2 = [1,3,4]

merged_list(list1, list2)