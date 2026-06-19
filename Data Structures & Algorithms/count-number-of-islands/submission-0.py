class Solution:
    def traverse(self, grid, x, y):
        if x < 0 or y >= len(grid[0]) or y < 0 or x >= len(grid):
            return
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        self.traverse(grid, x-1, y)
        self.traverse(grid, x+1, y)
        self.traverse(grid, x, y-1)
        self.traverse(grid, x, y+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.traverse(grid, x, y)
                    count+=1
        return count
        