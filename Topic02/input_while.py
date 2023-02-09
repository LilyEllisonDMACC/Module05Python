"""
Program: input_while.py
Author: Lily Ellison
Last date modified: 02/08/2023

The purpose of this program is to prompt user for input of a number between 1 and 100 until valid input is received.
All input will be stored in a list that will print once valid input received.

"""
ask_again = True
response_list = []

while ask_again:
    user_answer = input("Enter a number from 1 to 100: ")
    try:
        int(user_answer)
        if int(user_answer) in range(1, 100):
            ask_again = False
        else:
            response_list.append(user_answer)
    except:
        print("Not a whole number. Try again.")
        response_list.append(user_answer)
for entry in response_list:
    print(entry)

"""
Test results:

Enter a number from 1 to 100: okay
Not a whole number. Try again.
Enter a number from 1 to 100: 3.14
Not a whole number. Try again.
Enter a number from 1 to 100: pi
Not a whole number. Try again.
Enter a number from 1 to 100: fifty
Not a whole number. Try again.
Enter a number from 1 to 100: -9
Enter a number from 1 to 100: 0
Enter a number from 1 to 100: blah
Not a whole number. Try again.
Enter a number from 1 to 100: yay!
Not a whole number. Try again.
Enter a number from 1 to 100: !@#$
Not a whole number. Try again.
Enter a number from 1 to 100: 27
['okay', '3.14', 'pi', 'fifty', '-9', '0', 'blah', 'yay!', '!@#$']

Process finished with exit code 0

"""