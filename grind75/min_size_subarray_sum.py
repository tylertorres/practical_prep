class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_length = float("inf")
        subarray_sum = left = 0
    
        for right, value in enumerate(nums):
            subarray_sum += value

            while left <= right and subarray_sum >= target:
                window_length = min(window_length, right - left + 1)
                subarray_sum -= nums[left]
                left += 1
        
        return window_length if window_length != float("inf") else 0




"""
Algo
- iterate over the nums
- have a pointer left, and right to open and close a potential subarray sum
- calculate the current subarray sum
- if subarray sum >= target : shrink until window_sum < target and eval the min(window_sum_length, min_window_length)
- return min window_sum_length

- 
- return min_length of subarray whose sum >= target else 0
- left < right
- 



2 3 1 2 4 3 | t = 7
          l
          r


Pattern
- Sliding Window
"""
