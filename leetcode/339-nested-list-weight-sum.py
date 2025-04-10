# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# [1,[4,[6]]]
#  for i in list
#.     if  i integer:
#           add to total
#        else to recursive reuslt to total\

class Solution:
      def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def nested_integers_sum(nestedInteger:NestedInteger,depth:int)->int:
            if nestedInteger.isInteger():
                return nestedInteger.getInteger()  * depth
            sum_of_nested_integers = 0
            for child_nested_integer in nestedInteger.getList():
                    sum_of_nested_integers+=nested_integers_sum(child_nested_integer,depth+1)
            return sum_of_nested_integers
        result = 0
        for nestedInteger in nestedList:
            result+=nested_integers_sum(nestedInteger,1)
        return result

