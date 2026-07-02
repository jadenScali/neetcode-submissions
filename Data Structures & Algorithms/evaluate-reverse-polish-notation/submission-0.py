class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            token = tokens[i]

            first, secomd = None, None
            if token in "+-*/":
                second = stack.pop()
                first = stack.pop()

            match token:
                case "+":
                    stack.append(first + second)
                case "-":
                    stack.append(first - second)
                case "*":
                    stack.append(first * second)
                case "/":
                    stack.append(first // second)
                case _:
                    stack.append(int(token))
            
        return stack.pop()

            