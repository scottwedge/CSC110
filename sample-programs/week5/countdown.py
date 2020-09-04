# countdown.py
#
# counts down from larger input value to smaller

# CSC 110
# Fall 2011

first = int(input('Enter a number: '))
second = int(input('Enter another number: '))

# figure out which is larger. That's where we start.
if first <= second:
    start = second
    stop = first
else:
    start = first
    stop = second

print('\n')
# we use (stop-1) as the "stop before" value so that stop gets displayed
for val in range(start, stop-1, -1):
    print(val)

print("BLAST OFF")
