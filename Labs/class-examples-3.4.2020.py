
def sum2(arr):
    # returns the sum of all the numbers in the list arr
    # arr must contain only numbers
    total = 0
    for x in arr:
        total += x
    return total



def average_positive(arr):
    # returns the average of all the positive nubers in the arr
    # returns 0 if the list contain no positive numbers
    # arr must cantain only numbers

    count = 0
    total = 0

    for x in arr:
        if x > 0:
            count += 1
            total += x
    if count == 0:
        return 0
    return total / count


def get_highest(arr):
    # returns the highest value in the list arr.
    #  all values in arr must be comparable to each other
    #  len(arr) must be >0
    highest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]

    return highest

def get_lowest(arr):
    # returns the highest value in the list arr.
    #  all values in arr must be comparable to each other
    #  len(arr) must be >0
    lowest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]

    return lowest


# changes the list arr to increase each numbger by 10
# arr must contain only numbers
def plus10(arr):
    for i in range(len(arr)):
        arr[i] += 10
    
def contains(arr, target):
    # returns True if the list arr contains the value target, False otherwise.
    for x in arr:
        if x == target:
            return True
    return False

# returns the index of the first occurrence of target in the list arr,
#  or -1 if the target is not found.
def index_of(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# returns a new list containing all the value in arr that are greater than
# threshold.
def get_larger(arr, threshold):
    result = []
    for x in arr:
        if x > threshold:
            result.append(x)
    return result

def main():


    nums = [5, 12, -2, 7]

    print(nums)
    print(sum(nums))
    print(sum2(nums))

    print(average_positive(nums))
    print(average_positive([]))

    print(get_lowest(nums))
    print(get_highest(nums))

    nums2 = [99,52,1,0,41,15,74]
    print(get_highest(nums2))
    print(get_highest([]))

    chars = ['abc','lmn','tuv','xyz']

    print(get_highest(chars))
    print(get_lowest(chars))

    print(nums)
    plus10(nums)
    print(nums)

    print('contatins 15:',contains(nums, 15))
    print('contatins 22:',contains(nums, 22))
    print('contatins 17:',contains(nums, 17))
    print('contatins 5:',contains(nums, 5))

    print('index_of 15:',index_of(nums, 15))
    print('index_of 22:',index_of(nums, 22))
    print('index_of 17:',index_of(nums, 17))
    print('index_of 5:',index_of(nums, 5))

    print('larger than 22: ',get_larger(nums, 22))
    print('larger than 15: ',get_larger(nums, 15))
    print('larger than 7: ',get_larger(nums, 7))
main()