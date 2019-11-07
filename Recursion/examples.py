### Factorial


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)



### List all binary numbers

def list_binary_numbers(n): # n = number of bits
    if n == 0:
        return []
    elif n == 1:
        return ["0","1"]  
    else:
        tmp = []
        for i in list_binary_numbers(n-1):
            tmp.append( "0" + i )
            tmp.append( "1" + i )
        return tmp


### Ways to make change for X Liras
    
denominations = [100, 50, 20, 10, 5, 1]
    
def make_change(amount, accumulated = '', last_idx = 0):

    if amount == 0:
        print(accumulated[0:-2]) ## [0:-2] => Throw out the extra ", " at the end.

    for i in range(last_idx, len(denominations)):
        d = denominations[i]
        if amount >= d:
            make_change(amount= amount - d,
                        accumulated= str(d) + ", " + accumulated,
                        last_idx= i)

### Searching on an already sorted list

from random import Random

list_to_search = sorted([Random().randint(0,1000) for i in range(200)])

def find(target, mylist):
    for item in mylist:
        if target == item:
            return True
    return False


def binary_search(data, target, low, high):
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return mid
    elif target < data[mid]:
      return binary_search(data, target, low, mid-1)
    else:
      return binary_search(data, target, mid+1, high)

