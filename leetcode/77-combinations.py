'''
    [1,2,3,4]
    combinations of size 2
        1,2
        1,3
        1,4
        2,1
        2,3
        2,4
        3,1
        3,2
        3,4
        4,3
        4,2
        4,1
    some are duplicate in this since order doesn't matter in combination
        1,2
        1,3
        1,4
        2,3
        2,4
        3,4

    this means we can only care sub list from start to len(list) not the beinning of the lis
    Permutation care about ordering

    now it's reuduce to dfs with back tracking
    base case will be when path is equal to k
    we iterate over start to n and find out a valid combination

'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(start, path):
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(start, n+1):
                path.append(i)

                dfs(i+1, path)

                path.pop()

        dfs(1, [])
        return result

