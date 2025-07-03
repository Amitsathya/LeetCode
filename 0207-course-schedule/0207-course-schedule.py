class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        finished = set()
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if course in finished:
                return True
            visited.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            finished.add(course)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True