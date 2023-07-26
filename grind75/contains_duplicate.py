from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for num in nums:
            if num in seen and seen[num] > 0:
                return True
            seen[num] += 1
        
        return False
