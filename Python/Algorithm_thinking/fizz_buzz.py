"""
    . Fizz Buzz is a game for two or more players

    . Take it in turns to count aloud from 1 to 100,but each time you
    are going to say a multiple of 3, replace it with the word 'fizz'

    . For multiple of 5, say 'buzz' and for numbers that are multiples of both 3 and 5, say
    'fizz, buzz'

    Note: The problem here was to care about other of execution of our algorihtm, and check some 
    number that we know which are divided by 5 and 3

"""
import re

from collections import Counter

for value in range(1, 101):
    if value % 5 == 0 and value % 3 == 0:
        print('fizz, buzz')
    elif value % 5 == 0:
        print('buzz')
    elif value % 3 == 0:
        print('fizz')


def to_camel_case(text:str):
    """Convert string to camel case https://www.codewars.com/kata/517abf86da9663f1d2000003/python"""
    words = re.split(r'[-_]', text)
    return words[0] + ''.join(word.capitalize() for word in words[1:])


def find_deleted_number(arr, mixed_arr):
    """ lost number algo: (https://www.codewars.com/kata/595aa94353e43a8746000120/train/python)"""
    return sum(arr) - sum(mixed_arr)


def duplicate_count(text:str):
    """Counting Duplicates: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python"""
    return sum(1 for count in Counter(text.lower()).values() if count >= 2)

def f(n,l):
    """[Code Golf] - ZeroFiller:  https://www.codewars.com/kata/6777397b65316bd17df0f678/train/python"""
    return n.ljust(l,'0') if type(n)==str else f'{n:0{l}d}'
    

    
