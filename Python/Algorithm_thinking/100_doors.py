"""
    We start with a hallway that has 100 doors, all of which are closed at the start. 
We will make 100 passes down the hallway in total. On the first pass, we will open every door, 
toggling its state from closed to open. On the second pass, we will only toggle the state 
of every other door (i.e. 2, 4, 6,…). On the third pass, we will toggle the state of every 
third door (i.e. 3, 6, 9,…). This will continue until the 100th pass, where only the 100th 
door is toggled.

    After all of this, we should end up with a very specific pattern of open and closed doors.

    So which doors will be open?

    door open True otherwise False
"""
numbs_doors = 100
doors = [False] * numbs_doors

"""
    -> step i = 0 yield go to iteration with setp 1, off course will open all doors, so first 
        condition completed
    -> step i = 1 yield to go iteration with step 2 by 2
    -> step i = 2 yield go to iteration with step 3 by 3
    etc...
    of course after a passage in front of a door, it cannot
    have the same state that why we make 'not door' (opposite)
"""
   
for i in range(0, numbs_doors):
    for j in range(i, numbs_doors, i+1):
        doors[j] = not doors[j]

# all state of door after operation
for index, door in enumerate(doors):
    print('door at position {0} is {1}'.format(index, door))

print("---------- open  doors are ------------------------------")
for index, door in enumerate(doors):
    if door:
        print('door at position {0} is {1}'.format(index, door))
