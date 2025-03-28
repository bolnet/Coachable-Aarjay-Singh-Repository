class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result=[]
        max_element=heights[0]
        for i in range(len(heights)):
            if(heights[i] > max_element):
                result=[]
            if(i==len(heights)-1):
                result.append(len(heights)-1)
                break

            if heights[i] > heights[i+1]:
                result.append(i)

        return result


