class Node:
    def __init__(self, key=None, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        cache_value, cache_node = self.cache[key]
        curr = self.dummy_head.next
        while curr != cache_node:
            curr = curr.next
        self.remove(curr)
        self.add_to_the_front(cache_node)
        return cache_value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cache_value, cache_node = self.cache[key]
            curr = self.dummy_head.next
            while curr != cache_node:
                curr = curr.next
            self.remove(curr)
        if len(self.cache) >= self.capacity:
            lru_node = self.dummy_tail.pre
            self.dummy_tail.pre = lru_node.pre
            if lru_node.key in self.cache:
                del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.add_to_the_front(new_node)
        self.cache[key] = (value, new_node)

    def remove(self, curr):
        pre_node = curr.pre
        next_node = curr.next
        pre_node.next = next_node
        next_node.pre = pre_node

    def add_to_the_front(self, curr):
        next_node = self.dummy_head.next
        self.dummy_head.next = curr
        curr.pre = self.dummy_head
        curr.next = next_node
        next_node.pre = curr
