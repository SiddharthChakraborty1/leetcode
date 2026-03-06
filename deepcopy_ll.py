"""Copy Linked List with Random Pointer"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_new_mapper = {}
        current = head
        while current:
            new_node = Node(current.val, current.next, current.random)
            old_new_mapper[current] = new_node
            current = current.next
        
        for node in old_new_mapper:
            old_new_mapper[node].next = old_new_mapper[node.next] if node.next else None
            old_new_mapper[node].random = old_new_mapper[node.random] if node.random else None
        
        return old_new_mapper[head]

        
        
