class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
                count += 1
            elif char == ")":
                if len(stack) == 0:
                    count += 1
                elif len(stack) > 0 and stack[-1] != "(":
                    count += 1
                elif len(stack) > 0 and stack[-1] == "(":
                    count -= 1
                    stack.pop()
        return count



        '''
          initialize stack
          counter
          iterate over string
            if "(" 
                increment count
            if ")" and stack is empty:
                increment count
            if ")" and stack is not enmpty
                - if stack last element is "("
                    - decrement
                - if stack last element is no "("
                    -increment
          return counter

        (((
        
        ())

        '''
