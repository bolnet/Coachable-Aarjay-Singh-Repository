class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        result = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                result.append([low, high])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result

        '''
         firstList = [[0,2],[5,10],[13,23],[24,25]], 
         secondList = [[1,5],[8,12],[15,24],[25,26]]
         output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


        Input: firstList = [[1,3],[5,9]] 
        secondList = []
        Output: []
        this is a classic two pointer problem where we compare two intervals from two sorted list
            - start pointer finds the max of both the points
            - end pointer find teh min of both the points]
            -it's intersections if start less end pointer

      
        
        '''
