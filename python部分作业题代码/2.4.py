k = {"name": "weiwei", "home": "guilin"}
print(k["home"])
print(k.keys())
print(k.values())

k["like"] = "music"
k['name'] = 'guangzhou'
print(k)

print(k.get('edu', -1))

k.pop('like')
print(k)

print(dict(zip(('A', 'B', 'C'), [1, 2, 3])))