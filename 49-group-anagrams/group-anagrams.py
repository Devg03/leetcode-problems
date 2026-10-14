class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramDict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagramDict[sorted_word].append(word)

        return list(anagramDict.values())