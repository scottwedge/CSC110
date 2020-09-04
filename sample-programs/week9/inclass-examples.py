# Code developed in class on Monday, 3/3
# Introduces working with lists.
# Covers the basic loop and indexed loop.
# Enhanced a bit from what we did in class.

# CSC 110

nums = [5, 12, -2, 7]
colors = ['red', 'green', 'blue']

print(nums)
print(len(nums))
print(colors)
print(len(colors))

print()
chars = 0
for c in colors:
    chars += len(c)
    print('I like the color ' + c)
print('Total number of characters:', chars)
print()


# basic loop
# => Does ONE thing well: EXAMINE (but not change)
#    every value in the list from beginning to end.
total = 0
for num in nums:
    total += num
print('Sum of all the numbers:', total)

# indexed loop (a counting loop)
# => Use for all other purposes.
total = 0
for i in range(len(nums)):
    total += nums[i]
print('Sum of all the numbers:', total)


# Variations on the indexed loop:

# 1. Visit all elements in order
# 2. Change element values
print('\nIncrease each element value by 2:')
print(nums)
for i in range(len(nums)):
    nums[i] += 2
print(nums)
print()

# 3. Visit all elements in reverse order
for i in range(len(colors) -1, -1, -1):
    print(colors[i])
print()

# 4. Visit every other element starting with the first
for i in range(0, len(nums), 2):
    print('Element', i, 'has the value', nums[i])
print()


# some built-in functions that work with lists
print('sum:', sum(nums)) # list must contain only numbers
print('min:', min(nums)) # all items must be "comparable" to each other
print('min:', min(colors)) # all items must be "comparable" to each other
print('max:', max(nums)) # all items must be "comparable" to each other
print('max:', max(colors)) # all items must be "comparable" to each other