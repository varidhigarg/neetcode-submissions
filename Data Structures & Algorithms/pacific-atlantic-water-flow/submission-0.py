class Solution:
    def dfs(self, heights, x, y, visited):
        t = tuple([x, y])
        if t in visited:
            return
        visited.add(t)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr in directions:
            dx = x + dr[0]
            dy = y + dr[1]
            if dx < 0 or dx >= len(heights) or dy < 0 or dy >= len(heights[0]):
                continue
            if heights[dx][dy] >= heights[x][y]:
                self.dfs(heights, dx, dy, visited)


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if x == 0 or y == 0:
                    self.dfs(heights, x, y, pacific)
                if x == len(heights) - 1 or y == len(heights[0]) -1:
                    self.dfs(heights, x, y, atlantic)
        
        res = pacific & atlantic
        return list(map(lambda x: list(x), res))
                
        