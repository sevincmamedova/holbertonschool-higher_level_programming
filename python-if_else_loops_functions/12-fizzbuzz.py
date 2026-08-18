#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100, with Fizz Buzz substitutions."""
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")
