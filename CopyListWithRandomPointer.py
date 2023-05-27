"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        head_copy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            head_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = head_copy[curr]
            copy.next = head_copy[curr.next]
            copy.random = head_copy[curr.random]
            curr = curr.next
        return head_copy[head]
