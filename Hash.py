class ItemNode:

    def __init__(self, item, key, next):
        self._item = item
        self._key = key
        self._next = next


class HashTable:

    INITIAL_MERSENNE_NUMBER = 3 #
    
    def __init__(self):
        self._capacity = HashTable.INITIAL_MERSENNE_NUMBER
        self._data = [None] * (2 ** self._capacity - 1)
        self._size = 0

    def get(self, key):
        hashval = abs(hash(key)) % len(self._data)
        hashbucket = self._data[hashval]
        while hashbucket is not None:
            if hashbucket._key == key:
                return hashbucket._item
            hashbucket = hashbucket._next
        raise KeyError("No such key: " + str(key))

    def add(self, key, item):
        loadfactor = self._size / len(self._data)
        if loadfactor > 0.66:
            self._resize()
        hashval = abs(hash(key)) % len(self._data)
        self._data[hashval] = ItemNode(item, key, self._data[hashval])
        self._size += 1

    def delete(self, key):
        hashval = abs(hash(key)) % len(self._data)
        hashbucket = self._data[hashval]
        if hashbucket is None:
            raise KeyError("No such key: " + str(key))
        elif hashbucket._key == key:
            self._data[hashval] = hashbucket._next
            self._size -= 1
            return hashbucket._item
        elif hashbucket._next is None:
            raise KeyError("No such key: " + str(key))
        while hashbucket._next is not None:
            if hashbucket._next._key == key:
                temp = hashbucket._next._item
                hashbucket._next = hashbucket._next._next
                self._size -= 1
                return temp
            hashbucket = hashbucket._next
            
    def _resize(self):
        old_table = self._data
        self._capacity += 1
        self._data = [None] * (2 ** self._capacity - 1)
        self._size = 0
        for bucket in old_table:
            while bucket is not None:
                self.add(bucket._key, bucket._item)
                bucket = bucket._next
        
    
