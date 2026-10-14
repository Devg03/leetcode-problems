class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramDict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1

            anagramDict[tuple(count)].append(word)

        return list(anagramDict.values())