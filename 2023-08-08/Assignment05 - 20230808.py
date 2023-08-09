# Question 5
# Print a upside-down Right Triangle

print("Print a upside-down Right Triangle")

for i in range(1, 6):
    for j in reversed(range(i, 6)):
        print("*", end='')
    print()
