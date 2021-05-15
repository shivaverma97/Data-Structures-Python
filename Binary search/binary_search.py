def linear_search(search_list, num_to_find):
    for index, element in enumerate(search_list):
        if  element == num_to_find:
            return index
    return -1

def binary_search_recursive(search_list, num_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index+right_index)//2
    if mid_index >= len(search_list) or mid_index < 0 :
        return -1
    mid_number = search_list[mid_index]

    if mid_number == num_to_find:
        return mid_index
    if mid_number > num_to_find:
        right_index = mid_index - 1
    if mid_number < num_to_find:
        left_index = mid_index + 1

    return binary_search_recursive(search_list, num_to_find, left_index, right_index )



numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
number_to_find = 21

index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
print(f"Number found at index {index} using binary search")