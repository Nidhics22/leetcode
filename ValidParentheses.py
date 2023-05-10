class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in s_dict:
                if stack and stack[-1] == s_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0