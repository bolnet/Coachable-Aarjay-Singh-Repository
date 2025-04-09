'''
"/home/"
   if last character is / or // or /// remove them

"/home//foo/"
  replace // with /

/home/user/Documents/../Pictures
 if .. encountered that means  remove previous directory

/../. we can't go up if we are at / rootlevel


/.../a/../b/c/../d/./

... is a valid directory name

"/.../a/../b/c/../d/./"
traverse string
    -push all the elements to stack
    - if char is "/"
        -keep / conter
        -check if you reach to the end of strig
            -if yest pop stack counter times
            - else pop stack counter -1 times
    - if char is .
        -keep check if next char is .
        -combine all the dots
        - keep a counter for dot each time you encounter a .
            -if counter reaches to 3 or more than we don't need to do anything
            -if counter reaches to 2 than pop 5 times make sure not to pop root
            -if counter reaches to 1 than pop twice

/.../b/d


PLAN 2:
    use two pointers instead of stack
    -initialized two pointers at the beginning of of the string at 0
    iterate string
        - if char is "/" keep increment end pointer until u hit some other char
        -check if end reaches to the end of string
            if yes:
                we don't need to add any "/"
            else;
                add char to result and reset start to point end
        -check if char is '.'
            - keep incrementing end pointer until non "." char
            - calculate the difference of end - start
            - if diff is 3 or "." than add that many . in the result
            -if diff is  2 then pop thrice
            -if diff is 1 than pop twice





'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        index = 0
        while index < len(path):
            char = path[index]
            if char == '/':
                while index < len(path) and path[index] == '/':
                    index += 1
                if index <= len(path) - 2:
                    stack.append(char)
            elif char == '.':
                count = 0
                while index < len(path) and path[index] == '.':
                    stack.append(char)
                    count += 1
                    index += 1
                if count == 1:
                    for _ in range(2):
                        stack.pop()

                elif count == 2:
                    for _ in range(5):
                        stack.pop()
            else:
                stack.append(char)
                index += 1

        return ''.join(stack)
