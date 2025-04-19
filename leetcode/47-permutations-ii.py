class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        N = len(nums)
        '''
            create permuatations for each number
            1  1  2 
            1  2  1
            1  1  2
            1  2  1

            we can use dfs to build permutations one element at a time
                tracking used element at each recursion call
                skip the element we already used
                maintain path to build the permutation
                
        '''

        def dfs(nums, path):
            if len(path) == N:
                result.append(path.copy())
            used = set()
            for index in range(len(nums)):
                if nums[index] in used:
                    continue
                used.add(nums[index])
                path.append(nums[index])
                dfs(nums[:index] + nums[index + 1:], path)
                path.pop()

        dfs(nums, [])
        return result
