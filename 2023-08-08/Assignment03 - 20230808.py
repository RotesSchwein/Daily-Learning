# Question 3
# The space between the numbers should be applied with '\t'

print("구구단을 작성해보자")

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j}', end='\t')
    print()
