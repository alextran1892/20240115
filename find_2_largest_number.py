entry_number = input('Entry numbers: ')
numbers = []
for num in entry_number:
    numbers.append(int(num))
print(numbers)

numbers.sort()
print(numbers[-1])
print(numbers[-2])
