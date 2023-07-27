class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = left = 0
        seen = set()

        for right in range(len(s)):
            if s[right] in seen:
                left = self.move_left_until_valid(s, left, s[right], seen)
            
            longest = max(longest, right - left + 1)
            seen.add(s[right])

        return longest
    
    def move_left_until_valid(self, s, left, repeated_value, seen):
        while s[left] != repeated_value:
            seen.remove(s[left])
            left += 1
        
        return left + 1
