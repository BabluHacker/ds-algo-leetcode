class Solution:
    def trap(self, height: List[int]) -> int:
        # for every h[i] trapped water is min(max_left_h, max_right_h) - h[i]
        
        n = len(height)
        left, right = 0, n-1
        
        max_left, max_right = height[0], height[n-1]
        
        ans = 0
        
        while (left < right):
            if max_left > max_right: # move right pointer 
                right -= 1
                trapped = (max_right - height[right])
                ans += trapped if trapped > 0 else 0
                max_right = max(max_right, height[right])
            else:
                left += 1
                trapped = (max_left - height[left])
                ans += trapped if trapped > 0 else 0
                max_left = max(max_left, height[left])
            # print(left, right, trapped)
        return ans
            
                
            