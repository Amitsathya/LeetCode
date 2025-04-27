class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        finished = set()
        graph = defaultdict(list)

        def dfs(course):
            if course in visited:
                return False
            if course in finished:
                return True

            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            finished.add(course)
            return True

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
