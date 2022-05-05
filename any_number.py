#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The area and perimeter calculator


def main():
    # this program shows the sum of all numbers from 0 to number
    counter = 0
    sum = 0

    # input
    number = input("Enter number (integer): ")

    # process & output
    try:
        number_int = int(number)
        while counter < number_int:
            sum = sum + (counter + 1)
            counter = counter + 1
        print("The sum of all numbers to {0} is {1}".format(number_int, sum))

    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
