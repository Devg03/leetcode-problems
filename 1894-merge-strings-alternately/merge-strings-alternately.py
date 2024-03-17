class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        minSize = min(len(word1), len(word2))

        counter = 0
        while (counter < minSize):
            result += word1[counter]
            result += word2[counter]
            counter += 1
        if (len(word1) > len(word2)):
            for i in range(minSize, len(word1)):
                result += word1[i]
        if (len(word2) > len(word1)):
            for i in range(minSize, len(word2)):
                result += word2[i]

        return result 