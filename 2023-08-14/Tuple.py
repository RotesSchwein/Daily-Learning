empty_tuple = ()    # empty_tuple: tuple = ()

single_tuple = (42, )
multiple_tuple = (1, 2, 3, 4, "hello", "world")

# Check Tuple length
print("Check Tuple length")
multiple_tuple_length = len(multiple_tuple)
print(multiple_tuple_length)
print()

# Slice Tuple
print("Slice Tuple")
print(multiple_tuple[0:3])
print()

# Tuple and Zip()
print("Tuple and Zip()")
car = ("Sedan", "Truck", "4X4")
price = (0.9, 1.5, 1.2)
quantity = (3, 1, 5)
zip_car_info = zip(car, price, quantity)
print(zip_car_info)
car_info_list = list(zip_car_info)
print(car_info_list)
