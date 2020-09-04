# for num2 in [1,2,3]:
#     print("Huskies!")
# for num1 in [1,2,3]:
#     print("Go!")

# for i in range(3):
#     print("Go")
# for j in range(3):
#     print("Huskies!")

# for i in range(3):
#     print("Go")
#     for j in range(i +1):
#         print("Huskies!")


# def mangle(x,y):
#     if x > y:
#         z = 8
#     else:
#         z = 6
#     print(z)
#     return z

# def tangle(c):
#     b = 0
#     j = 1
#     while j < c:
#         b += j
#         j *= 2
#     return b

# q = tangle(mangle(30,60))

# print(q)



# import random

# print(random.random())



# def test(a,b):
#     result = 2 * a + b
#     return result

# print(test(3,5))



def test(a,b):
    result = 2 * a + b
    return result == 12

print(test(3,5))