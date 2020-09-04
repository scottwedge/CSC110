# strings.py
#
# Program to illustrate the "string concatenation operator" (+)
# and the use of string variables.
#
# CSC 110
# 9/25/2011, updated 10/4/2016

str1 = input("Enter a string: ")
str2 = input("Enter a second string: ")

# create a 2 more strings
str3 = str1 + str2
str4 = "second string = " + str2

# display
print(str3)
print(str4)
print("Here is " + str1 + ". Notice there is no space added before the period.")

# This final statement illustrates the "repetition operator" (*).
print(str2 * 3)