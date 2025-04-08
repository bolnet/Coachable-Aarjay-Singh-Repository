

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
LRUCache lRUCache = new LRUCache(2);
max_capacity initialized in thebenning

lRUCache.put(1, 1); // cache is {1=1}
add key value to cache so some kind of map for acccessing the elements

lRUCache.put(2, 2); // cache is {1=1, 2=2}
add key value to cache so some kind of map for acccessing the elements


lRUCache.get(1);    // return 1
get value from map
also it's updating the ordering so some kind of linked data structure.
    we need to keep recently used value to the beginning of the list
    we need to add and remove nodes so doubly linked list might be more useful here


lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
adding more values when cache is full. we need to remove last element from the linked list begore adding new elment at the beginning
also update the map if we remove or add the elements in this case remove key 2
lRUCache.get(2);    // returns -1 (not found)
if don't have keys than return defaul return value -1
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}

lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

    PLAN :
         Implement doubly link list
            - create Node with prev next and val element
            - initialize linkelist wih head, tail.
            - poiint head next to tail
            -point tail prev to head

            -implement remove a node
                -traverse linkedlist
                    -if you find the node
                    -get prevous node prev_node=node.prev
                    -get next node next_node=node.next
                    -prev point to next node. prev_node.next=next_node
                    next_node point to pre --> next_node.prev=pre_node

            -implment add node to head
                -check if head is None
                    create  a node
                    head=new_Node
                    new_node.next = tail
                    tail.pev= new_node
                if head is not None
                    - create a new_node
                    -new_node.next=head

                    head.pre =new_node

                    head -= new_node

            -move node will use remove and add methods



PLAN 2:
         Implement doubly link list
            -leverage deque  implementation

        -initialize deque to maintain ordering of nodes
        -initialize map to access cache

    def __init__(self, capacity: int)::
            initialize capacity
            intilaize deque
            initialize cache map
      def get(self, key: int) -> int:
          if value doesn't exsit in cache return -1
           if value exist in cache
                move the node to front of deque
                return value

        def put(self, key: int, value: int) -> None:
                check if we have available capacity
                    if yes:
                        add key value to cache
                        add node to the begining of the queue
                    if no
                        remove tail node from cache
                        add key value to cache
                        add node to the begining of the queue


PLAN 3: implement doublylinked list using dummy_node
    Initialized dummy head and tail.
    Use doublyt linked list to perform pop and appendLeft


'''
class Node:
    def __init__(self, key=None, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def appendLeft(self, key, val=None):
        return self.insertAfter(self.dummy_head, key, val)

    def appendRight(self, key, val=None):
        return self.insertBefore(self.dummy_tail, key, val)

    def insertAfter(self, node, key, val=None):
        next_node = node.next
        new_node = Node(key, val)

        node.next = new_node
        new_node.pre = node
        new_node.next = next_node
        next_node.pre = new_node

        return new_node

    def insertBefore(self, node, key, val=None):
        return self.insertAfter(node.pre, key, val)

    def remove(self, node):
        if node == self.dummy_head or node == self.dummy_tail:
            return False
        pre_node = node.pre
        next_node = node.next

        pre_node.next = next_node
        next_node.pre = pre_node

        return True

    def pop(self):
        if self.is_empty():
            return None

        last_node = self.dummy_tail.pre
        if last_node == self.dummy_head:
            return None

        self.remove(last_node)
        return last_node.key

    def is_empty(self):
        return self.dummy_head.next == self.dummy_tail

    def find_node_by_key(self, key):
        curr = self.dummy_head.next
        while curr != self.dummy_tail:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = DoublyLinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, node = self.cache[key]

        self.queue.remove(node)
        new_node = self.queue.appendLeft(key)

        self.cache[key] = (value, new_node)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            _, old_node = self.cache[key]
            self.queue.remove(old_node)
            new_node = self.queue.appendLeft(key)
            self.cache[key] = (value, new_node)
            return

        if len(self.cache) >= self.capacity:
            lru_key = self.queue.pop()
            if lru_key is not None and lru_key in self.cache:
                del self.cache[lru_key]

        new_node = self.queue.appendLeft(key)
        self.cache[key] = (value, new_node)
