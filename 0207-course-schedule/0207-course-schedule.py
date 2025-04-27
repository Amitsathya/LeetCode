class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hashMap = {i:[] for i in range(numCourses)}
        for cse, pre in prerequisites:
            hashMap[cse].append(pre)
        
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if hashMap[course] == []:
                return True
            
            visiting.add(course)
            for pre in hashMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            hashMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        