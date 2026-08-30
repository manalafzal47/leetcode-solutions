class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # first check if there is an empty list, the graph will still be valid
        if not n:
            return True
        
        # create an adjacency list for the neighbors
        adj = {i: [] for i in range(n)}
        # since the direction of the edges dont matter, the adjacency list holds both nodes 
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        # DFS recursive algorithm that has the index of the node and the prev            
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            # check the neighbors of each node
            for j in adj[i]:
                if j == prev:
                    continue
                # if we get False return value, then we have detected a cycle. 
                # notice that our j value is the current value and i is the prev value which is the parent node
                if not dfs(j,i):
                    return False
            # otherwise, we are returning true, if we check all nodes and it does not have a cycle
            return True
            
        return dfs(0,-1) and n == len(visited)
                
                