#Given the head of a singly linked list, reverse the list, and return the reversed list.

head = [1,2,3,4,5]
reversed_head = []

for i in range(len(head)-1, -1, -1):
    reversed_head.append(head[i])
print(reversed_head)

#^this returns an error for some reason. alternative solution:
prev_node = None
current_node = head

while current_node is not None:
    next_node = current_node.next
    current_node.next = prev_node
    prev_node = current_node
    current_node = next_node

print(prev_node)