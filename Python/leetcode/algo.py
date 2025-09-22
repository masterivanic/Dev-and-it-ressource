from collections import Counter

"""
Task
The function is given a string with lower-case characters. Split the string into as many substrings as possible such that each character appears in only one substring. 
Return the list of lengths of the resulting substrings.

Examples
"abbccc" ➞ [1, 2, 3]
# "a", "bb", "ccc"

"abbacdceef" ➞ [4, 3, 2, 1]
# "abba", "cdc", "ee", "f"

"abacded" ➞ [3, 1, 3]
# "aba", "c", "ded"

"abcdea" ➞ [6]
# "abcdea" because first letter is equal to the last letter.
"""

def is_exclusive_tuple(t):
    sets = [set(s) for s in t]
    char_counts = {}
    for s in sets:
        for ch in s:
            char_counts[ch] = char_counts.get(ch, 0) + 1
    return all(count == 1 for count in char_counts.values())

def all_partitions(st):
    substring = []
    for i in range(len(st)):
        for j in range(i+1, len(st)+1):
            substring.append(st[i:j])
    return substring

def all_partitions(s):
    n = len(s)
    for mask in range(1 << (n-1)):
        parts = []
        start = 0
        for i in range(n-1):
            if mask & (1 << i):
                parts.append(s[start:i+1])
                start = i+1
        parts.append(s[start:])
        yield tuple(parts)

def split_string(st):
    last_index = {ch: i for i, ch in enumerate(st)}
    result = []
    start = end = 0
    
    for i, ch in enumerate(st):
        end = max(end, last_index[ch])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result


class Solution:

    """
      write a code who take a sentence such as 'Hello world!'
      and print in ouput 
      Hello
      world
      !
    """
    def format_word(sentence: str) -> str:
        if sentence is not None:
            return ''.join(word + "\n" for word in sentence.split(' '))

    """
        You are given an array of binary strings strs and two integers m and n.
        Return the size of the largest subset of strs such that there are at 
        most m 0's and n 1's in the subset.
        A set x is a subset of a set y if all elements of x are also elements of y.

        Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
        Output: 4
        Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
        Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
        {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
    """
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        count = [[s.count("0"), s.count("1")] for s in strs]
   
        def deap_algo(m, n, sts):
            if m < 0 and n < 0:
               return -1
            elif sts == len(strs):
                return 0
            num_0, num_1 = count[sts]
            return max(1+ deap_algo(m-num_0, n-num_1, sts+1), deap_algo(m,n, sts+1))

        return deap_algo(m, n, 0)


if __name__ == '__main__':
    value = Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
    value1 = Solution().findMaxForm(["10","0","1"], 1, 1)
    assert value == 4
    assert value1 == 2

