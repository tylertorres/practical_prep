class Solution:
    def longestPalindrome(self, s: str) -> str:
        indices = [0, 0]
        length = len(s)

        for index in range(length):
            left, right = self.expand_palindrome(s, index)
            indices = indices if indices[1] - indices[0] + 1 > right - left + 1 else [left, right]

        left, right = indices
        return s[left: right + 1]
    
    def expand_palindrome(self, s, index):
        max_right = max_left = 0

        for i in range(2):
            left, right = index - i, index

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            if right - left + 1 > max_right - max_left + 1:
                max_left = left
                max_right = right
        
        return max_left, max_right

"""
s = babad
Topic or Pattern
- String
- Palindrome
- Two Pointers
- What is the trick or vital piece of info?
    - Expand around the middle!!
    - Be careful about OOB 
"""
