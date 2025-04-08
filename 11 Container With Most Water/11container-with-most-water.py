import math
class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        p1 = 0
        p2 = len(height) - 1

        maxArea = -math.inf

        while p1 < p2:

            area = min(height[p1] , height[p2]) * (p2 - p1)
            if area > maxArea:
                maxArea = area
            
            if height[p1] > height[p2]:
                p2 -= 1
            else: # height[p1] < height[p2]:
                p1 += 1
            
            
        return maxArea
            


        