#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    operators = "+-*/"

    if num_arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(arguments[0])
    operator = arguments[1]
    b = int(arguments[2])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operator_functions = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }

    if operator in operator_functions:
        func = operator_functions[operator]
        result = func(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
