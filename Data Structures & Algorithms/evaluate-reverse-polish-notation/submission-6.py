class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        for token in tokens[1:]:
            if token == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        return int(stack[-1])
        


        