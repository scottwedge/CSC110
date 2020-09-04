# Lab Activity - List and Functions
# CSC 110 - Section 03
# Justin Clark
# 3/5/2020

# function takes an array parameter, 
# and two index value parameters and swaps them
def swap(arr, index1, index2):
    
    # save the first value to a temporary location
    temp = arr[index1]

    # swap the first index value with the second index value
    arr[index1] = arr[index2]

    # swap the second index value with temp's value
    arr[index2] = temp


# function takes an array parameter and returns a 
# new array for all strings with a length of 2
def sift_two(arr):

    # variable to hold new array
    new_arr = []

    # loop through the original array
    for string in arr:

        # find strings with a length of 2
        if len(string) == 2:

            # add string with length of 2 to the new array
            new_arr.append(string)

    # return the new array
    return new_arr

def main():

    print('-'*50)
    #Function ONE
    stuff = [10, 20, 30, 40]
    print(stuff)
    swap(stuff, 0, 2)
    print(stuff)
    nums = [5, 8, 15, 12, 18]
    print(nums)
    swap(nums, 2, 3)
    print(nums)


    print('-'*50)
    # Function TWO
    stuff = ['this', 'is', 'a', 'list', 'of', 'strings', 'yo']
    print(stuff)
    others = sift_two(stuff)
    print(others)
    print(stuff)
    print(sift_two(['go', 'try', 'a', 'new', 'thing', 'and', 'just', 'do', 'it']))

main()