class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            k = left + (right - left)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours > h:
                # Too slow — must speed up -- too much time to eat increase eating capacity per hr
                left = k + 1
            else:
                # Possible to go slower
                right = k
        # left == right
        return left