# read_numbers.py
#
# Sample program to read numbers from a file, count them and sum them.
# Assumes each line in the file contains a valid number.

# CSC 110
# Winter 2012

# open the file 'numbers.txt' for reading
infile = open('numbers.txt', 'r')

total = 0  # initialization
count = 0  # initialization
line = infile.readline()  # read in first line (initialization)

# as long as 'line' isn't an empty string, 
# we haven't reached the end of the file
while line != '':
    value = float(line) # convert from string to number
    print(value)  
    total += value
    count += 1
    line = infile.readline() # this is the update -- read another line

infile.close() # close the connection to the file 

print('There were ' + str(count) + ' numbers, totaling ' + str(total))
