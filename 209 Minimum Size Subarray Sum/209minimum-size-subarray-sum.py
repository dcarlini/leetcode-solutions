import math
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window_start = 0
        window_sum = 0
        current_size = 0
        min_length = math.inf
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            while window_sum >= target:
                # print("start", window_start, "end", window_end, "sum", window_sum, "minl", min_length)
                min_length = min(min_length, window_end - window_start + 1)  # Update the minimum length
                window_sum -= nums[window_start]  # Remove the element going out of the window
                window_start += 1  # Slide the window ahead
    
                
        if min_length == math.inf:
            min_length = 0

        
        return min_length


        