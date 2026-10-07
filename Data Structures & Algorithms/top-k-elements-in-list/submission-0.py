class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countSet = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countSet[n] = countSet.get(n, 0) + 1
        for n, c in countSet.items():
            frequency[c].append(n)

        result = []
        #dont care about freq[0] as nothing will ever be in there so you can stop at 0
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
        