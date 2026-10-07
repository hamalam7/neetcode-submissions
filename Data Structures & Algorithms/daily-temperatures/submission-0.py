class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        #add pair to stack so you know which day it occured
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                # NOTE: i > j Always 
                j, t = stack.pop()
                res[j] = i - j

            stack.append((i, temp))

        return res
