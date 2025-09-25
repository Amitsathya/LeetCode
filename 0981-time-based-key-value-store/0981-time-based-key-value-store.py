class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([timestamp, value])        

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.cache.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                l = m + 1
                res = values[m][1]
            else:
                r = m - 1
        return res       


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)