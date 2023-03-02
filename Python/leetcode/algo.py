from collections import Counter


class Solution:

    def get_numbers_caracters(self, value: str):
        count = Counter(value)
        if count.get('0') and count.get('1'):
            return count.get('0'), count.get('1')
        elif count.get('0') and not count.get('1'):
            return count.get('0'), 0
        elif not count.get('0') and count.get('1'):
            return 0, count.get('1')

    def findMaxForm(self, strs: list, m: int, n: int) -> int:

        value_0, value_1 = 0, 0
        subsets = []
        for value in strs:
            num_0, num_1 = self.get_numbers_caracters(value)  # 1, 1
            value_0 = num_0
            value_1 = num_1
           
            print(num_0, num_1, end='--> \n')
           

            if num_0 < m and num_1 < n:
                print('--- condition 1----')
                subsets.append(value)
                num_0 = value_0 + num_0
                num_1 = value_1 + num_1
            elif num_0 < m and num_1 <= n:
                print('--- condition 2----')
                subsets.append(value)
                num_0 = value_0 + num_0
                num_1 = value_1 + num_1
            elif num_0 <= m and num_1 < n:
                print('--- condition 3----')
                subsets.append(value)
                num_0 = value_0 + num_0
                num_1 = value_1 + num_1
            elif num_0 == m and num_1 == n:
                print('--- condition 4----')
                subsets.append(value)
                num_0 = value_0 + num_0
                num_1 = value_1 + num_1

           

         

        return len(subsets)


if __name__ == '__main__':
    value = Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
    print(value)
    assert value == 4
#https://leetcode.com/problems/ones-and-zeroes/