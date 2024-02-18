class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        largest = max(strs)
        result = ""

        for j in range(0, len(smallest)):
            if smallest[j] == largest[j]:
                result += smallest[j]
            else:
                break

        return result
        