class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # look for the temp in stack < temp[i]
            while stack:
                top = stack[-1]
                if top[0] < temperatures[i]:
                    ans[top[1]] = i - top[1]
                    stack.pop()
                    
                else:
                    break
            stack.append((temperatures[i], i))
        return ans