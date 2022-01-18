#  File: Reducible.py
#  Description: This program use python to find reducible words.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/02/2021
#  Date Last Modified: 04/04/2021

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
# This is hash1 that decide the original key
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
# This is hash2 that moves the str when there is a collision
def step_size (s, const):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % const
    stepSize = const - (hash_idx % const)
    return stepSize

# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    if (hash_table[idx] != ""):
        newPos = step_size(s, 13)
        # while the spot is not empty we will continue to increment our algorithm until we find a new spot for the word
        i = 1
        while (hash_table[(idx + newPos * i) % len(hash_table)] != ""):
            i += 1
        # once we find a spot that is empty, we will assign the word to that spot
        hash_table[(idx + newPos * i) % len(hash_table)] = s
    # if the initial spot is empty, we will place the word in that spot
    else:
        hash_table[idx] = s





# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word (s, hash_table):
    idx = hash_word(s,len(hash_table))
    if hash_table[idx] == s:
      return True
    # if the str is not at the original position
    if hash_table[idx] != "":
        new_idx = step_size(s, 13)
        stepSize = 1
        while hash_table[(idx + new_idx * stepSize) % len(hash_table)] != "":
            if hash_table[(idx + new_idx * stepSize) % len(hash_table)] == s:
                return True
            stepSize += 1
    return False



# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
# need to check both hash_table and hash_memo
def is_reducible (s, hash_table, hash_memo):
  # if original one does not contain a or i or o
  if 'a' not in s and 'i' not in s and 'o' not in s:
    return False
  # if the original str is a or i or o
  if s == 'a' or s == 'i' or s == 'o':
    return True
  # if s just in memo
  if find_word(s, hash_memo):
      return True

  reducible_words = []
  for i in range(len(s)):
    words = s[:i] + s[i + 1:]
    if find_word(words, hash_table):
      # append all reducible words into a lst
      reducible_words.append(words)

  for word in reducible_words:
    if word == 'a' or word == 'i' or word == 'o':
        return True
    if 'a' not in word and 'i' not in word and 'o' not in word:
        return False
    if is_reducible(word, hash_table, hash_memo):
        insert_word(s, hash_memo)
        return True
  return False



# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
  max_length_lst = []
  max_len = 0
  for i in range(len(string_list)):
    if len(string_list[i]) >= max_len:
      max_len = len(string_list[i])
  if max_len > 10:
      max_len = 10
  for i in range(len(string_list)):
    if len(string_list[i]) == max_len:
      max_length_lst.append(string_list[i])
  return max_length_lst

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  word_list.append("a")
  word_list.append("i")
  word_list.append("o")

  # find length of word_list
  length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  primeNum = length * 2
  while (is_prime(primeNum) == False):
      primeNum += 1

  # create and empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(primeNum):
      hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
      insert_word(word, hash_list)

  # create an empty hash_memo
  hash_memo = []

  # populate the hash_memo with M blank strings
  for i in range(primeNum):
      hash_memo.append("")

  # create and empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
      if is_reducible(word, hash_list, hash_memo):
          reducible_words.append(word)

  # find words of the maximum length in reducible_words
  longestWords = get_longest_words(reducible_words)

  # print the words of maximum length in alphabetical order
  # one word per line
  longestWords.sort()
  for word in longestWords:
      print(word)

if __name__ == "__main__":
  main()
