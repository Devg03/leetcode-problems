from functools import reduce

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return reduce(max, [s.count(" ") + 1 for s in sentences])