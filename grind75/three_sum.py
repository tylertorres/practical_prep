class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for first_index in range(len(nums) - 2):
            if first_index > 0 and nums[first_index] == nums[first_index - 
1]:
                continue
            
            left, right = first_index + 1, len(nums) - 1
            while left < right:
                current_sum = nums[first_index] + nums[left] + nums[right]
                if current_sum == 0:
                    # found a valid triplet ; process appropriately
                    triplets.append([nums[first_index], nums[left], 
nums[right]] )
                    # move forward left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # move forward right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

"""
- main loop that holds 1st value of triplet
- What happens when a value is found?
    - move until ptrs cross
    - move forward ptrs 
        - while left[i] == left[i + 1] : i++
        - while rightt[i] == right[i - 1]: i--
        - left += 1
        - right -= 1
"""
        
