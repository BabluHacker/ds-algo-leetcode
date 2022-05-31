class Solution:
    def isValid(self, s: str) -> bool:
        isValid = True
        stack = []
      
        for i in range(len(s)):
            
            if s[i] == ')':
                last = stack.pop() if stack  else '#'
                if last != '(':
                    isValid = False
                    break
            elif s[i] == '}':
                last = stack.pop() if stack  else '#'
                if last != '{':
                    isValid = False
                    break
            elif s[i] == ']':
                last = stack.pop() if stack  else '#'
                if last != '[':
                    isValid = False
                    break
            else:
                stack.append(s[i])
            # print(i, stack)
        
        return isValid if len(stack) == 0 else False