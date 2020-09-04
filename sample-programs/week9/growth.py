
# growth.py
#
# Illustrates changing the values stored in a list.
# Notice that you must use a loop that varies an index so that 
# the index can be used to access each list element in sequence.

# CSC 110
# Fall 2011


values = [5, 8, 14, 22]

print('Original list =', values)

# visit each element, by index number
# increase each element value by 2
for idx in range(len(values)):
    values[idx]  += 2

print('Updated list =', values)  # Shows that the list has been changed.
