"""
File: hailstone_extensions.py
Name: Angel Chen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Firstly, insert a number to the program.
    Secondly, the program will identify whether this number is odd or even.
    Then, this program computes Hailstone sequences
    The program stops until the number is one.
    """

    while True:  # Handling Exceptions
        try:
            print('【This program computes Hailstone sequences.】 \n')
            num = int(input('Enter a positive number:  '))
            # asks the user for input until a valid integer has been entered.
            break
        except (ValueError, RuntimeError, TypeError, NameError):
            # if the user doesn't input a integer, it will reminds user to input correctly.
            print("Oops! That was not a valid number.  Try again...\n")

    if num == 1:   # when user input 1, the program stops.
        print("\nIt took 0 step to reach 1.")
    else:
        x = 1  # calculate the number of steps, and the starting value is one.
        while True:
            if num % 2 == 1:   # means this number is odd
                answer = 3*num+1
                print(str(num) + ' is odd, so I make 3n+1: ' + str(answer))
                num = answer   # reassign the number
                if num == 1:
                    break
                x += 1   # add one more step
            else:   # means this number is even
                answer = num//2  # do not need float
                print(str(num) + ' is even, so I take half: ' + str(answer))
                num = answer   # reassign the number
                if num == 1:
                    break
                x += 1   # add one more step

        print("\nIt took " + str(x)+" steps to reach 1.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
