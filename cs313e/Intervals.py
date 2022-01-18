#  File: Intervals.py
#  Description: This program use python to collapse intervals and identify them.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 02/04/2021
#  Date Last Modified: 02/05/2021

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
import sys

def merge_tuples (tuples_list):
    # sort the tuples
    lst = len(tuples_list)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tuples_list[j][0] > tuples_list[j + 1][0]):
                temp = tuples_list[j]
                tuples_list[j] = tuples_list[j + 1]
                tuples_list[j + 1] = temp
    # merge the tuples
    new_list = []
    for i in range(0, len(tuples_list)-1):
        if tuples_list[i][1] >= tuples_list[i + 1][0] and tuples_list[i][1] <= tuples_list[i + 1][1]:
            a = tuples_list[i][0]
            b = tuples_list[i + 1][1]
            temp_tuple = (a, b)
            tuples_list[i + 1] = temp_tuple
            #last case, append it
            if i == (len(tuples_list)-2):
                new_list.append((a, b))
        elif tuples_list[i][1] >= tuples_list[i + 1][0] and tuples_list[i][1] >= tuples_list[i + 1][1]:
            temp_tuple = tuples_list[i]
            tuples_list[i + 1] = temp_tuple
            #last cases
            if i == (len(tuples_list)-2):
                new_list.append(tuples_list[i])
        # two tuples do not intercept
        else:
            c = tuples_list[i]
            new_list.append(c)
            # if last case has no interval with the previous one.
            if i == (len(tuples_list)-2):
                new_list.append(tuples_list[i+1])
    return new_list
# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

# find interval size in another function
def find_interval_size(tuple):
    return tuple[1] - tuple[0]

def sort_by_interval_size (tuples_list):
    return sorted(tuples_list, key=find_interval_size)

def main():
    num = int(sys.stdin.readline())
    tupleList = []
    for i in range(num):
        a, b = map(int, sys.stdin.readline().split())
        tupleList.append((a, b))
    merged_tuples = merge_tuples(tupleList)
    sorted_tuples = sort_by_interval_size(merged_tuples)
    print(merged_tuples)
    print(sorted_tuples)
  # open file intervals.in and read the data and create a list of tuples

  # merge the list of tuples

  # sort the list of tuples according to the size of the interval

  # write the output list of tuples from the two functions

if __name__ == "__main__":
    main()