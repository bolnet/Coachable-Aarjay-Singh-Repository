# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
          A->a1->a2->c1->c2->c3->b1->b2->b3-c1
          B->b1->b2->b3->c1->c2->c3->a1->a2-c2

          PLAN
          initialize pointer p and q for first and second list
          iterate both the list using p and q pointer until we find intersection
          in each iteration p pointer to next pointer until it reaches to the end of list
            if it reached to the end
            assign q pointer's initial position
          -in each iteration q pointer to next pointer until it reached to the end of the list
            -if it reached to the end
            -assing q pointer to the initial position of p
         return 0 if no intersection found


        '''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_pointer = headA
        q_pointer = headB
        while p_pointer != q_pointer:
            p_pointer = p_pointer.next if p_pointer is not None else headB
            q_pointer = q_pointer.next if q_pointer is not None else headA

        return p_pointer


