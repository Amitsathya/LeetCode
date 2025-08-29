class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, finished = set(), set()
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        def dfs(n):
            if n in visited:
                return False
            if n in finished:
                return True
            visited.add(n)
            for nei in adj[n]:
                if not dfs(nei):
                    return False
            visited.remove(n)
            finished.add(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True