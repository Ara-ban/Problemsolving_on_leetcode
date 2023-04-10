#beats 75% in soeed and 35% in memory
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #an island is a set of adjacent ones, the approach is to put all ones in aset then identify adjacent ones using bfs
        if not grid:
            return
        ones=set()
        rows=len(grid)
        cols=len(grid[0])
        for i in range (rows):
            for j in range (cols):
                if grid[i][j]=="1":
                    ones.add((i,j))
        count=0
        while ones:
            q=deque([ones.pop()])
            count+=1
            while q:
                row, col = q.popleft()
                for dr, dc in [(0, 1), (1, 0),(0, -1), (-1, 0)]:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and  (r,c) in ones:
                        ones.remove((r,c))
                        q.append((r,c))
        return(count)
