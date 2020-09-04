# # nested2.py
# #
# # Nested loop Example 2

# # CSC 110
# # Fall 2011

# #accumulators for the outer loop
# sumOuter = 0 

# for outer in [1, 2, 3, 4]:
#     print('Outer loop iteration', outer)
#     sumOuter += outer

#     sumInner = 0   # accumulator for this inner loop
#     # notice that the inner loop's repetitions is based on the value
#     # of the outer loop's control variable
#     for inner in range(1, outer + 1):
#         print('    Inner loop iteration', inner)
#         sumInner += inner

#     # after the inner loop finishes, display its sum
#     print('    Inner loop sum = ', sumInner)
#     print()

# #after the outer loop finishes, display its sum
# print('Outer loop sum = ', sumOuter)



# print(format('n','3.0f'),end='')
# for j in range(4):
#     print(format('n^'+j,'20.0f'),end='')
# print()
for n in range (1,21,1):
    print(format(n,'3.0f'),end='')
    for i in range(3,7,1):
        print(format(n**i,'20,.0f'), end='')
    print()