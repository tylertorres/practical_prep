class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_stair(0, n)

    def climb_stair(self, current_stair: int, end_stair: int):
        stairs_count = [0 for _ in range(end_stair + 1)]
        stairs_count[-1] = 1 # base case
        
        for i in range(end_stair - 1, -1, -1):
            ways_jumping_two = stairs_count[i + 2] if i + 2 <= end_stair 
else 0
            ways_jumping_one = stairs_count[i + 1]

            stairs_count[i] = ways_jumping_one + ways_jumping_two

        return stairs_count[0]

    
    # Correct but TLE
    def climb_stair_bf(self, current_stair: int, end_stair: int):
        if current_stair == end_stair:
            return 1
        
        distinct_ways = 0
        for hop_increment in range(2, 0, -1):
            if current_stair + hop_increment <= end_stair:
                distinct_ways += self.climb_stair(current_stair + 
hop_increment, end_stair)
        
        return distinct_ways





"""
- [ 0 0 0 0 0 ]
- options : jump 1, jump 2
- Availability = current + jump < n
- if available: take that option
    - start by being greedy
- have to exhuast all options ; so both j1 and j2
"""
