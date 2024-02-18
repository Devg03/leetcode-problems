class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for j in range(0, len(min(strs))):
            if min(strs)[j] == max(strs)[j]:
                result += min(strs)[j]
            else:
                break

        return result
        