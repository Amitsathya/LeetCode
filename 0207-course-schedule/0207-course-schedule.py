class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            adj[c].append(pre)
        visited = set()
        finished = set()
        def dfs(c):
            if c in visited:
                return False
            if c in finished:
                return True
            visited.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            finished.add(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
