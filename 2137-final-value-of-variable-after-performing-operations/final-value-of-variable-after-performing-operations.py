class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in operations:
            lowI = i.lower()
            if lowI == "++x" or lowI == "x++":
                value += 1
            else:
                value -= 1
        return value