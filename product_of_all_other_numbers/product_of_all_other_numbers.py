'''
Input: a List of integers
Returns: a List of integers
'''
# Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index.

# For example, given
# ```
# [1, 7, 3, 4]
# ```
# your function should return
# ```
# [84, 12, 28, 21]
# ```
# by calculating
# ```
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]

from functools import reduce


def product_of_all_other_numbers(arr):
    # Your code here
    if len(arr) == 2:
        arr.reverse()
        return arr
    new_arr = []

    for i in range(len(arr)):
        # if arr[i] == arr[len(arr) - 1]:
        #     result = reduce((lambda x, y: x * y), spliced_arr)

        spliced_arr = list(filter(lambda x: x != arr[i], arr))
        # print(spliced_arr)
        result = reduce((lambda x, y: x * y), spliced_arr)
        # print(result)
        new_arr.append(result)
    # new_arr.reverse()
    return new_arr
    # return new_arr


print(product_of_all_other_numbers([7, 9, 1, 8, 6, 7, 8, 8, 7, 10]))


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
