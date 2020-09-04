# Lab Activity - Working with Strings
# CSC 110 - Section 03
# Justin Clark
# 3/9/2020

line_separator = '\n'+'-'*50

string = input('Enter a short phrase: ')

#1
print(line_separator)
for ch in string:
    print(ch)

#2
print(line_separator)
print(string[::-1])

#3
print(line_separator)
for ch in range(len(string)-1,-1,-1):
    print(string[ch], end='')

#4
print(line_separator)
for ch in string:
    if ch == ' ': ch = '\n'
    print(ch, end='')

#5
print(line_separator)
input_file = open(input('Enter a file name: '), 'r')
output_file = open('output.txt', 'w')

text = ''
new_text = ''

vowels = ['a','e','i','o','u']

for line in input_file:
    text += line

for ch in text:
    if not ch.lower() in vowels:
        new_text += ch

for ch in new_text:
    if ch == ' ': ch = '\n'
    print(ch, end='')

input_file.close()

#6
print(line_separator)
string += ' '
new_string = ''
word = ''

for ch in string:
    word += ch
    if ch == ' ':
        if word[0] == 'b': new_string += 'bee '
        else: new_string += word
        word = ''

print(new_string)