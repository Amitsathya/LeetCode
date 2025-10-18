class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = { i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        visited, cycle = set(), set()
        output = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

        