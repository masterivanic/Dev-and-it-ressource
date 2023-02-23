"""
    . Fizz Buzz is a game for two or more players

    . Take it in turns to count aloud from 1 to 100,but each time you
    are going to say a multiple of 3, replace it with the word 'fizz'

    . For multiple of 5, say 'buzz' and for numbers that are multiples of both 3 and 5, say
    'fizz, buzz'

    Note: The problem here was to care about other of execution of our algorihtm, and check some 
    number that we know which are divided by 5 and 3

"""

for value in range(1, 101):
    if value % 5 == 0 and value % 3 == 0:
        print('fizz, buzz')
    elif value % 5 == 0:
        print('buzz')
    elif value % 3 == 0:
        print('fizz')
    

    