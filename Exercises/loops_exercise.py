# Prints the numbers 1 through 9 (WHILE LOOP)

num = 1
while num < 10:
    print(num)
    num = num + 1

# Prints the numbers 1 through 9 (FOR-IN LOOP)
for num in range(1, 10):
    print(num)

# Prints a list of names
for name in ["Annie", "Boris", "Chris"]:
    print(name)


# Work through these exercises:

# Write a program to print all the numbers from 2321 to 34325 inclusive.
for numbers in range(2321, 34325):
    print(numbers)
# Write a program to sum all of the even numbers in that range.
total = 0
for even_numbers in range(2321, 34325 + 1):
    if even_numbers % 2 == 0:
        total = total + even_numbers

print(total)

# Challenge:

# Write a program to find the factorial of 17.
# The factorial of a number is that number multiplied by every number below it until 1. So, 10 factorial is 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1, evaluating to 3628800.
# When correct, your program should produce the number 355687428096000.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(17)
print(result)


