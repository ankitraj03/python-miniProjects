#sum of individual digit to power no of the digits should be equal to original no
num = input("Enter a number: ")

size = len(num)

total = 0

for digit in num:
    total += int(digit) ** size

if total == int(num):
    print("Yes, it is an Armstrong number.")
else:
    print("No, it is not an Armstrong number.")
