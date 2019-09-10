#!/usr/bin/env python3

# Helper class to make sure that the correct type of data is entered on input()
# If the incorrect type is entered, then continually ask again


def input_int(input_msg: str) -> int:
    num1 = 'text'
    while not isinstance(num1, int):
        try:
            num1 = int(input(input_msg))
        except ValueError:
            print("Whoops! You need to enter an integer")

    return num1
