class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultSet = defaultdict(list)
        for word in strs:
            # sorted() returns a list of chars which is why you need to join them to get the string
            key = "".join(sorted(word))
            resultSet[key].append(word)

        return list(resultSet.values())
        