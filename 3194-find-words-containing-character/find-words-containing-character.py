class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []

        for i in range(0, len(words)):
            if x in words[i]:
                out.append(i)

        return out