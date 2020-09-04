
# largest.py
#
# Creates a list filled with random numbers and then displays
# the average and largest value.
# Demonstrates the random.randint() function.

# CSC 110
# Fall 2011

import random

HIGH = 30
LOW = -20
COUNT = 10

def main():
    
    # get random values
    data = create_random_list(LOW, HIGH, COUNT)

    ave = get_average(data)
    largest = get_largest(data)
    largest2 = get_largest_alternate(data)

    print('List =', data)
    print('Average =', ave,)
    print('Largest =', largest, '-- confirmed:', largest2)

    data = create_random_list(0, 100, 50000)
    ave = get_average(data)
    print('Average of 50000 random numbers between 0 and 100 =', ave,)
    

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


# Return the average of the values in the list 'numbers'.
def get_average(numbers):
    total = 0  # initialize accumulator
    for value in numbers:
        total += value
    return float(total)/len(numbers) # float() needed in Python 2; not Python 3


# Return the largest value in the list 'numbers'.
# Assumes the list contains at least one element.
def get_largest(numbers):
    largest = numbers[0]  # Start by assuming the first element is the largest.

    # Now visit the rest of the list and find the largest.
    for idx in range(1, len(numbers)):
        # Test to see if we found a new larger number.
        if numbers[idx] > largest:
            largest = numbers[idx]
    return largest


# Another way to write the 'get_largest' function.  The code is very
# slightly less efficient, but also slightly simpler.
# Assumes the list contains at least one element.
def get_largest_alternate(numbers):
    largest = numbers[0]  # Start by assuming the first element is the largest.

    # This loop visits EVERY element in the list.  Visiting the first'
    # element again is unnecessary, but not harmful.
    for num in numbers:
        # Test to see if we found a new larger number.
        if num > largest:
            largest = num
    return largest


main()
