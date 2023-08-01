class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        distance = lambda x, y: abs(x - y)
        closest_sum = min_distance = float('inf')
        size = len(nums)

        nums.sort()

        for index in range(size - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            left, right = index + 1, size - 1
            while left < right:
                current_sum = nums[index] + nums[left] + nums[right]
                if current_sum == target:
                    return target
                
                current_distance = distance(target, current_sum)
                if current_distance < min_distance:
                    min_distance = current_distance
                    closest_sum = current_sum

                if current_sum > target:
                    right -= 1
                else:
                    left += 1

            
        return closest_sum


