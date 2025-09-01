class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: set() for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].add(pre)
        visited, finished = set(), set()
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
        for c in adj:
            if not dfs(c):
                return False
        return True