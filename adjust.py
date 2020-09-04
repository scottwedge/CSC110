def adjust(entry):
    if entry > 5:
        num = entry / 2
    else:
        num = entry * 3
    if num > 30:
        num = 30
    return num + 1
x = 4
while x < 15:
    y = adjust(x + 3)
    print(y - 4)
    x = x + 5
print('Bye!')