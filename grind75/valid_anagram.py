class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        character_map = buildMap(s)
        for char in t:
            if char in character_map:
                character_map[char] -= 1
        return all(value == 0 for value in character_map.values())


def buildMap(s: str):
    character_map = {}
    for char in s:
        if char not in character_map:
            character_map[char] = 0
        character_map[char] += 1
    return character_map
            
