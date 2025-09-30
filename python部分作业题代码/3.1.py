s = '7'
num = int(s)
num -= 1
num *= 6
print(num)

salary = 1000
if salary > 10000:
    print("Wow!!!!!!!")
elif salary > 5000:
    print("That's OK.")
elif salary > 3000:
    print("5555555555")
else:
    print("Too low")

a = 1
while a < 10:
    if a <= 5:
        print(a)
    else:
        print("Hello")
    a = a + 1
else:
    print("Done")

heights = {'Yao': 226, 'Sharq': 216, 'AI': 183}
for i in heights:
    print(i, heights[i])

for key, value in heights.items():
    print(key, value)

total = 0
for i in range(1, 101):
    total += i
print(total)

for i in range(1, 5):
    if i == 3:
        break
    print(i)

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

for i in range(1, 5):
    if i == 3:
        pass
    print(i)

fruits = ['"Apple"', 'Watermelon', '"Banana"']
print([x.strip('"') for x in fruits])
print([x**2 for x in range(21) if x % 2])
print([m + n for m in 'ABC' for n in 'XYZ'])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])