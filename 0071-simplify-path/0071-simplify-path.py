class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for c in components:
            if c == "" or c == ".":
                continue
            
            if c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "/" + "/".join(stack)