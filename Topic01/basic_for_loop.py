"""
Program: basic_for_loop.py
Author: Lily Ellison
Last date modified: 02/08/2023

The purpose of this program is to create a list of floating point numbers and use a for loop to print out each number.
It will also print the odd numbers from 99 to 33, inclusive, in descending order.

"""

birthdays = [5.31, 7.13, 10.19, 12.02, 12.1, 12.3]
for date in birthdays:
    print(date)

num_list = range(99, 32, -2)
for number in num_list:
    print(number)