'''
heights = [4,2,3,1] ||
           4 > 2 yes
           2 > 3 No
           3 > any of visited no 3 is not blocking view
           3 > 1 that means yes
           1 is the last not so yes

Input: heights = [4,3,2,1]
                1 yes biggest so far =1
                2 > 1 yes biggest so far 2
                3 > 2 and bigger than biggest 2 so update that to 3
                4 > 3 and bigger than biggest so update the biggest

                0,1,2,3,


heights = [1,3,2,4]
                    4 yes biggest=4
                    2 < 4 no
                    3 > 2 yes 3 > biggest no
                    1 < 3 no
                answer 3

PLAN
initilaize biggest with last_number in array
last_element with last_number in array
initilize the result. add the last index

start traversing from second last element n-2 -> 0
    check if element is bigger than biggest
        if yes check if it's bigger then the last_element
            if yes add it's index to result
        update biggest
    repeat this process
return result


https://www.loom.com/share/45867f57ccf245d89fca46328d596ecb


'''


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) < 0:
            return heights
        result = []
        biggest = heights[-1]
        last_element = biggest
        result.append(len(heights) - 1)
        for index in range(len(heights) - 2, -1, -1):
            if heights[index] > biggest:
                if heights[index] > last_element:
                    result.append(index)
                biggest = heights[index]
            last_element = heights[index]

        r = []
        while result:
            r.append(result.pop())
        return r
