from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        encoding_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            encoding_map[sorted_s].append(s)
        
        return encoding_map.values()
