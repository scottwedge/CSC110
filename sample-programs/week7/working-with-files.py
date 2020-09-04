# Code developed in class on Monday, 2/24
# Demonstrates working with files
#
# Each section of the program demonstrates
# the OPEN-PROCESS-CLOSE pattern.
#
# CSC 110

# NOTE: YOU WILL NEED TO CREATE YOUR OWN DATA FILES.

# reading in string data
infile = open('data.txt', 'r')

line = infile.readline()  # priming read (initialization)
while line != '':
    line = line.rstrip()  # remove trailing newline
    print(line)
    line = infile.readline()  # UPDATE read

infile.close()


# reading in numbers
# NOTE: Assumes nums.txt contains one integer value per line.
infile = open('nums.txt', 'r')

count = 0 # init counter
total = 0 # init accumulator
line = infile.readline()  # priming read (initialization)
while line != '':
    num = int(line)  # extract a number from the line
    total += num # update accumulator
    count += 1 # update counter
    line = infile.readline()  # UPDATE read

print('\nThe ' + str(count) + ' numbers in the file total ' \
      + str(total) + '.')
infile.close()


# writing data out to a file
outfile = open('result.txt', 'w')

for i in range(1, 11):
    # write requires a single string argumens; add '\n' if needed
    outfile.write(str(i) + '\n') 

outfile.close()


# Working with multiple files at the same time...
# Read each number from the input file.  If the number
# is greater than zero, write out a number to the plus5.txt
# file that is 5 greater than the number read in.  If
# the absolute value of the number is less than 50,
# write out to the squares.txt file the square of the number.
infile = open('nums.txt', 'r') # input file
plus5file = open('plus5.txt', 'w') # first output file
sqfile = open('squares.txt', 'w') # second output file

line = infile.readline()  # priming read (initialization)
while line != '':
    num = int(line)  # extract a number from the line
    if num > 0:
        plus5file.write(str(num+5) + '\n')
    if abs(num) < 50:
        sqfile.write(str(num**2) + '\n')
    line = infile.readline()  # UPDATE read

infile.close()
plus5file.close()
sqfile.close()


# checking the results in squares.txt
infile = open('squares.txt', 'r')

print()
line = infile.readline()  # priming read (initialization)
while line != '':
    line = line.rstrip()  # remove trailing newline
    print(line)
    line = infile.readline()  # UPDATE read

infile.close()