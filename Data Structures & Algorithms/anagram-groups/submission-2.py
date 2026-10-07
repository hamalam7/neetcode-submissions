class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a char freq map on each word and then convert the freq map to a tuple which acts as the key.
        resultSet = defaultdict(list)
        for word in strs:
            charFreqMap = [0] * 26
            for c in word:
                #compute its ordinal position and increase it
                charFreqMap[ord(c) - ord("a")] += 1
            
            resultSet[tuple(charFreqMap)].append(word)

        return list(resultSet.values())
        