from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter_map = Counter(s)
        evens = odds = 0

        for value in counter_map.values():
            if value % 2 == 0:
                evens += value
            
            if value % 2 == 1:
                odds += 1
            
        return len(s) - odds + 1 if odds != 0 else len(s)
