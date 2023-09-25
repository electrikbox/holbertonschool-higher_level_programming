import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
sign = ""

if number < 0:
    sign = "-"

if last_digit > 5:
    sentence = "greater than 5"
elif last_digit == 0:
    sentence = "0"
else:
    sentence = "less than 6 and not 0"

print(f"Last digit of {number} is {sign}{last_digit} and is {sentence}")
