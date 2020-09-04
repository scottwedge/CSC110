
# first_list_example.py
#
# Illustrates two ways to iterate through a list (examine every
# element in a list).

# CSC 110
# Fall 2011

stuff = [7, 17, -4, 0.5]  # create a list filled with integers

print(stuff)  # prints in "list" form (with square brackets and commas)


# This loop visits every element of the list, by index number.
for index in range(len(stuff)):
    print('Index', index, 'has value', stuff[index])
print()


# This loop displays the squares of the values in the list
# and then then the sum of the squares.
# Since the algorithm doesn't need index numbers, we can just use the
# natural behavior of the 'for' loop to visit every element in the list.

sqSum = 0 # initialize accumulator
for value in stuff:
    sq =  value ** 2
    print('The number', value, 'squared =', sq)
    sqSum += sq
print('The sum of the squares =', sqSum)
