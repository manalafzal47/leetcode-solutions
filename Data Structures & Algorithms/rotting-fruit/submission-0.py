class Solution:
    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        row, col = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                elif grid[r][c] == FRESH:
                    fresh_oranges += (
                        1 
                    )

        # missed a edge case; if there are no fresh oranges at min 0, then answer is just 0
        if fresh_oranges==0:
            return 0

        num_min = -1

        while q:
            q_size = len(q)
            num_min += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for r, c in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        fresh_oranges -= 1
                        q.append((r, c))
        
        if fresh_oranges == 0:
            return num_min

        else:
            return -1
