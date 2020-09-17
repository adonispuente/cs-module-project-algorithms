'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # create new array , make it equal to the number of indexes in the given arr
    arr_length = len(arr)
    new_arr = [0] * arr_length
    # make a counter
    counter = 0

    # loop through with range
    for i in range(len(arr)):
        item = 1
        for j in range(len(arr)):
            if j != i:
                item = item * arr[j]

        new_arr[counter] = item
        counter += 1

    return new_arr

    # for loop, start at the index infront of current index a

    # multiply all the numbers your coming across in the second for loop
    # return that number and insert it into the created array at index of counter
    # increase counter + 1
    # at current index,


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
