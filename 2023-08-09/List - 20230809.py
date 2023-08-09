# Create new List and add new element
from typing import Iterable

empty_list = []
print(empty_list)

empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
print(empty_list)
print('')

# List indexing and slicing
numbers = [1, 2, 3, 4, 5]

print(numbers[0])
print(numbers[2])

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print('')

# List loop
fruits = list(['apple', 'banana', 'orange'])

for fruit in fruits:
    print(fruit)

    if fruit == 'banana':
        print("Found element 'banana'. Ending loop.")
        break
print('')

# List Comprehension
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # ouput : [1, 4, 9, 16, 25]

# or

squares = [num ** 2 for num in range(1, 6)]  # Alt + Enter at the front '[' for reconstruction
print(squares)
print('')

# List method
list_to_sort = [5, 2, 2, 8, 4, 1]

list_to_sort.sort()
print(list_to_sort)

list_to_sort.reverse()
print(list_to_sort)

list_to_sort.remove(8)
print(list_to_sort)

list_length = len(list_to_sort)
print(list_length)

# 다차원 리스트

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for _row in matrix:
    for _element in _row:
        print(_element)


# 중첩된 리스트의 평탄화
def flatten_list(nested_list):
    flattened = []
    for sublist in nested_list:
        for item in sublist:
            flattened.append(item)
    return flattened


nested_matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

print(flatten_list(nested_matrix))
print('')

# 리스트 병합과 최대 최소값 찾기
list_1 = ["mango", "apple", "banna", "peach"]
list_2 = ["watermelon"]

list_3 = list_1 + list_2
print(list_3)
print('')

list_for_minmax = [1, 2, 3, 4, 5]

min_by_list_for_minmax = min(list_for_minmax)
max_by_list_for_minmax = max(list_for_minmax)

print(min_by_list_for_minmax)
print(max_by_list_for_minmax)
print('')

# Count List element
list_of_fruits = list(["apple", "banana", "orange", "banana", "kiwi"])

banana_count = list_of_fruits.count("banana")
kiwi_count = list_of_fruits.count("kiwi")
grape_count = list_of_fruits.count("grape")

print("Amount of banana: ", banana_count)
print("Amount of kiwi: ", kiwi_count)
print("Amount of grape: ", grape_count)
print('')

# Reverse list element using slicing
numbers_A = [1, 2, 3, 4, 5]
reversed_numbers = numbers_A[::-1]
print(reversed_numbers)  # Output : [5, 4, 3, 2, 1]

# Reverse list element using reverse() method
num_listA = [1, 2, 3, 4, 5]
num_listA.reverse()
print(num_listA)

# Reverse list element using reverse() function
num_listB = [1, 2, 3, 4, 5]
num_listB_reversed = reversed(num_listB)
print(num_listB_reversed)
for num_print in num_listB_reversed:
    print(f"{num_print} ", end='')
print('')

# Converting Iterable List num_listB to Iterator iter_num_listB_reversed
iter_num_listB_reversed = iter(num_listB_reversed)
print(f"Is num_listB_reversed able to be looped?", isinstance(num_listB_reversed, Iterable))
print(f"Is iter")

# Find specific index in List
fruits_list_A = ["apple", "banana", "orange", "kiwi"]
# Find index for "banana"
index_of_banana = fruits_list_A.index("banana")
print(f"Index of banana: {index_of_banana}")
print('')

for i, fruit in enumerate(fruits_list_A):
    print(i, fruit)
print('')

# Filtering according to condition of List's element
list_of_numbers = [10, 11, 21, 36, 49, 56, 60, 72, 81, 90]
even_numbers = []
odd_numbers = []
for number in list_of_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 != 0:
        odd_numbers.append(number)
print(f"{even_numbers}\n{odd_numbers}")
print('')

num_above_30 = []
for number in list_of_numbers:
    if number > 30:
        num_above_30.append(number)
print(num_above_30)

# Zip() & Unpack
fruit_ids = [1, 2, 3, 4, 5, 6]
fruit_nms = ["apple", "apple(rotten)", "banana", "orange", "banana", "kiwi"]
fruit_price = [2000, 1000, 3000, 4000, 3000, 5000]

zipped_fruits = zip(fruit_ids, fruit_nms, fruit_price)
convert_to_list_fruit = list(zipped_fruits)
print(convert_to_list_fruit)

# Sort()
list_for_sort_A = ["mango", "banana", "apple", "pineapple"]
list_for_sort_A.sort()
print(f"")