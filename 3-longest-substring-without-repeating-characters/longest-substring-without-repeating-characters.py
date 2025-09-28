class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()
        n = len(s)

        # O(n)
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            seen.add(s[r])

        return longest
