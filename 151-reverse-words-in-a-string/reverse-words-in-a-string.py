class Solution:
    def reverseWords(self, s: str) -> str:
        result = []

        for i in reversed(s.split()):
            result.append(i)

        return " ".join(result)