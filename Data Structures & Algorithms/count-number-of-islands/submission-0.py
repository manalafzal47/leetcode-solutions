from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return len (of islands)

        # BFS PROBLEM
        # standard bfs problem. where the problems checks each unvisited cell in the grid

        # initialize row and column, and count variable, visited set to check if you have already visited this.if 

        # check for any unvisted 1's and check each nearby cells in all adjacent directions (left, right, top, bottom) and seperated by water cells
        # add to queue if 1
        # increment count variable 
        # create a queue to hold next visited cells

        WATER, LAND = "0", "1"
        row, col = len(grid), len(grid[0])
        count = 0
        # visited = set()
        
        directions=[[0,1], [1,0], [-1,0], [0,-1] ]

        # running the bfs function  
        def bfs(r,c):
            queue = deque()
            grid[r][c]=WATER # mark cell as visited
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc=dr+r, dc+c
                    if (nr<0 or nc<0 or 
                        nr>=row or nc>=col or 
                        grid[nr][nc] == WATER):
                            continue
                    queue.append((nr,nc)) # meaning land cell , append to queue
                    grid[nr][nc]=WATER

        # checking each cell
        for r in range(row):
            for c in range(col):
                if grid[r][c]==LAND:
                    bfs(r,c)
                    count+=1

        return count