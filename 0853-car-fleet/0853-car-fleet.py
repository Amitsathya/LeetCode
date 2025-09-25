class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)