'''
[[[1]],[]]

[null,0]

[[[1,3]],[],[],[],[],[]]
1 / 1+3
3 / 1+3  ==> return index =1

[[[1,3]],[],[],[],[],[]]
Solution solution = new Solution([1, 3]);
For example, if w = [1, 3],
the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 [1, 3]
 [1,4]
 total=4

target number range in 1 to 3 total * random()
  iterate over prefix array
  if target is less than vale than return the index


 [1,2,3,4,5,6,7,8,9]

    initialilzed  wiht array
        -initialized prefix sum array
        -calculate total sum
    pick index:
        -calculate target using total sum and random number
            - it will generate a number in the range prefix arary
        iterate over prefix array
            - check if target is less than prefix value if yes return index



prefix_sum=[]
[1,2,3,4,5]
[0,0,0,0,0]
[1,3
[1,3,6,10,15] prefix_sum
total_sum=

15 * .75 =11.0
https://www.loom.com/share/784dda1913a5419b85e423d443170459
https://www.loom.com/share/70aa3ce4b84a4737b224d0a79c839313
'''
import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0 for i in range(len(w))]
        self.prefix_sum[0] = w[0]
        for i in range(1,len(w)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]
        self.total = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        target = self.total * random.random()
        for index,weight in enumerate(self.prefix_sum):
            if target < weight:
                return index
        return -1




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
