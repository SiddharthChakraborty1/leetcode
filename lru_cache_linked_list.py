class Node:

    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: "Node | None" = None
        self.next: "Node | None" = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None
    
    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_after_head(self, node:Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int):
        if key not in self.cache:
            return -1
        
        node = self.cache.get(key)
        self._remove(node)
        self._insert_after_head(node)
        return node.val
    
    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value
            self._remove(node)
            self._insert_after_head(node)
            return
        
        if len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_after_head(new_node)


        
