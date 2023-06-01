class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        while len(q) > 0: 
            x, y , level = q.pop(0)
            if x == n - 1 and y == n - 1: 
                return level 
            for ix, iy in ((x - 1, y -1), (x + 1, y + 1), (x -1, y), (x + 1, y), (x, y -1), (x, y +1), (x - 1, y + 1), (x + 1, y - 1)):
                if 0 <= ix < n and 0 <= iy < n and grid[ix][iy] == 0: 
                    grid[ix][iy] = 1
                    q.append((ix, iy, level+1))
        return -1