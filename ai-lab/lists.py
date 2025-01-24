myList = [1,2,3,4,5,6,7,8,9,10]

myList.append(11)
print(f"append() method adds an element: {myList}")

myList2 = myList.copy()
print(f"copy() method return copy: {myList2}")

print(f"count() return no. of times a value has occured: {myList.count(10)}")

myNums = [56, 89, 23]
myNums.extend(myList)
print(f"extend() joins another iterable to list: {myNums}")

print(f"index() gives index of specified element: {myList.index(5)}")

myList.insert(2, 69)
print(f"insert() inserts elmnt at given pos: {myList}")

myList.pop(1)
print(f"pop() removes elmnt at specified pos: {myList.pop(1)}")

myList.remove(7)
print(f"remove() removes first item with specified value: {myList}")

myList.reverse()
print(f"reverse(): {myList}")

myList.sort()
print(f"sort() sorts list: {myList}")