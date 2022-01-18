#  File: Spiral.py
#  Description: This program use python to create a spiral and find the sum of it.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 01/31/2021
#  Date Last Modified: 02/02/2021
# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral

import sys

def create_spiral ( n ):
    # if n is even add one to n
    if not n % 2 == 1:
        n += 1
    #define an empty 2d array.
    arr = [[0 for i in range(n)] for i in range(n)]
    arr[n // 2][n // 2] = 1
    val = n ** 2
    # how many round we circled.
    for i in range(n // 2 + 1):
        # different conditions in each round
        for j in range(n - i - 1, i - 1, -1):
            arr[i][j] = val
            val -= 1
        for j in range(i + 1, n - i):
            arr[j][i] = val
            val -= 1
        for j in range(i + 1, n - i):
            arr[n - i - 1][j] = val
            val -= 1
        for j in range(n - i - 2, i, -1):
            arr[j][n - i - 1] = val
            val -= 1
    return arr

def sum_adjacent_numbers(spiral, n):
    length = len(spiral)
    if n <= 0 or n > length ** 2:
        return 0
    row = 0
    col = 0
    for x in range(0, length):
        for y in range (0, length):
            if spiral[x][y] == n:
                row = x
                col = y
                break
    # double for loop
    #write if statement for each case
    num_sum = 0
    if 0 <= row - 1 < length and 0 <= col - 1 < length:
        num_sum += spiral[row - 1][col - 1]
    if 0 <= row - 1 < length and 0 <= col < length:
        num_sum += spiral[row - 1][col]
    if 0 <= row - 1 < length and 1 <= col + 1 < length:
        num_sum += spiral[row - 1][col + 1]
    if 0 <= row < length and 0 <= col - 1 < length:
        num_sum += spiral[row][col - 1]
    if 0 <= row < length and 0 <= col + 1 < length:
        num_sum += spiral[row][col + 1]
    if 1 <= row + 1 < length and 0 <= col - 1 < length:
        num_sum += spiral[row + 1][col - 1]
    if 1 <= row + 1 < length and 0 <= col < length:
        num_sum += spiral[row + 1][col]
    if 1 <= row + 1 < length and 1 <= col + 1 < length:
        num_sum += spiral[row + 1][col + 1]
    return num_sum

def main():
    line = sys.stdin.readline()
    dimension = int(line.rstrip())
    for line in sys.stdin.readlines():
        if line != "":
            num = int(line.rstrip())
            sum_num = (sum_adjacent_numbers(create_spiral(dimension), num))
            print(sum_num)

if __name__ == "__main__":
    main()
