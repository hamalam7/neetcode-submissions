class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)
		res = max(piles)
		while l <= r:
			#try new mid value see if it works on each pile and is less than "h"
			mid = (l + r) // 2
			totalHours = 0
			for p in piles:
				#must spend 1 full hour, even if 1 extra banana (round up)
				totalHours += math.ceil(p/mid)
			#update res and pointers, found a valid answer keep searching
			if totalHours <= h:
				res = min(res, mid)
				r = mid - 1
			else:
				l = mid + 1
		return res
			