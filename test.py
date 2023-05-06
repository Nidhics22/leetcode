def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    token_set = {"+", "-", "/", "*"}
    for token in tokens:
        if token not in token_set:
            stack.append(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            val3 = 0
            if token == "+":
                val3 = val2 + val1
            elif token == "-":
                val3 = val2 - val1
            elif token == "/":
                val3 = val2 / val1
            else:
                val3 = val2 * val1
            stack.append(int(val3))
    return stack.pop()



class Solution(object):
    temp = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(temp)

