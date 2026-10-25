class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        """ Stack follows LIFO. In other words, if we ever were to encounter a
        valid expression, we would run into a closing parantheses first. """

        mappings = {")": "(", "}": "{", "]": "["}
        # All of the potential matchings

        for i in s:
            if i in mappings:
                # We check for closing parantheses
                if stack:  # If stack is not empty
                    top_element = (
                        stack.pop()
                    )  # Check the top element of the stack as it must be the closing parantheses
                else:
                    top_element = "#"

                """ If the top element is not in mappings[i], then we can say its 
                invalid as the top element must be a closing parantheses"""
                if top_element != mappings[i]:
                    return False
            else:  # If its not a closing parantheses then we add it to the stack
                stack.append(i)

        return (
            not stack
        )  # Returns whether stack is empty or not. if the expression is valid, then the stack would be empty.
