
# fill_list_with_words.py
#
# Creates an initially empty list and fills it with words
# entered by the user.  Illustrates a sentinel-controlled
# loop used to get the values from the user.

# CSC 110
# Fall 2011

user_strings = []  # create an EMPTY list

# get the first input from the user
word = input('Enter a string, or the word stop to finish: ')
word = word.lower()  # convert the word to all lower-case letters

while word != 'stop':
    user_strings.append(word)  # add a new element to the list
    # get another input
    word = input('Enter a string, or the word stop to finish: ')
    word = word.lower()

# After user input, display the entire list
print('\n\nHere are your entries')
for i in range(len(user_strings)):
    print('Index', i, '-->', user_strings[i])

print(user_strings)
