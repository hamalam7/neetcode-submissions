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
		oldToCopy = {None:None}
		cur = head
		#each node maps to its copy
		while cur:
			copy = Node(cur.val)
			oldToCopy[cur] = copy
			cur = cur.next

		#reset for next loop, and set pointers for the copy
		#need to point to new node, not original, so use hashMap
		cur = head
		while cur:
			copy = oldToCopy[cur]
			copy.next = oldToCopy[cur.next]
			copy.random = oldToCopy[cur.random]
			cur = cur.next
		#need to return start of linked list which is at head but of ur copy
		return oldToCopy[head]
		