'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # return the integer in the list that doesn't have a duplicate
    # an optimized solution here would be to use a hashmap but idk how to do that
    # i can try a brute force way by looping through the array to create a list of 1 of each
    # then loop through the array again but this time make a nested for loop of the list i created and keep count of each time
    my_dict = {}
    for i in arr:
        if len(my_dict) == 0:
            my_dict[i] = 1
        elif i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for i in my_dict:
        if my_dict[i] == 1:
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
