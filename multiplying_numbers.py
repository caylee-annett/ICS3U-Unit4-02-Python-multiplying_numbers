#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program multiplies integers from 1 to the user's input and uses loops


def main():
    # This function multiplies the numbers
    loop_counter = 0
    answer = 1

    # Input
    print("This program multiplies integers from 1 to what you enter.")
    number_as_string = input("Enter a positive integer: ")
    print("")

    # Process & Output
    try:
        number_as_integer = int(number_as_string)

        if number_as_integer > 0:
            while loop_counter < number_as_integer:
                loop_counter = loop_counter + 1
                answer = loop_counter * answer
            print("{0}! = {1}".format(number_as_integer, answer))
        elif number_as_integer == 0:
            print("0! = 1")
        else:
            print("{} is not a positive integer.".format(number_as_integer))
    except Exception:
        print("{} is not a valid input.".format(number_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
