
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    print(letter, end=', ')

original_string = 'abcdefghijklmnopqrstuvwxyz'

# reverse order of string (short way)
new_string = original_string[::-1]
print(new_string)

# reverse order of string (long way)
for i in range(len(original_string)-1,-1,-1):
    print(i, original_string[i])
    new_string += original_string[i]
print (new_string)

if type(new_string).isalpha:
    print("is alpha")

'a' in alphabet

numbers = [1,2,3,4,5,6,7,8]
5 in numbers