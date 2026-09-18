class Solution:
    def island(self, grid, i, j, visited):
        visited.add((i, j))
        rows, cols = len(grid), len(grid[0])
        
        if i > 0 and grid[i-1][j] == '1' and (i-1, j) not in visited:
            self.island(grid, i-1, j, visited)
        if i < rows - 1 and grid[i+1][j] == '1' and (i+1, j) not in visited:
            self.island(grid, i+1, j, visited)
        if j > 0 and grid[i][j-1] == '1' and (i, j-1) not in visited:
            self.island(grid, i, j-1, visited)
        if j < cols - 1 and grid[i][j+1] == '1' and (i, j+1) not in visited:
            self.island(grid, i, j+1, visited)     
    def numIslands(self, grid: List[List[str]]) -> int:
        visited  = set()
        islands  = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    self.island(grid , r , c, visited)

        return islands

        