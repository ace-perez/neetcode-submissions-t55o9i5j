class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_max = 0
        left, right = 0, len(heights) - 1

        while left < right:
            total_vol = min(heights[left],heights[right]) * (right - left)
            water_max = max(water_max, total_vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        
        return water_max
        