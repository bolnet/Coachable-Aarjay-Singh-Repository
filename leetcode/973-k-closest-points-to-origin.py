import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x1, y1 in points:
            distance = -1 * math.sqrt((x1 ** 2 + y1 ** 2))
            if len(heap) < k:
                heapq.heappush(heap, (distance, (x1, y1)))
            elif heap[0][0] < distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (distance, (x1, y1)))
        result = []
        while heap:
            result.append(heappop(heap)[1])
        return result

'''
    origin is (0,0)
   x= (x2-x1) ** 2
   y= (y2-y1) **2
   distance =sqrt(x+y)
   create max heap to store k value
distances=[4,1,3,2,8,5]

k=2
[-4]
[-1 -4]
[-1 -3]
[1 2]
[1 2]


PLAN :
    iterate over list
        calculate x
        calculate y
        calculate distance
        check if heap size is less than k
            if yes
                push to max heap . it's negative to min heap value
            if no 
                check if value is bigger than top elmenet in heap
                if yes:
                    pop the elemet from heap
                    push this element into heap


'''
