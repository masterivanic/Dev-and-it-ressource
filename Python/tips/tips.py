
"""
    multi-dimensional list to a simple list using
    sum function. example:
    input : [[1,2] , [3 , 4] , [5,6]]
    output: [1, 2, 3, 4, 5, 6]
"""

tab = [[1, 2], [3, 4], [5, 6]]
flat = sum(tab, [])
print(flat)

"""
   to fusion 2 dictionnaries in one
   input: {'maths':0, 'science':10}, {'sport':8, 'algorithm':19}
   ouput: {'maths': 0, 'science': 10, 'sport': 8, 'algorithm': 19}
"""
first_dict = {'maths': 0, 'science': 10}
second_dict = {'sport': 8, 'algorithm': 19}
final_dict = {**first_dict, **second_dict}
print(final_dict)

