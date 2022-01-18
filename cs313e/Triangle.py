#  File: Boxes.py
#  Description: This program use python to find the greatest path sum of a triangle.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 3/28/2021
#  Date Last Modified: 3/29/2021

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
#recursive approach that stores all path sum
def brute_force(grid):
    all_sum = []
    brute_force_helper(grid,0,0,0,all_sum)
    return max(all_sum)

# use helper function to keep track of path sum
def brute_force_helper(grid, idx_out, idx, path_sum, all_sum):
    # base case is it reaches bottom
    if idx_out == (len(grid)):
        # append all the sum in the end (base case)
        all_sum.append(path_sum)
    else:
        path_sum += grid[idx_out][idx]
        return brute_force_helper(grid, idx_out+1, idx, path_sum, all_sum) or brute_force_helper(grid, idx_out+1, idx+1, path_sum, all_sum)

# returns the greatest path sum using greedy approach
def greedy(grid):
    # start from the first num
    grid_sum = grid[0][0]
    idx = 0
    for i in range(1, len(grid)):
        if grid[i][idx] > grid[i][idx+1]:
            grid_sum += grid[i][idx]
        else:
            grid_sum += grid[i][idx+1]
            idx = idx+1
    return grid_sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    all_sum = []
    divide_conquer_helper(grid, 0, all_sum)
    return int(max(all_sum))

def divide_conquer_helper(grid, path_sum, all_sum):
    # base case
    if len(grid) == 1:
        all_sum.append(path_sum + grid[0][0])
    else:
        grid1 = []
        grid2 = []
        # separate the triangle
        for i in grid[1:]:
            grid1.append(i[1:])
            grid2.append(i[:-1])
        path_sum += grid[0][0]
        return (divide_conquer_helper(grid1, path_sum, all_sum)) or (divide_conquer_helper(grid2, path_sum, all_sum))

# returns the greatest path sum and the new grid using dynamic programming
# start at the bottom
def dynamic_prog(grid):
    # loop for bottom-up calculation
    for i in range(len(grid)-2, -1, -1):
        for j in range(i + 1):
            # if the below one is larger, add it
            if grid[i + 1][j] > grid[i + 1][j + 1]:
                grid[i][j] += grid[i + 1][j]
            else:
                grid[i][j] += grid[i + 1][j + 1]

    # return the top element that stores the maximum sum
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # call the function
    # print time taken using exhaustive search
    print('The greatest path sum through exhaustive search is', str(max(brute_force(grid))))
    print('The time taken for exhaustive search in seconds is', times)

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print('The greatest path sum through greedy search is', str(greedy(grid)))
    print('The time taken for greedy approach in seconds is', times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print('The greatest path sum through recursive search is', str(max(divide_conquer(grid))))
    print('The time taken for recursive search in seconds is', times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print('The greatest path sum through dynamic programming is', str(dynamic_prog(grid)))
    print('The time taken for dynamic programming in seconds is', times)


if __name__ == "__main__":
    main()