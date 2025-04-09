'''
[3,2,1,5,6,4].  k=2
[1,2,3,4,5,6].
         2
sort the array
    get the second last element from the array
    we can traverse fron the end of the list

O(nlogn). O(n). --> O(nlogn)

we can use a min heap of size k to solve thid problem.
    -initialize min heap
    -if  heap is full
         compare the incoming number with top element in heap
            if the top element is smaller than incoming number
                remove element from heap
                add the new element
    top element in heap is your kth larget element
O(logn)

https://www.loom.com/share/fcbd31cfe7d044259b566be5e1a7a1a4
'''
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif len(heap) >= k and num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heapq.heappop(heap)
