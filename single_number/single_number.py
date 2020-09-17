'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    new_arr = []
    # loop through the array
    # i need to compare the index im on, with all the other indexes
    # if none of the other indexes values is equal to the current index, return that index
    # while i is not len(arr):
    for i in range(len(arr)):
        if i < len(arr):
            if arr[i] not in new_arr:
                new_arr.append(arr[i])
                arr.pop(i)

    for item in new_arr:
        if item not in arr:
            needed_value = item
    return needed_value


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
