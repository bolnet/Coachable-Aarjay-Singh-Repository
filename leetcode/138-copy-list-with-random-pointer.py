"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

PLAN:
    This problem can be to reduce to link list traversal if we have way to handle random ref
        - random ref is also a node ref.
        - if we store ref for all the nodes than we can simply build the linkedlis
    First pass
        iterate list and build map of new node ref for old old
    second pass:
        iterate old list use it's node value map to rebuild new list
    return list


"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        old_list_to_new_node = {}
        while curr:
            old_list_to_new_node[curr] = Node(-1)
            curr = curr.next

        curr = head
        while curr:
            new_node = old_list_to_new_node[curr]
            if curr.next:
                new_node.next = old_list_to_new_node[curr.next]
            if curr.random:
                new_node.random = old_list_to_new_node[curr.random]
            new_node.val = curr.val
            curr = curr.next

        return old_list_to_new_node[head]
