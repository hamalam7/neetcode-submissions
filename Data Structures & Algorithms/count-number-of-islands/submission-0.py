class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(ROWS) and c in range(COLS)
                        and grid[r][c] == "1" and (r,c) not in visit):
                            q.append((r, c))
                            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands