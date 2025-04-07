'''
 s = "3+2*2"
 return 7
multiplicatin and division have precedence over plus and miinus

('+', '-', '*', '/')

"  3 + 2 * 2"
           |
   3 -> + -> 2
    *
        get next elmenet
        pop previous elemen
        perform operation
        push it back ot stack
  3-> + ->4
  once we exhast the string then we know it will be additona or sbtraction of two elements
 pop element
 pop operation
 pop element
 perform operation
 retunr resuls

  " 3/2 "
  3 ->
    /
        get next element 2
        pop stack 3
        perform operation
        push to stack
  if stack size is 1 than it's a result

  " 3+5 / 2 "
  3->+->5
        /
        get next element
        pop stack
        perform operation
        push it to stack
  3-> + -> 2

  check if stack len 1 no
  pop find element
  pop to find operation
  pop to fin elemen
  perform operation
  return result

  PLAN:
  initilize stack
  define operation funcitons
   "+"  add()
   "-"  subract()
   "*" multiplication
   "/" divition
   iterate the string
        if character is number than push to stack
        if it's + or - than push to stack as well
        if encounter / or * get the next element from string if it's available
        pop the stack to get previous number
        use current character to invoke / division( pass number in stack , next numver)
        push the result back to stack
        repeat this process till the end of strig
    check if stack len is 1 if yes pop the element and it';s the result
    else
        pop first number
        pop opertiono to perdom
        pop second number
        perform operation
    return result




'''
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        index=0
        while index < len(s)-1:
            if s[index] ==' ':
                index+=1
                continue
            if s[index]=='/' or s[index]== "*":
                second_number_index=index+1
                if(s[second_number_index]==' '):
                    second_number_index=index+2

                if second_number_index < len(s)-1:
                    second_number=int(s[second_number_index])
                    first_number=int(stack.pop())
                    if s[index]=='/':
                        stack.append(first_number // second_number)
                    else:
                        stack.append(first_number * second_number)
                    if second_number_index > index+1:
                        index+=2
                    else:
                        index+=1
            else:
                stack.append(s[index])
            index+=1

        if len(stack)==1:
            return stack.pop()
        else:
            second_number=int(stack.pop())
            char=stack.pop()
            first_number=int(stack.pop())

            if char=='/':
                return first_number // second_number
            else:
                return first_number * second_number
