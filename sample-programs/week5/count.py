# count.py
#
# Program illustrates counting using both a for loop and a while loop.
# Counts beginning at 5 in steps of 2; stops BEFORE 15.

# CSC 110
# Fall 2011

for value in range(5, 15, 2):
    print(value)

print('\n')

number = 5
while number < 15:
    print(number)
    number += 2
