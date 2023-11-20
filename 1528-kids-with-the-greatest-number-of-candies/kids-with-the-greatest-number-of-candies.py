class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolList = []
        for i in candies:
            if (i + extraCandies) >= max(candies):
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList
        