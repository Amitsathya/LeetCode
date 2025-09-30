class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c: [] for c in range(numCourses)}
        for c, pre in prerequisites:
            prereq[c].append(pre)
        
        output = []
        visit, cycle = set(), set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for nei in prereq[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            visit.add(c)
            output.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output