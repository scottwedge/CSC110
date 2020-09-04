



some_file = open(file="files/somefile.txt", mode="w")



some_text = ''
for n in range (1,21,1):
    some_text += format(n,'3.0f')
    for i in range(3,7,1):
        some_text += format(n**i,'20,.0f')
    some_text += '\n'

some_file.write(some_text)

some_file.close()


# open file, followed by close file without writing anything will overwrite the file with nothing
