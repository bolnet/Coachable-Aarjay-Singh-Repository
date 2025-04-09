class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_non_zero_nums = {}
        for index, val in enumerate(nums):
            if val != 0:
                self.index_to_non_zero_nums[index] = val

    def get_index_to_non_zero_nums(self):
        return self.index_to_non_zero_nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum_of_dot_product = 0
        index_to_non_zero_nums_2 = vec.get_index_to_non_zero_nums()
        for index in self.index_to_non_zero_nums:
            if index in index_to_non_zero_nums_2:
                sum_of_dot_product += index_to_non_zero_nums_2[index] * self.index_to_non_zero_nums[index]
        return sum_of_dot_product



'''
 0 1 2 3 4
[1,0,0,2,3]. 
[0,3,0,4,0]
 we need need to multiply and the numbers if both are non zero
  initialize a map to store the index and it's non zero value
  dot product will loop through with keys and find out if value in second vector is 
  non zero if  yes add to sum
  reut
'''
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
