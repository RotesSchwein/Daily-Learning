# Set
empty_Set = {}

set_1 = {6, 9}
set_2 = {"Hello", "World!"}

set_fruit_1 = {'apple', 'banana', 'orange', 'cherry'}
print(f"set_fruit_1 before addition : {set_fruit_1}")
set_fruit_1.add('mango')
print(f"set_fruit_1 after addition : {set_fruit_1}")
print()

# Update is available in Set
set_fruit_1.update(("strawberry", "watermelon"))
print(f"set_fruit_1 after update : {set_fruit_1}")

# Remove element of Set - If try to remove non-existing element, returns Error
set_fruit_2 = {"mango", "banana", "watermelon"}
"""set_fruit_2.remove("mangooooo")"""
set_fruit_2.remove("mango")
print(f"set_fruit_2 after remove : {set_fruit_2}")
print()

# Discard element of Set - If try to discard non-existing element, does not return Error
set_fruit_2.discard("bananana")
print(f"set_fruit_2 after discard : {set_fruit_2}")
print()