
class Item:
    def __init__(self, value, key):
        self._val = value
        self._key = key

    def __lt__(self, other):
        return self._key < other._key

    def __gt__(self, other):
        return self._key > other._key

    def __str__(self):
        return str(self._key) +  ": " + str(self._val)
    

class Heap:

    def __init__(self):
        self._heapArray = []

    def __len__(self):
        return len(self._heapArray)

    def __str__(self):
        return str(self._heapArray)

    def __repr__(self):
        return str(self)
    
    def is_empty(self):
        return 0 is len(self)

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self)

    def _has_right(self, i):
        return self._right(i) < len(self)

    def _swap(self, i , j):
        self._heapArray[i], self._heapArray[j] = self._heapArray[j], self._heapArray[i]
    
    def _trickle_up(self, i):
        #Base
        if i <= 0:
            return
        parent_idx = self._parent(i)
        if self._heapArray[parent_idx] < self._heapArray[i]:
            self._swap(parent_idx, i)
            self._trickle_up(parent_idx)

    def add(self, value, key):
        item = Item(value, key)
        self._heapArray.append(item)
        self._trickle_up(len(self) - 1)

    def _trickle_down(self, i):
        if self._has_left(i):
            left_idx = self._left(i) #big child idx
            bigchild = left_idx
            if self._has_right(i):
                right_idx = self._right(i)
                if self._heapArray[left_idx] < self._heapArray[right_idx]:
                    bigchild = right_idx
            if self._heapArray[bigchild] > self._heapArray[i]:
                self._swap(i, bigchild)
                self._trickle_down(bigchild)

    def max(self):
        return self._heapArray[0]._val, self._heapArray[0]._key

    def delete(self):
        self._swap(0, len(self) - 1)
        retval = self._heapArray.pop()
        self._trickle_down(0)
        return (retval._val, retval._key)
        
        
