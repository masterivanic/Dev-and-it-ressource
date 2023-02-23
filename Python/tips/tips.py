
"""
    multi-dimensional list to a simple list using
    sum function. example:
    input : [[1,2] , [3 , 4] , [5,6]]
    output: [1, 2, 3, 4, 5, 6]
"""

tab = [[1,2] , [3 , 4] , [5,6]]
flat = sum(tab, [])
print(flat)