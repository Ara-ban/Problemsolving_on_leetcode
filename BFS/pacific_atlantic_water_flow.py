#beats 75% in speed and 74% in memory
from collections import deque
class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        if not h:
            return []
        
        m, n = len(h), len(h[0])
        
        # Create visited matrices for both oceans
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]
        
        # Create queue for both oceans
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Add cells in the first and last m to their respective queues
        for col in range(n):
            pacific_queue.append((0, col))
            atlantic_queue.append((m-1, col))
            pacific_visited[0][col] = True
            atlantic_visited[m-1][col] = True
        
        # Add cells in the first and last columns to their respective queues
        for row in range(m):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, n-1))
            pacific_visited[row][0] = True
            atlantic_visited[row][n-1] = True
        
        # check if a cell can flow to pacific
        while pacific_queue:
            row, col = pacific_queue.popleft()
            # Check adjacent cells
            for dr, dc in [(0, 1), (1, 0),(0, -1), (-1, 0)]:
                r, c = row + dr, col + dc
                # Check if cell is within bounds and hasn't been visited yet
                if 0 <= r < m and 0 <= c < n and not pacific_visited[r][c]:
                    # Check if cell can flow to the ocean
                    if h[r][c] >= h[row][col]:
                        pacific_visited[r][c] = True
                        pacific_queue.append((r, c))
        # check if a cell can flow to atlantic
        while atlantic_queue:
            row, col = atlantic_queue.popleft()
            for dr, dc in [(0, 1), (1, 0),(0, -1), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and not atlantic_visited[r][c]:
                    if h[r][c] >= h[row][col]:
                        atlantic_visited[r][c] = True
                        atlantic_queue.append((r, c))
        
    
        
        # Find the cells that can flow to both oceans
        result = []
        for row in range(m):
            for col in range(n):
                if pacific_visited[row][col] and atlantic_visited[row][col]:
                    result.append([row, col])
        
        return result
