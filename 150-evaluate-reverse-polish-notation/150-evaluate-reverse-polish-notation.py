class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                ans = stack.pop()
                if token == '+':
                    ans = (stack.pop()) + ans
                elif token == '-':
                    ans = (stack.pop()) - ans
                elif token == '*':
                    ans = (stack.pop()) * ans
                elif token == '/':
                    ## this one is tricky 6//-132 = -1 but should be 0 so ,, we divide then typecast to int.
                    ans = int((stack.pop()) / ans)
                stack.append(int(ans))
            # print(stack)
        return stack.pop()