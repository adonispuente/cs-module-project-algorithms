'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # loop through the array
    # if item is 0, pop that index and append it to the end
    # return array + array[0]

    for i in range(len(arr)):
        if arr[i] == 0:
            item = arr.pop(i)
            arr.append(item)
            i = 0
            if i == 0:
                if arr[i] == 0:
                    item = arr.pop(i)
                    arr.append(item)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
