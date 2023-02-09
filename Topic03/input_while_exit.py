"""
Program: input_while_exit.py
Author: Lily Ellison
Last date modified: 02/09/2023

The purpose of this program is to prompt user for input of a number between 1 and 100 until valid input is received or
a sentinel flag is used for the input.
All input will be stored in a list that will print once valid input received.

"""
ask_again = True
response_list = []
sent_flag = 0

while ask_again:
    user_answer = input("Enter a number from 1 to 100 (To quit, enter \'0\'): ")
    try:
        int(user_answer)
        if int(user_answer) == 0:
            break
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
1st Test -
Enter a number from 1 to 100 (To quit, enter '0'): okay
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): 3.14
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): pi
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): fifty
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): -9
Enter a number from 1 to 100 (To quit, enter '0'): 0
okay
3.14
pi
fifty
-9
2nd Test - 
Enter a number from 1 to 100 (To quit, enter '0'): blah
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): -875
Enter a number from 1 to 100 (To quit, enter '0'): 12346
Enter a number from 1 to 100 (To quit, enter '0'): 8.45
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): asodib
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): ekekeke
Not a whole number. Try again.
Enter a number from 1 to 100 (To quit, enter '0'): 45
blah
-875
12346
8.45
asodib
ekekeke

Process finished with exit code 0


Process finished with exit code 0

"""