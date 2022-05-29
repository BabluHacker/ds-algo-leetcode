class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_water = 0
        while start < end:
            curr_water = (end - start) * min(height[start], height[end])
            max_water = max(max_water, curr_water)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_water