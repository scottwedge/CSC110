# CSC 110 Lab 1
# Program to prompt the user for their name, then say hello to the user
# Section 03
# Justin Clark
# 1/7/2020


# input section
username = input('Please enter your name: ')

# input class
userClass = input('Please enter your class: ')

# input grade
userGrade = float(input('Please enter your grade: (e.g. 4.0) '))


# output greeting
print("Hello " + username + "-- Nice to meet you!")

# output message depending on grade entered
if userGrade < 2.0:
    print('You need to study a bit harder.')
elif userGrade > 3.5:
    print('You are doing great!')
else:
    print('You are doing alright')
