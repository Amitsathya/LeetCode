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
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            finished.add(course)
            return True


        for pre, course in prerequisites:
            graph[course].append(pre)
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

