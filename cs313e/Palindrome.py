#  File: Palindrome.py
#  Description: This program uses python to find the smallest palindrome of a string.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 3/7/2021
#  Date Last Modified: 3/7/2021

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string


def smallest_palindrome(str):
    # if str is empty str
    if str == '':
        return 0
    # if str has a length of 1, directly return it
    elif len(str) == 1:
        return str
    # if str has a length of 2
    elif len(str) == 2:
        if str[0] == str[1]:
            return str
        else:
            return str[1] + str
    # if str length is greater or equal to 3, check palindrome
    else:
        for i in range(0, len(str) - 2):
            # if there's palindrome in the str
            if str[i] == str[i + 2]:
                mid = i + 1
                new_str = str[mid]
                if str[0] == str[2] and str[1] == str[3]:
                    mid = 2
                    new_str = str[mid]
                for j in range(1, len(str) - mid):
                    # find palindrome in the str
                    if str[mid - j] == str[mid + j] and mid - j >= 0:
                        new_str = str[mid - j] + new_str + str[mid + j]
                    if len(str) == len(new_str):
                        return new_str
                    # find the remainder of the str
                    elif len(str) >= len(new_str):
                        # if the remainder were at the beginning
                        if str.endswith(new_str):
                            res = str[:-(len(new_str))]
                            rev_res = res[::-1]
                            # add to the end of the str
                            new_str = res + new_str + rev_res
                            return new_str
                        # if the remainder were at the end
                        else:
                            idx = len(str) - 1 - mid - j
                            res = str[-idx:]
                            rev_res = res[::-1]
                            new_str = rev_res + new_str + res
                            return new_str
            elif i + 2 >= len(str) - 1:
                store_str = str[1:]
                rev_store = store_str[::-1]
                return rev_store + str

def main():
    # read the data
    # print the smallest palindromic string that can be made for each input
    for line in sys.stdin.readlines():
        if line != '':
            input_str = str(line.rstrip())
            result = smallest_palindrome(input_str)
            print(result)

if __name__ == "__main__":
  main()