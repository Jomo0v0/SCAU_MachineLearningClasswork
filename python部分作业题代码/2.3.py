studentsSet = set([0, 1, 2, 3, 4, 5, 'han', 'long', 'wan'])
print(studentsSet)

studentsSet.add('xu')
print(studentsSet)

studentsSet.remove('xu')
print(studentsSet)

a = set("abcnmaaaaggsng")
print('a=', a)
b = set("cdfm")
print('b=', b)

x = a & b
print('x=', x)

y = a | b
print('y=', y)

z = a - b
print('z=', z)

new = set(a)
print(new)