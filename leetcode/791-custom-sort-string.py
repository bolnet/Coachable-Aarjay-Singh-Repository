
'''
    order=cba s =abcd
    c-0          a in order yes add to frequency map
    b=1           b on 
    a=2

    order= b c a f g
           0 1  2 3 4
    s=abcd
    result
      create a frequency map from string
      - iterate over order string
        - if char in frequency map than get the frequency
        - based on frequncy add  char to result
        -remove the entry from map
      -if map still have remainig char 
        -iterrate overr it's key value an add the char to result
   
      -

    output =cbad
https://www.loom.com/share/e3084c8dc7da4915b326552b90d3d91c
'''
from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequency_count=defaultdict(int)
        result = []
        for char in s:
            frequency_count[char]+=1

        for char in order:
            if char in frequency_count:
                count = 0
                while count < frequency_count[char]:
                    result.append(char)
                    count += 1
                del frequency_count[char]

        for char, value in frequency_count.items():
            count=0
            while count < value:
                result.append(char)
                count += 1
        return ''.join(result)

