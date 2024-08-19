class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(reversed(str(x))) == list(str(x))