"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


input_string = input("Input?: ")
tokens = input_string.split(' ')
tokens[1] = int(tokens[1])
tokens[2] = int(tokens[2])


while True:
    if "pow" in tokens:
        print(power(tokens[1], tokens[2]))
    elif "q" in tokens:
        break
    elif "+" in tokens:
        print(add(tokens[1], tokens[2]))
    elif "-" in tokens:
        print(subtract(tokens[1], tokens[2]))
    elif "/" in tokens:
        print(divide(tokens[1], tokens[2]))
    elif "*" in tokens:
        print(multiply(tokens[1], tokens[2]))
    elif "square" in tokens:
        print(square(tokens[1]))
    elif "cube" in tokens:
        print(cube(tokens[1]))
    elif "mod" in tokens:
        print(mod(tokens[1]))

    break
