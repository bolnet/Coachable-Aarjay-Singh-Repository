class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
            initiliaze right to  left  parenthesis map
            initialize result array
            initialize empty stack hold result index and opening parenthesis
            iterate over string
                -check if it's opening parenthesis
                    get the current result index where value will be added
                    add the value
                    create tuple with value and result index and push to stack
                -if it's closing parenthesis
                    check if stack is empty
                        -if yes skip this parenthesis
                        -if no check if it's mathing to last element in stack
                            -if yes pop stack
            if stack is not empty
                pop elmeent from stack and find out result index
                -remove elements from result using this index
            return result

        '''

        stack = []
        right_to_left_paren_map = {")": "("}
        result = []
        result_index = 0
        for val in s:
            if val in right_to_left_paren_map.values():
                stack.append((val, result_index))
                result_index += 1
                result.append(val)
            elif val in right_to_left_paren_map and len(stack) > 0 and right_to_left_paren_map[val] == stack[-1][0]:
                result.append(val)
                result_index += 1
                stack.pop()
            elif val in right_to_left_paren_map and len(stack) == 0:
                continue
            else:
                result.append(val)
                result_index += 1

        if len(stack) > 0:
            while stack:
                val, i = stack.pop()
                result.pop(i)

        return ''.join(result)
