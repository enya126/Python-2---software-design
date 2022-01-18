#  File: Work.py
#  Description: This program uses python to find the work time and maximize the sleep time for Vyasa.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 3/5/2021
#  Date Last Modified: 3/7/2021

import sys

import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    sum_tot = 0
    p = 1
    copy_v = v
    while copy_v/k >= k:
        copy_v = copy_v/k
        p += 1
    for i in range(0, p+1):
        sum_tot += v // (k**i)
        if v // k ** p == 0:
            break
    return sum_tot

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    if n <= k:
        return n
    for v in range(n//2, n):
        if sum_series(v, k) >= n:
            return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    if n <= k:
        return n
    start = 0
    end = n
    # v gets smaller as k gets smaller, but it will always be larger than half of n
    for v in range(n//2, n):
        mid = (start + end) / 2
        if sum_series(v, k) < n:
            start = mid + 1
        elif sum_series(v, k) > n+2:
            end = mid - 1
        elif sum_series(v, k) >= n:
            return v

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()