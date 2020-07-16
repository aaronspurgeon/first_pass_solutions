'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# # Sliding Window Max

# Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

# ## Example
# ```
# Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Expected Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


def array_max(arr, start):
    result = None
    for i in arr:
        if result == None:
            result = i
        if i > result:
            result = i
    return result


# print(array_max([-1, -3, 5]))


def sliding_window_max(nums, k):
    max_arr = []
    # start = 0
    # end = len(nums) - 1
    start = 0
    end = start + k
    counter = 0
    new_arr = nums

    # a[start:stop]  # items start through stop-1

    while counter <= len(nums) - 1:
        if end == len(nums) + 1:
            break
        new_arr = nums
        new_arr = new_arr[start:end]
        append_max = array_max(new_arr, start)
        max_arr.append(append_max)
        # print(new_arr)
        end = end + 1
        start = start + 1
        counter = counter + 1

    return max_arr


print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 2))
if -1 > -3:
    print('yup')


# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(
#         f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
