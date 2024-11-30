
# https://support.github.com/tickets/personal/0
"""
Date: 23 Nov 2024
Returns the array of elements containing the next greater element of each of the elements present in arr
"""
def next_greater_elements(arr):
    length = len(arr)
    result = [-1] * length
    # Using the Monotonically Decreasing Stack
    mono_decreasing_stack = []
    # By processing elements from right to left, we ensure that as we move through the array,
    # the stack contains only elements to the right of the current element.
    for i in range(length - 1, -1, -1):
        while mono_decreasing_stack and arr[i] >= mono_decreasing_stack[-1]:
            mono_decreasing_stack.pop()
        # If stack is not empty then the top is the next greater element
        if mono_decreasing_stack:
            result[i] = mono_decreasing_stack[-1]
        mono_decreasing_stack.append(arr[i])
    return result

"""
Returns the array of elements containing the next smaller element of each of the elements present in arr
"""
def next_smaller_elements(arr):
    length = len(arr)
    result = [-1] * length
    # Using the Monotonically Increasing Stack
    mono_increasing_stack = []
    # By processing elements from left to right, we ensure that as we move through the array,
    # the stack contains only elements to the left of the current element.
    for i in range(0, length):
        while mono_increasing_stack and arr[i] < mono_increasing_stack[-1]:
            mono_increasing_stack.pop()
        # If stack is not empty then the top is the next smaller element
        if mono_increasing_stack:
            result[i] = mono_increasing_stack[-1]
        mono_increasing_stack.append(arr[i])
    return result

if __name__ == '__main__':
    print(next_greater_elements([1, 2, 4, 5, 3]))
    print(next_smaller_elements([1, 2, 4, 5, 3]))
