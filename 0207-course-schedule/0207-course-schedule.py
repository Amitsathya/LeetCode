class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : set() for i in range(numCourses)}
        visited, finished = set(), set()
        for course, pre in prerequisites:
            adj[course].add(pre)
        def dfs(i):
            if i in finished:
                return True
            if i in visited:
                return False
            visited.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visited.remove(i)
            finished.add(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        