numbers = []

for ele in range(3):
    num = int(input("Enter number: "))
    numbers.append(num)

i = 0
while i < len(numbers) - 1:
    if numbers[i] < numbers[i + 1]:
        numbers.remove(numbers[i])
    else:
        i += 1

print(numbers)