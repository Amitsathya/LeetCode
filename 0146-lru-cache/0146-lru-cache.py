class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
    
    def insert(self, node):
        prev, curr = self.right.prev, self.right
        prev.next = curr.prev = node
        node.prev, node.next = prev, curr
    
    def remove(self, node):
        prev, curr = node.prev, node.next
        prev.next, curr.prev = curr, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)