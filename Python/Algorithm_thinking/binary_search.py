"""
 Way to resolve an complex algorithm is decrease and conquer
 Classic example of Decrease and Conquer:
 --> Binary search
 --> Euclid's algorithm
 --> Depth-first search
 --> Breadth-first search
 --> Inserion sort and selection sort
 
"""
import random


def binary_search(data, target_value):
    low_index = 0
    high_index = len(data) - 1
    while low_index < high_index:
        mid = (low_index + high_index) // 2
        if data[mid] == target_value:
            return mid
        elif data[mid] < target_value:
            low_index = mid + 1
        else:
            high_index = mid - 1
    return -1


n = 10
max_value = 100
nums = [random.randint(0, max_value) for _ in range(n)]
print("list: ", nums)
nums.sort()
print("Sorted list: ", nums)
target = int(input("Enter a target position:"))
target_pos = binary_search(data=nums, target_value=target)
if target_pos == -1:
    print("target position not found in the list")
else:
    print("you target value found", target_pos)
