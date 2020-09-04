# Code developed in class on Wednesday, 3/4.
# Demonstrates List Algorithms.
# Demonstrates a list accumulator.
#
# CSC 110


# Returns the sum of the numbers in the list arr.
# arr must contain only numbers
def sum2(arr):
    total = 0
    for x in arr:
        total += x
    return total


# Returns the average of the POSITIVE numbers in the list arr.
# Returns 0 if there are no positive numbers in the list.
# arr must contain only numbers
def average_pos(arr):
    count = 0
    total = 0
    for x in arr:
        if x > 0:
            count += 1
            total += x
    if count == 0:
        return 0
    return total / count


# Returns the highest value in the list arr.
# All values in arr must be comparable to each other.
# len(arr) must be >0
def get_highest(arr):
    highest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
    return highest


# CHANGES the list arr by increasing each number by 10.
def plus10(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] + 10  # arr[i] += 10


# Returns True if target is contained in the list arr,
# False otherwise.
def contains(arr, target):
    for x in arr:
        if x == target:
            return True
    return False


# Returns the INDEX of the FIRST occurrence of target
# in the list arr, or -1 if the target is not found.
def index_of(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Returns a NEW LIST containing all number in arr
# that are greater than or equal to threshold.
# arr must contain only numbers; threshold is a number
def get_large(arr, threshold):
    result = [] # initialize LIST ACCUMULATOR
    for x in arr:
        if x > threshold:
            result.append(x) # update LIST ACCUMULATOR
    return result


def main():
    nums = [5, 12, -2, 7]
    nums2 = [52, -35, 73]
    print(nums)
    print(sum(nums))
    print(sum2(nums))
    print(nums2)
    print(sum(nums2))
    print(sum2(nums2))
    print(average_pos(nums))
    print(get_highest(nums))
    print(get_highest(nums2))

    print(get_highest([0]))
    print(get_highest([]))
    
    print(nums)
    plus10(nums)
    print(nums)
    
    # test first, middle, last, not present
    print('Contains 15?', contains(nums, 15))
    print('Contains 22?', contains(nums, 22))
    print('Contains 17?', contains(nums, 17))
    print('Contains 5?', contains(nums, 5))
    
    # test first, middle, last, not present
    print('index_of 15?', index_of(nums, 15))
    print('index_of 22?', index_of(nums, 22))
    print('index_of 17?', index_of(nums, 17))
    
    # test all, some, none
    print('index_of 5?', index_of(nums, 5))
    print('values larger than 22:', get_large(nums, 22))
    print('values larger than 15:', get_large(nums, 15))
    print('values larger than 7:', get_large(nums, 7))

main()