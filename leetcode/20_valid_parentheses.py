class Solution:
    def isValid(self, s: str) -> bool:
        '''
         "()"
                [(]
                []
                return true
        "()[]{}"
                []        
                return true
            "(]"       [( ]
            return false
            "([])"
                    []
                    return true
        PLAN:
        initilize left to right parenthesis map
        initilize stack to keep track the valid parenthesis
        iterrate string
            if it's left paren add to stack
            if it's  right parenthesis  and stack is not empty
                check if matches to last elment in stack
                    if yes pop stack
                if no matching return false

                if stack is empyt then return false. we found right parenthesis before left
            check stack len if it's zero than we have mathing parenthesis
        
        '''
        left_to_right_paren_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in left_to_right_paren_map.values():
                stack.append(i)
            elif len(stack) != 0 and left_to_right_paren_map[i] == stack[-1]:
                stack.pop()
            elif len(stack) != 0 and left_to_right_paren_map[i] != stack[-1]:
                return False
            elif len(stack) == 0:
                return False
        return len(stack) == 0
