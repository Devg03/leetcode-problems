class Solution:
    def reverseString(self, s: List[str]) -> None:
        count = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[count] = s[count], s[i]
            count -= 1
            