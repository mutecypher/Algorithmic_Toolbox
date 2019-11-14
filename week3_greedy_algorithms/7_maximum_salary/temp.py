# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python3 program to convert a list 
# of integers into a single integer 
def convert(a): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res) 
  
# Driver code 
if __name__ == '__main__':
    data = int(input)
    a = data[1:]
print(convert(a)) 