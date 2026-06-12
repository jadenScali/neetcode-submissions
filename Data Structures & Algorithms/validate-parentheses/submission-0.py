class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = { '[' : ']', '(' : ')', '{' : '}' }

        for l in s:
            if l in matching_bracket:
                stack.append(l)
            elif not stack or matching_bracket[stack.pop()] != l:
                return False
        
        return True

        