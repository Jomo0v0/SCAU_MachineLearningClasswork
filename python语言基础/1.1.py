print('hello world!')
c = 'It is a"dog"!'
print(c)
c1 = "It's a dog!"
print(c1)
c2 = """hello world!"""
print(c2)

print('It\'s a dog!')
print("hello world!\nhello Python!")
print('\\\t\\')
print(r'\\\t\\')

s = 'Python'
print('Py' in s)
print('py' in s)
print(s[2])
print(s[1:4])

word1 = '"hello"'
word2 = '"world"'
sentence = word1.strip('"') + ' ' + word2.strip('"') + '!'
print('The first word is %s, and the second word is %s' % (word1, word2))
print(sentence)