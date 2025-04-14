#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04, 14, 2025
# This program  uses while loop in order to calculate sum.


def main():
    # Gets input
    number = input("Enter the number for how much loop will run")
    # Catches any errors and different value besides integer
    sum_number = 0
    loop_run = 0
    try:
        number = int(number)
        # While loop which calculates the sum of all numbers and demonstrates it
        while loop_run <= number:
            sum_number = sum_number + loop_run
            loop_run = loop_run + 1
            print(f"The sum of numbers till {number} is {sum_number}.")
    except ValueError:
        # This statement pops up when the value is wrong
        print("Enter positive and valid integer.")


if __name__ == "__main__":
    main()
