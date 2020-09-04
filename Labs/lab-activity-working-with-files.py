# Lab Activity - Working with Files
# CSC 110 - Section 03
# Justin Clark
# 2/25/2020

# https://canvas.northseattle.edu/courses/1871665/assignments/16999870?module_item_id=38896093

# get file name from user
file_name = input('Enter a file name: ')

# open input file
input_file = open(file_name, 'r')

# open output files
even_file = open('even.txt', 'w')
odd_file = open('odd.txt', 'w')

# initialize accumulators
negative_count = 0
even_sum = 0

# read the first line in the file
line = input_file.readline().rstrip()

# loop through all the lines in the file
while line != '':

    # read the line in as an integer
    num = int(line)

    # process even numbers
    if (num == 0) or (num % 2 == 0):
        even_file.write(str(num)+'\n')
        even_sum += num
    # process odd numbers
    else:
        odd_file.write(str(num)+'\n')
    # process negative numbers
    if num < 0: negative_count += 1

    # set the next line to read for the loop
    line = input_file.readline().rstrip()

# print the results to the console
print(
    'sum of even numbers: '+str(even_sum)+'\n'+\
    'count of odd numbers: '+str(negative_count)
)

# close input file
input_file.close()

# close output files
even_file.close()
odd_file.close()