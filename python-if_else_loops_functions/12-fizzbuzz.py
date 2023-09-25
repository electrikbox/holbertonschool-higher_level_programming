#!/usr/bin/python3

def fizzbuzz():
    sentence = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            sentence += "FizzBuzz "
        elif i % 3 == 0:
            sentence += "Fizz "
        elif i % 5 == 0:
            sentence += "Buzz "
        else:
            sentence += str(i) + " "

    print(sentence, end="")
