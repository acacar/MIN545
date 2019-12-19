## Stacks with arrays

class ArrayStack():

    def __init__(self):
        self._data = []
        self._size = 0

    def push(self, item):
        if len(self._data) > self._size:
            self._data[self._size] = item
        else:
            self._data.append(item)
        self._size += 1
        
    def pop(self):
        if len(self) == 0:
            raise IndexError("Stack is empty")
        self._size -= 1
        return self._data[self._size]

    def __len__(self):
        return self._size

# Or better:

mystack = []
mystack.append("a")
mystack.pop()

from LinkedList import LinkedList

class ListStack:

    def __init__(self):
        self._data = LinkedList()

    def __len__(self):
        len(self._data)

    def push(self, item):
        self._data.prepend(item)
        
    def pop(self):
        if len(self._data) == 0:
            raise IndexError("Stack is empty")
        temp = self._data.head.value
        self._data.chop_head()
        return temp

s = ListStack()

s.push("a")
s.push("b")
s.push("c")
s.push("d")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

