"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    PLAN 1;
    Single pass
        traverse the circular linked list to find the correct positon of the node
        insert the node to the correct position

"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break
            elif curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                break
            curr = curr.next
            if curr == head:
                break
        new_node = Node(insertVal)
        new_node.next = curr.next
        curr.next = new_node
        return head
