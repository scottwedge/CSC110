# count_lines.py
#
# program to read lines from a file and count those that are not empty

# CSC 110
# Winter 2012

count = 0       # total number of lines in the file
line_count = 0  # number of non-empty lines in the file

# open the file 'words.txt' for reading
infile = open('words.txt','r')

# read in the first line ("priming read")
line = infile.readline()

# as long as 'line' isn't an empty string, 
# we haven't reached the end of the file
while line != '':
    count += 1
    # each line read in ends with a "newline" character, 
    # so 'line' is at least 1 character long
    # if 'line' is MORE THAN one character long, the line is non-empty
    if len(line) > 1:
        line_count += 1

    # this is the update -- read another line
    line = infile.readline()

infile.close()  # close the connection to the file

print('This file has ' + str(line_count) + ' non-empty lines ' \
      + 'out of a total of ' + str(count) + ' lines.')

