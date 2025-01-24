mySet = {
    "brand": "ford",
    "model": "mustang",
    "year": 1965
}

print(mySet.get("brand"))

mySet2 = mySet.copy()
print(mySet2)

mySet3 = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(mySet3, y)
print(thisdict)

x = mySet.keys()

mySet["color"] = "red"
print(mySet)

mySet.pop("color")
print(mySet)

mySet.update({'color': "white"})
print(mySet)

values = mySet.values()
print(values)