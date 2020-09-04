def show_cube_root(x):
    ans = x ** (1/3)
    if ans == 3:
        print('Yay 3!!')
    else:
        print('The cube root of ' + str(x) + ' is ' + format(ans, '.3f'))
print('Some cube roots...')
num = 26
while num <= 28:
    show_cube_root(num)
    num += 1
print('That\'s all!')