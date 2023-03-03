"""
 Way to resolve an complex algorithm is decrease and conquer
 Classic example of Decrease and Conquer:
 --> Binary search
 --> Euclid's algorithm
 --> Depth-first search
 --> Breadth-first search
 --> Inserion sort and selection sort

Application of Depth-first search:
    + Optimization of criteria (cost, speed, etc.)
    + Pathfinding
    + Scheduling algorithm
    + Assessing investment decision trees
    + Ordering of formula cell evaluation in spreedsheets
    + Determining the order of compilation tasks of software builds
    + Data serialization
    + Resolving symbol dependicies 
 
Application of Breadth-first search:
    Breadth-first search used Queue as data structure
    which basic functionnality is ta search a path from
    a start postion to the ended position by discovering neighboor
    enqueue and dequeue each of them until will reach the ended position.

    + GPS System
    + Flight system reservation
    + Finding neighboor nodes in peer-to-peer network
    + Social network sites to find connections between users
    + Web crawlers
    + Many applications in IA
    + Electronics and communication engineering
    + scientific modeling

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
