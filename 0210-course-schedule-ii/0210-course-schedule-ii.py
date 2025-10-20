class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        visit, cycle, res = set(), set(), []
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res