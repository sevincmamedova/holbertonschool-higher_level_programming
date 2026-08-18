#!/usr/bin/python3
for tens in range(0, 9):
    for units in range(tens + 1, 10):
        print("{:d}{:d}".format(tens, units),
              end=", " if tens * 10 + units < 89 else "\n")
