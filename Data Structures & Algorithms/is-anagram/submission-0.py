class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1

        for char in t:
            charMap[char] = charMap.get(char, 0) - 1
        
        return all(v == 0 for v in charMap.values())
        