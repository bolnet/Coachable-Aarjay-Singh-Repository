'''
  initialize stack
  clean string
  initialize two pointers start and end to zero
  if end  "-" or "+"
    push elmement from start to end to stack for future processing
  if end find "/" or "*" we process start end and end+1
    push the result to stack again
  initialize result to zero
  traverse stack
    -pop first element
    -check to any other element left in stack
        - this can be a "-"
            if yes multiple - with first element poped
    add pooped element to result
'''
import re


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        clean_string = re.sub(r'[\s]', '', s)
        index = 0
        start = 0
        end = 0
        while end < len(clean_string) - 1:
            if clean_string[end] == '+' or clean_string[end] == '-':
                while (start <= end):
                    stack.append(clean_string[start])
                    start += 1
                end += 1
                start = end
            elif clean_string[end] == '/':
                stack.append(int(clean_string[start]) // int(clean_string[end + 1]))
                end = end + 2
                start = end
            elif clean_string[end] == '*':
                stack.append(int(clean_string[start]) * int(clean_string[end + 1]))
                end = end + 2
                start = end
            else:
                end += 1
        result = 0
        while stack:
            val = int(stack.pop())
            if stack:
                op = stack.pop()
                if op == "-":
                    val = -1 * val
            result += val
        return result
