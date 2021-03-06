
# My approach, Failed in all of them except one

# def is_list(input):
#     return isinstance(input,list)
#
# def deep_reverse(arr):
#     if len(arr) <= 1:
#         return arr
#     first = arr[0]
#     if is_list(first):
#         first = deep_reverse(first)
#     returned_list = deep_reverse(arr[1:])
#     if is_list(first):
#         for elem in first:
#             returned_list.append(elem)
#     else:
#         returned_list.append(first)
#     return returned_list


'''
Udacity solution
'''


def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)


def deep_reverse(arr):
    """
    Function to deep_reverse an input list
    """
    return deep_reverse_func(arr, 0)


def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    """
    # Base Case
    if index >= len(arr):
        return list()

    output = deep_reverse_func(arr, index + 1)

    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]

    output.append(to_append)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)


