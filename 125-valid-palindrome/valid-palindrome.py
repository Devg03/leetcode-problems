class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())

        return "".join(res) == "".join(reversed(res))