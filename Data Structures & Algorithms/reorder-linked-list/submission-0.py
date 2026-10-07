# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reorderList(self, head: ListNode) -> None:
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		#reverse 2nd half which starts at slow.next
		#also need to set its next to None because it will now be the last node
		secondHalf = slow.next
		slow.next = None
		prev = None
		while secondHalf:
			tmp = secondHalf.next
			secondHalf.next = prev
			prev = secondHalf
			secondHalf = tmp

		#set up your pointers for merging
		#need to use tmp to store next node since you breaking links
		first, second = head, prev
		while second:
			tmp1, tmp2 = first.next, second.next
			first.next = second
			second.next = tmp1
			first = tmp1
			second = tmp2