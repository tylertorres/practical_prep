from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: 
int) -> List[List[int]]:
        origin_color = image[sr][sc]
        queue = deque([(sr, sc)])
        directions = [(1,0), (0,1),(-1, 0),(0, -1)]
        visited = set()

        while queue:
            row, column = queue.popleft()
            visited.add((row, column))
            image[row][column] = color

            for new_row, new_column in directions:
                current_row, current_column = new_row + row, new_column + 
column
                if not isOutOfBounds(image, current_row, current_column) 
and \
                        isOriginColor(origin_color, 
image[current_row][current_column]) and \
                        isNotVisited(visited, current_row, 
current_column):
                            queue.append((current_row, current_column))
        return image


def isOutOfBounds(image: List[List[int]], current_row: int, 
current_column: int):
    rows, columns = len(image), len(image[0])
    return current_row >= rows or current_row < 0 or current_column >= 
columns or current_column < 0

def isOriginColor(origin: int, current: int):
    return origin == current

def isNotVisited(visited: set, current_row: int, current_column: int):
    return (current_row, current_column) not in visited
        

"""
- image[sr][sc] == starting point
- same color 4-D as starting point are filled with color param

Steps
1. Get the value at the starting point ; origin value
2. Look in all directions
3. if new pixel is the same as origin value, add to queue

Negative Cases
- Out Of Bounds
- Not Same Color
"""
