class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        # left.next point to least recently used, right.prev point to the most recently used
        # left is head, right is tail
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
    # remove from the list
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    # insert to the right most of the linklist (most recently used)
    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node
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
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)