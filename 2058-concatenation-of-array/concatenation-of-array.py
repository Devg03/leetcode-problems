class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, 2):
            for j in nums:
                result.append(j)

        return result
