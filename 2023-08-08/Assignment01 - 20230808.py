# Question 1
# Use if loop and for loop

print("1부터 10까지의 짝수를 표시합니다")

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}")
    elif i % 2 != 0:
        continue
    i += 1
