# List
tempList_1 = ['a', 'b', 'c', 'd', 'e']
print(f"This is tempList_1 : {tempList_1}")
print('')

# 문자열 list
tempText = "Hello, World!"
print(f"This is List<String> tempText : ")
for txt in tempText:
    print(txt, end='')
print('')

# Tulple
tempTuple = ("246", "357")
print(tempTuple)
print('')

# List append, insert
tempList_2 = ['a', 'b', 'c', 'd', 'e']
print(f"thisList_2 (f 요소 추가 전) : {tempList_2}")
tempList_2.append('f')
print(f"thisList_2 (f 요소 추가 후) : {tempList_2}")
tempList_2.insert(1, 5)
print(f"thisList_2 (인덱스 1자리에 요소 5를 추가 후) -- {tempList_2}")
print('')

# List del, remove, pop
# delete element in said index
del tempList_2[2]
print(f"del element of index no.2 in tempList_2 : {tempList_2}")
print('')

# remove() element that is 'c'
tempList_1.remove('c')
print(f"remove() element 'c' in tempList_2 : {tempList_2}")
print('')

# pop() element in said index and save to a varialbe
removedElement = tempList_2.pop(4)
print(f"pop() element in said index in tempList_2 : {tempList_2}")
print(f"Element that has been popped via pop() : {removedElement}")
print('')

# List slicing => data[start:stop:step]
sliceList = ["a", "b", "c", "d", "e", "f", "g"]

print(sliceList[1:6:2])  # start from index 1 and ends at index 6 in interval of 2
print(sliceList[::-1])  # slice it in reverse
print(sliceList[::-2])  # slice it in reverse in interval of 2
print('')

# Shallow Copy
copyList_1 = ["a", "b", "c", "d", "e", "f", "g"]
copyList_2 = copyList_1

print(f"Original copList_1 : {copyList_1}")
print(f"Original copList_2 : {copyList_2}")
print('')

copyList_2[0] = "Hello"

print(f"After copList_1 : {copyList_1}")
print(f"After copList_2 : {copyList_2}")
print('')

# Deep Copy
# using copy() method
data_A = [1, 2, 3, 4, 5]
data_B = data_A.copy()  # Or data_B = list(data_A)

print(f"Original data_A : {data_A}")
print(f"Original data_B : {data_B}")
print('')

data_B[0] = 10

print(f"After altering data what data_A looks like : {data_A}")
print(f"After altering data what data_B looks like : {data_B}")
print('')

# using deepcopy() method
import copy

data_D = [1, 2, 3, 5, 6]
data_E = copy.deepcopy(data_D)