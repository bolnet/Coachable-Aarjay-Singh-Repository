'''
    initilize global sum
    create a helper function to traverse tree using dfs
       iterate over list:
        isinteger then
         global_sum=global sum + integer valy * level
        else
            gobal_sum =global sum + dfs(getlist,depth+1
    return global sum
'''


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        global_sum = [0]

        def dfs(nestedList, depth):
            for list in nestedList:
                if list.isInteger():
                    global_sum[0] += list.getInteger() * depth
                else:
                    dfs(list.getList(), depth + 1)

        dfs(nestedList, 1)
        return global_sum[0]
