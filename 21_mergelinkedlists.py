#You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. 
#The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

def merge_two_lists(list1: ListNode, list2: ListNode):
    dummy = ListNode()
    current = dummy

    p1, p2 = list1, list2

    while p1 and p2:
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next    
        else:
            current.next = p2
            p2 = p2.next
        current = current.next

    if p1:
        current.next = p1
    
    if p2:
        current.next = p2

    return dummy.next