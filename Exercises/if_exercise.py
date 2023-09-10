import random

random_number = random.randint(1, 5)

# Print "One" if `random_number` is 1
if random_number == 1:
    print("One")
# Print "Two" if `random_number` is 2
elif random_number == 2:
    print("Two")
# Print "More" if `random_number is above 2
elif random_number > 2:
    print("More")

# Challenge 2
import time

seconds = int(time.time())

# Print "Fizz" if `seconds` is divisible by 3
if seconds % 3 == 0:
    print("Fizz")
# Print "Buzz" if `seconds` is divisible by 5
elif seconds % 5 == 0:
    print("Buzz")
# Print "FizzBuzz" if `seconds` is divisible by 3 and 5
elif seconds % 3 == 0 and seconds % 5 == 0:
    print("FizzBuzz")
# Otherwise, print `seconds`
else:
    print("seconds")