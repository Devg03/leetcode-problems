class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = left = 0
        chars = {}

        for right, c in enumerate(s):
            chars[c] = 1 + chars.get(c, 0)
            while chars[c] > 1:
                chars[s[left]] -= 1
                left += 1
        
            maxLength = max(maxLength, right - left + 1)

        return maxLength