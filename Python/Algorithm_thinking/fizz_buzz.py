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
from functools import reduce
from operator import mul

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

def persistence(n, count=0):
    digits = [int(x) for x in str(n)]
    if len(digits) == 1:
        return count
    
    if len(digits) >= 2:
        n = reduce(mul, digits)
        count += 1
        return persistence(n, count=count)


def get_all_index_of_word(word:str, list_word:list[str]):
    ids, count = [], 0
    for idx, w in enumerate(list_word):
        if count <= 2:
            if word.__eq__(w):
                count = count + 1
                ids.append(idx)
    return {word:ids}

def find_secret_message(paragraph):
    """ Secret Message: https://www.codewars.com/kata/54808e45ab03a2c8330009fb/train/python"""
    import string
    punct_to_remove = string.punctuation.replace('-', '')
    paragraph:str = paragraph.translate(str.maketrans('', '', punct_to_remove)).lower()
    copy = paragraph.split().copy()
    result = list(map(lambda x: get_all_index_of_word(x, copy), copy))
    result = {key:value[1] for d in result for key, value in d.items() if len(value) >= 2}
    result = dict(sorted(result.items(), key=lambda item: item[1]))
    return " ".join(result.keys())

def find_secret_message(paragraph):
    """ refacto version of find_secret_message algorithm"""
    s = set()
    ret = []
    for w in (word.strip('.,:!?').lower() for word in paragraph.split()):
        if w in s and not w in ret:
            ret.append(w)
        else:
            s.add(w)
    return ' '.join(ret)

def solution(s):
    """Split Strings: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python"""
    if len(s) % 2 != 0:
        s += '_'
    
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    
    return result


def reverse_number(n):
    """https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python"""
    return -int(str(n).replace("-", "")[::-1]) if "-" in str(n) else int(str(n)[::-1])

def reverse_number(n):
    reverseInteger = 0
    rem = 0
    num = n
    if n < 0: n = abs(n)
    while n > 0:
        reverseInteger *= 10
        rem = n % 10
        n = (n - rem) // 10
        reverseInteger += rem
    return -reverseInteger if num < 0 else reverseInteger

def unique(struct):
    if isinstance(struct, str):
        struct = list(struct)
    return [struct[i] for i, _ in enumerate(struct) if i == len(struct) - 1 or struct[i] != struct[i+1]]

    
