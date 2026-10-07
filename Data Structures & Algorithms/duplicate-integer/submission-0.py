import collections 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        hashSet = collections.defaultdict()
        for x in nums:
            if x not in hashSet:
                hashSet[x] = 1
            else:
                return True
        
        return False

        