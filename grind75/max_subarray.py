import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -math.inf

        for number in nums:
            current_sum += number
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0
        
        return max_sum


