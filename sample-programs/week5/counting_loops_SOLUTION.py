
# Solution for Part 2 of the Counting Loops lab exercise
# CSC 110, F'16

# The first four of these solutions follow exact patterns presented in class.
# The last two are variations on the same patterns.

# Use a 'while' loop to create this pattern: -3, -2, -1, 0, 1, 2, 3, 4
print("\n#1:")
count = -3
while count <= 4:
    print(count)
    count += 1

# Use a 'for' loop to create the same pattern: -3, -2, -1, 0, 1, 2, 3, 4
print("\n#2:")
for count in range(-3, 5):
    print(count)

# Use a 'while' loop to create this pattern: 20, 15, 10, 5, 0, -5, -10
print("\n#3:")
count = 20
while count >= -10:
    print(count)
    count -= 5

# Use a 'for' loop to create the same pattern: 20, 15, 10, 5, 0, -5, -10
print("\n#4:")
for count in range(20, -11, -5):
    print(count)

# Use a 'while' loop to create this pattern: 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36 
print("\n#5:")
count = -6
while count <= 6:
    print(count**2)
    count += 1

# Use a 'while' loop to create this pattern: 10, 20, 40, 80, 160, 320, 640 
print("\n#6:")
count = 0
while count <= 6:
    print(10 * 2**count)
    count += 1
