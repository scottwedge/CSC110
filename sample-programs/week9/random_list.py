
# random_list.py
#
# Menu driven program to display all of a list or subsets of it.

# CSC 110
# Fall 2011

import random

HIGH = 100
LOW = 2
COUNT = 15
 
def main():
    # get random values
    list = create_random_list(LOW, HIGH, COUNT)

    # get user choice and run their request (sentinel-controlled loop)
    userChoice = menu()
    while userChoice != 'q':
        if userChoice == 'a':
            display_all(list)
        elif userChoice == 'e':
            display_even(list)
        else:
            display_odd(list)
        # ask user again what they want to do
        userChoice = menu()

# Create and return a list of random integers.
# parameter lo, the lowest possible random integer
# parameter hi, the highest possible random integer
# parameter ct, the number of elements in the list
def create_random_list(lo, hi, ct):
    # create an empty list
    result = []
    for x in range(ct):
        result.append(random.randint(lo,hi))
    return result

# Prints a menu and then gets and returns user input.
# Returns either 'q', 'a', 'e', or 'o' for quit/all/even/odd.
def menu():
    print()
    print('a:   print all values')
    print('e:   print even values')
    print('o:   print odd values')
    print('q:   to quit')

    answer = input("please enter your choice: a/e/o/q ")
    answer = answer.lower()
    while answer != 'a' and answer != 'e' and answer != 'o' and answer != 'q':
        print("Invalid input. Please try again")
        answer = input("please enter your choice: a/e/o/q ")
        answer = answer.lower()
    return answer


# displays the entire contents of the list stuff
def display_all(stuff):
    for numb in stuff:
        print(numb)


# displays all the odd values in the list stuff
def display_odd(stuff):
    for numb in stuff:
        if numb % 2 != 0:
            print(numb)

# displays all the even values in the list stuff
def display_even(stuff):
    for numb in stuff:
        if numb % 2 == 0:
            print(numb)

main()
