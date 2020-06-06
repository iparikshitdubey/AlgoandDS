def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    temp_arr = arr
    while temp_arr:
        if temp_arr[-1] < 9:
            temp_arr[-1] += 1
            break
        else:
            temp_arr[-1] = 0
            if len(temp_arr) > 1:
                temp_arr = temp_arr[:-1]
            else:
                temp_arr = [1] + temp_arr
                break
    return temp_arr


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9, 9]
solution = [1, 0, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 7, 9]
solution = [9, 9, 8, 0]
test_case = [arr, solution]
test_function(test_case)