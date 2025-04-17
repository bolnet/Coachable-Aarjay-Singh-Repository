from collections import deque
from collections import  defaultdict

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([(0, 0),0])
        visited = {(0, 0)}
        distance = 1
        n = len(grid)
        target = (n - 1, n - 1)
        bfs_levels=defaultdict(list)
        while queue:
            level_size = len(queue)
            cell,level = queue.popleft()
            bfs_levels[level].append(cell)
            #for _ in range(level_size):

              #  if cell == target:
                 #   return distance
            for dx, dy in directions:
                    current_x = cell[0] + dx
                    current_y = cell[1] + dy
                    if 0 <= current_x < len(grid) and 0 <= current_y < len(grid[0]):
                        if (current_x, current_y) not in visited and grid[current_x][current_y] != 1:
                            queue.append((current_x, current_y),level+1)
                            visited.add((current_x, current_y),level+1)

        for key in range(len(bfs_levels)):
            if bfs_levels[key] == target:
                return key
        return -1

    def shortestPathBinaryMatrix_single_pass(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([((0, 0), 1)])
        visited = {(0, 0)}
        n = len(grid)
        target = (n - 1, n - 1)
        bfs_levels = defaultdict(list)
        while queue:
            cell, level = queue.popleft()
            bfs_levels[level].append(cell)
            for dx, dy in directions:
                current_x = cell[0] + dx
                current_y = cell[1] + dy
                child_node = ((current_x, current_y), level + 1)
                if 0 <= current_x < len(grid) and 0 <= current_y < len(grid[0]):
                    if child_node[0] not in visited and grid[current_x][current_y] != 1:
                        queue.append(child_node)
                        visited.add(child_node[0])

        for key in range(1, len(bfs_levels) + 1):
            if target in bfs_levels[key]:
                return key
        return -1






        '''
        0  1. 
        1  0.   

        0 0 0
        1 1 0.   
        1 1 0 

        matrix is connected 8 dirctionaly
        directions =[(1,0),(0,1)(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        start with 0,0 and keep traversing in each direction untill you reach the end of the matrix
        if you reach to n-1 and n-1 cell that means we reach to the end of the path
        keep track of shortest_path as global

        PLAN;
        initialize directions:
        initialize shortes_path
        start with 0,0 and iteratively check all the directions
         -use directions list to move in one directions and keep incrementing in same directions untill you reach to the end
         -you need to back track to explore another path if end doesn't result 
        repead this process


        PLAN -2
            it's  unweighted graph traversal
            - BFS always yeilds shortes path
            - initialize valid directions in a list
            -initialize queue
            -initialize visited cells
            -initialize initial distance
            - get the level size using queue size
                - iterate over all the  cell at this level
                    - if cell is a target return the distance
                    - find all the childerens using direction list
                    - find the valid cell if cell are in matrix boundary
                    - find the valid cell don't have 1
                    -cell is not already visited
                    -add the cell to queue
                    
                 increment distance  


            -

        '''
