print("Hello, world")


def myfunction(x):
    print("I just ran my function")
    return x ** 2


myfunction(4)


def foo(name, isSpanish=False):
    if isSpanish:
        return f'Hola, {name}'
    else:
        return f"Hello, {name}"


print(foo("Bob", 1))


myfunction(4)

x = 4
x


x += 2
# i.e. x = x + 2

mylist = ['a', 4, 74, 92, 2.3, 5]

mylist

mylist[1:-1]

s = "some string"

s.split(" ")


s1 = "Something"
s2 = s1

s2 = s2 + " else"


list1 = [1, 2, 3, 4, 5]
list2 = list1

list2[4.8] = 82992
s2.ex

s2 = s


class Counter:
    def __init__(self):
        self._count = 0

    def tick(self):
        self._count += 1

    def get_count(self):
        return self._count

    def reset(self, newcount=0):
        self._count = newcount
