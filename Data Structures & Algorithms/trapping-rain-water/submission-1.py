class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        l,r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        trappedWater = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    trappedWater += maxLeft - height[l]
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    trappedWater += maxRight - height[r]
                r -= 1
        
        return trappedWater