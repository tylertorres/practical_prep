class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = build_magazine_map(magazine)
        for char in ransomNote:
            if char not in magazine_map or magazine_map[char] <= 0:
                return False
            magazine_map[char] -= 1
        return True

def build_magazine_map(mag):
    counter_map = {}
    for char in mag:
        if char not in counter_map:
            counter_map[char] = 0
        counter_map[char] += 1
    return counter_map


"""
- check if all letters in ransom note are in magazine
- hold state to make sure all letters in ransomNote are accounted for
- counter of magainze
- iterate through ransom note and any time you cant form that letter with 
the current map, return false
- return true at the end ; all processing done correctly
"""
