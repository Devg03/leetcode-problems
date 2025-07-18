class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in range(len(s)):
            if s[i].isalnum():
                res += (s[i].lower())

        return "".join(res) == "".join(reversed(res))