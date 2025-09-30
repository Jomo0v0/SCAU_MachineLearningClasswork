str1 = "as"
int1 = -9
print(len(str1))
print(abs(int1))

fruits = ['Apple', 'Banana', 'Melon']
fruits.append('Grape')
print(fruits)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))

def filter_fruit(someList, d):
    for i in someList:
        if i == d:
            someList.remove(i)
    return someList
print(filter_fruit(fruits.copy(), 'Melon'))

def test(i, j):
    k = i * j
    return i, j, k
a, b, c = test(4, 5)
print(a, b, c)
print(type(test(4, 5)))

myFunction = abs
print(myFunction(-9))

def add(x, y, f):
    return f(x) + f(y)
print(add(7, -5, myFunction))

from functools import reduce
myList = [-1, 2, -3, 4, -5, 6, 7]
print(list(map(abs, myList)))

def powerAdd(a, b):
    return pow(a, 2) + pow(b, 2)
print(reduce(powerAdd, myList))

def is_odd(x):
    return x % 3
print(list(filter(is_odd, myList)))

print(sorted(myList))

def powAdd(x, y):
    def power(n):
        return pow(x, n) + pow(y, n)
    return power
myF = powAdd(3, 4)
print(myF(2))

f = lambda x: x * x
print(f(4))
print(list(map(lambda x: x * x, myList)))
print(reduce(lambda x, y: x + y, map(lambda x: x * x, myList)))

def powAdd1(x, y):
    return lambda n: pow(x, n) + pow(y, n)
lamb = powAdd1(3, 4)
print(lamb(2))

import keyword
print(keyword.kwlist)