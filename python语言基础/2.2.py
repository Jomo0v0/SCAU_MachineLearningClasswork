studentsTuple = ("ming", "jun", "qiang", "wu", [90, 80, 75, 66])
print(studentsTuple)

try:
    studentsTuple[1] = 'fu'
except TypeError:
    print('TypeError')

studentsTuple[4][1] = 100
print(studentsTuple)

print('ming' in studentsTuple)
print(studentsTuple[0:4])
print(studentsTuple.count('ming'))
print(studentsTuple.index('jun'))
print(len(studentsTuple))