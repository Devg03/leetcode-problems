class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"}":"{", ")": "(", "]":"["}

        for char in s:
            if char in mappings:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'

                if mappings[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack