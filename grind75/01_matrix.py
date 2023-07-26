class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        zero_locations = self.find_all_zeros(mat, visited)
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]

        while zero_locations:
            row, column, steps = zero_locations.popleft()
            
            for row_offset, column_offset in directions:
                new_row, new_column = row + row_offset, column + column_offset
                if self.is_coordinate_valid(mat, new_row, new_column) and (new_row, new_column) not in visited:
                    mat[new_row][new_column] = steps + 1
                    zero_locations.append((new_row, new_column, steps + 1))
                    visited.add((new_row, new_column))
        return mat

        
    def find_all_zeros(self, matrix: List[List[int]], visited: set):
        rows, columns = len(matrix), len(matrix[0])
        zeros = deque()

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    zeros.append((row, column, 0))
                    visited.add((row, column))
        
        return zeros

    def is_coordinate_valid(self, matrix, row, column):
        return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])
