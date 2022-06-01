class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        max_area = 0
        for i in range(len(heights)):
            new_ind = i
            while stack:
                top = stack[-1]
                if top[0] > heights[i]: # pop top and update index of curr height
                    curr_area = top[0] * (i-top[1])
                    max_area = max(max_area, curr_area)
                    new_ind = top[1]
                    stack.pop()
                else:
                    break
            stack.append([heights[i], new_ind])
        i = len(heights) 
        while stack:
            top = stack[-1]
            curr_area = top[0] * (i-top[1])
            max_area = max(max_area, curr_area)
            stack.pop()
            
        return max_area
                
                    
                