class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = pointer = 0
        end = 1
        merged = []

        # if newInterval should be first element
        if not intervals or newInterval[end] < intervals[pointer][start]:
            return [newInterval] + intervals
        
        while pointer < len(intervals) and intervals[pointer][end] < newInterval[start]:
            merged.append(intervals[pointer])
            pointer += 1

        merged.append(newInterval)
        for index in range(pointer, len(intervals)):
            current_interval = intervals[index]
            previous_interval = merged[-1]

            if previous_interval[end] >= current_interval[start]:
                overlapped_interval = [min(previous_interval[start], current_interval[start]), max(previous_interval[end], current_interval[end])]
                merged[-1] = overlapped_interval
            else:
                merged.append(current_interval)

        return merged
