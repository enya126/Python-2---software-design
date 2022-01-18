#  File: Radix.py
#  Description: This program use python to do radix sort.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/07/2021
#  Date Last Modified: 04/07/2021

import sys

def radix_sort (a):
  # create a queue list
  queue_lst = []
  for i in range(38):
    queue_lst.append([])

  # get maximum length
  max_len = 0
  for str in a:
    if len(str) > max_len:
      max_len = len(str)

  # max_len = how many passes
  for i in range(1, max_len+1):
    for str in a:
      if len(str) == max_len:
        key = radix_sort_helper(str[-i])
      if len(str) == 1:
        add = max_len - len(str)
        if i <= add:
          key = radix_sort_helper('0')
        else:
          key = radix_sort_helper(str[-i+add])
      else:
        add = max_len - len(str)
        if i <= add:
          key = radix_sort_helper('#')
        else:
          key = radix_sort_helper(str[-i+add])
      queue_lst[key].append(str)
    a.clear()
    # dequeue
    for value in queue_lst:
      a.extend(value)
      value.clear()

  return a



# input should be a single str like 'f' or '2'
def radix_sort_helper(str):
  # mapping from a character to an index in the above list
  dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
          13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o',
          25: 'p', 26: 'q', 28: 'r', 29: 's', 30: 't', 31: 'u', 32: 'v', 33: 'w', 34: 'x', 35: 'y', 36: 'z', 37: '#'}
  # find idx from the dict
  for key, value in dict.items():
    if str == value:
      return key

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()