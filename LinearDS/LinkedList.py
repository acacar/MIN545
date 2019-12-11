import random


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, value):
        self.head = ListNode(value, self.head)
        self.size += 1

    def _get_node(self, pos):
        current = self.head         # Start "after" head
        for i in range(pos):      # jump ahead n-1 times
            current = current.next
        return current

    def insert(self, value, pos):
        if pos == 0:
            self.prepend(value)
            return
        if pos > len(self):
            raise IndexError(f"Position {pos} is out of bounds!")

        current = self._get_node(pos-1)
        current.next = ListNode(value, current.next)
        self.size += 1

    def chop_head(self):
        if len(self) < 1:
            raise IndexError("List is empty")
        else:
            self.head = self.head.next
            self.size -= 1

    def delete(self, pos):
        if len(self) <= pos or len(self) < 0:
            raise IndexError(f"Position {pos} is out of bounds")
        else:
            if pos == 0:
                self.chop_head()
            else:
                node_before = self._get_node(pos-1)
                node_before.next = node_before.next.next
                self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        temp = "["
        current = self.head
        while current is not None:
            temp += str(current) + ", "
            current = current.next
        if len(temp) > 0:
            return temp[:-2] + "]"
        else:
            return temp + "]"

    def __contains__(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __repr__(self):
        return str(self)


def test_list():
    mylist = LinkedList()
    for item in random.choices(range(100), k=10):
        mylist.prepend(item)
    print("Random list:", mylist)
    mylist.chop_head()
    print("After chop_head:", mylist)
    mylist.insert(value=111, pos=0)
    print("After prepend 111:", mylist)
    mylist.insert(value=222, pos=5)
    print("After insert 222 @5:", mylist)
    mylist.insert(value=999, pos=len(mylist))
    print("After insert 999 at end:", mylist)
    mylist.delete(pos=5)
    print("After deleting @5:", mylist)
    mylist.delete(pos=0)
    print("After deleting @0:", mylist)
    mylist.delete(pos=len(mylist)-1)
    print("After deleting last:", mylist)


test_list()
