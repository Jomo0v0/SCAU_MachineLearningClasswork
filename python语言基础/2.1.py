mylist = [0, 1, 2, 3, 4, 5]
print(mylist)

print(mylist[4])
print(mylist[-4])
print(mylist[0:4])
print(mylist[:4])
print(mylist[4:])
print(mylist[0:4:2])
print(mylist[-5:-1:])
print(mylist[-2::-1])

mylist[3] = "小月"
print(mylist[3])
mylist[5] = "小楠"
print(mylist[5])
mylist[5] = 19978
print(mylist[5])
print(mylist)

mylist.append('han')
mylist.extend(['long', 'wan'])
print(mylist)

scores = [90, 80, 75, 66]
mylist.insert(1, scores)
print(mylist)

print(mylist.pop(1))
print(mylist)

print('wan' in mylist)
print('han' not in mylist)
print(mylist.count('wan'))
print(mylist.index('wan'))

print(range(10))
print(range(-5, 5))
print(range(-10, 10, 2))
print(range(16, 10, -1))