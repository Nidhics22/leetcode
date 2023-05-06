from _ast import List


def generateParenthesis(n: int):
    stack = []
    result = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            result.append("".join(stack))
            print("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    print(result)

class test2(object):
    generateParenthesis(3)



