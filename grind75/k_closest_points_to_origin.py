import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        euclidean_distance = lambda x, y : math.sqrt((x**2 + y**2))

        for x, y in points:
            current_distance = euclidean_distance(x, y)
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (-current_distance, [x, y]))
            else:
                heapq.heappush(min_heap, (-current_distance, [x, y]))
            
        return [xy for dist, xy in min_heap]

"""
- Only pushing when min_heap < k or min_heap > k and dist < top of heap
- Only pop when min_heap > k and dist < top of heap
"""

