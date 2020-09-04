# string_accumulator.py
#
# This short program demonstrates the use
# of a STRING ACCUMULATOR named 'result'.

# CSC 110
# Winter 2018

colors = ['red', 'green', 'blue', 'purple']

result = 'The artist said...' # INITIALIZATION
for word in colors:
    result += '\nI like the color ' + word + '!' # UPDATE

result += '\n\nWhat a colorful world!' # FINALIZATION (optional)

print(result)
