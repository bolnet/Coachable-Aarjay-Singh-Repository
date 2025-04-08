
'''
Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)

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



'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        result = self.cache[key]
        self.queue.remove(key)
        self.queue.appendleft(key)
        return result


    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.queue.appendleft(key)
        else:
            last_value = self.queue.pop()
            if last_value in self.cache:
                del self.cache[last_value]
                self.cache[key] = value
                self.queue.appendleft(key)
