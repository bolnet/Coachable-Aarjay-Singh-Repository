'''
      PLAN -2
            - if number is bigger than it's neighbors than it's a peek
            - if middle element greater than right neighbor downward slope
            - if middle element smaller than right neighbor upward slope
            we can use reduce this problem to follow the slope using binary search.

'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

        return lo

    '''
    def findPeakElement(self, nums: List[int]) -> int:
        
         [1,    2,   3,    1]
          i    i+1  i+2.      
         use three pointers
         if lo mid high 
         if  lo <= mid <= high return mid
        PLAN:
            initialize three pointers start mid, end
            traverse list
                find mid such that start < mid. < end 

  

            initialize lo=0 hi=len(nums)-1
            iterate till lo and hi is not equal
                - calculate mid
                    - check if we upward slope if yes than peek is on the right side.
                    - check if we have downward slope than peek is on the left side
                repeat this process
            

        

        if len(nums) < 3 :
            return -1
        start=0
        mid=1
        end=2
        while end < len(nums):
            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                return mid
            start+=1
            mid=mid+1
            end+=1
        
        return -1
def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) < 3 :
            return -1
        index=0
        while index < len(nums)-1:
            if nums[index] > nums[index+1]:
                return index
            index+=1
        
        
        return len(nums)-1
'''
