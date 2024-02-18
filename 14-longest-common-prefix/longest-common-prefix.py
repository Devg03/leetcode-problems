class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        result = ""

        for j in range(0, len(smallest)):
            if smallest[j] == max(strs)[j]:
                result += smallest[j]
            else:
                break

        return result
        