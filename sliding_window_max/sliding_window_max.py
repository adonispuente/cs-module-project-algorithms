'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # make an array, this array consist i + k - 1
    window = k
    new_arr = []
    counter = 0
    loop = len(nums) - k + 1
    # loop through nums with range

    for i in range(0, loop):
        item = -10
        counter = i
        for j in range(len(nums[i:window])):
            j = counter
            if nums[j] >= item:
                item = nums[j]
                counter += 1
            else:
                counter += 1

        window += 1
        new_arr.append(item)

    return new_arr

    # compare all the values inside this created array, and loop through them to see which is the biggest

    # return that item and insert it into another created array - return this array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
