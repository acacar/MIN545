
# def is_palindrome(s):

#     if len(s) <= 1:
#         return True
#     if s[0] == s[-1]:
#         return is_palindrome(s[1:-1])
#     else:
#         return False

def is_palindrome(s):
    stack = []
    stack.append(s)
    while len(stack) > 0: # not empty
        print(stack)
        tmp = stack.pop()
        if len(tmp) < 2:
            return True
        if tmp[0] != tmp[-1]:
            return False
        stack.append(tmp[1:-1])

import math

def simple_calc(s):

    stack = []

    tokens = s.split()

    for token in tokens:
        if token  == "+":
            stack.append(stack.pop() + stack.pop())
        elif token  == "*":
            stack.append(stack.pop() * stack.pop())
        elif token  == "-":
            tmp = stack.pop()
            stack.append(stack.pop() - tmp)
        elif token  == "/":
            tmp = stack.pop()
            stack.append(stack.pop() / tmp)
        elif token  == "v":
            stack.append(math.sqrt(stack.pop()))
        else:  # has to be a number
            stack.append(float(token))
             
    return stack.pop()
