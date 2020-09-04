

file = input ('Please enter a file\'s name: ')
infile = open(file, 'r')

startinglist = list()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print('The following are the words inside file without vowels')
startinglist = file.split(' ')
for word in startinglist:
  print(word)
  string = ''
  for consonant in word:
    if(consonant not in vowels):
      string += consonant
  print (string)

infile.close()