"""
Program: debugging.py
Author: Lily Ellison
Last date modified: 02/09/2023

The purpose of this program is to debug some code using PyCharm debugger.
Program should print all numbers starting from 1 to the number passed to it when main called the function.

"""
def print_to_number(number):
    """Prints to the number value passed in, beginning at 1"""
    for counter in range(1, number+1):
        print (counter)

if __name__ == "__main__":
    print_to_number(5)

    '''
    Fixed by increasing the range to check for to the input number plus one.
    The range is checked before the number is printed out, so it stops once it sees it has reached 5 without printing 5.
    '''