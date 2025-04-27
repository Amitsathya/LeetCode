class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if (n - 1) != len(edges): return False

        hashMap = {i: [] for i in range(n)}
        for a, b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)
        
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in hashMap[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

        