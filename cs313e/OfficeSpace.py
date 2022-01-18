# File: OfficeSpace.py
# Description: This program use python to find office space.
# Student Name: Enya Liu
# Student UT EID: el27773
# Course Name: CS 313E
# Unique Number: 52230
# Date Created: 02/25/2021
# Date Last Modified: 02/26/2021

import sys
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    rect_length = rect[2] - rect[0]
    rect_width = rect[3] - rect[1]
    rect_area = rect_width * rect_length
    return rect_area
# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
# return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    if rect1[0] < rect2[0]:
      max_x1 = rect2[0]
    else:
      max_x1 = rect1[0]
    if rect1[1] < rect2[1]:
      max_y1 = rect2[1]
    else:
      max_y1 = rect1[1]
    if rect1[2] < rect2[2]:
      min_x2 = rect1[2]
    else:
      min_x2 = rect2[2]
    if rect1[3] < rect2[3]:
      min_y2 = rect1[3]
    else:
      min_y2 = rect2[3]
    if max_y1 >= min_y2:
      return 0, 0, 0, 0
    else:
      return max_x1, max_y1, min_x2, min_y2

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
# space in the office
def unallocated_space (bldg):
    count = 0
    for i in bldg:
      for j in i:
        if j == 0:
          count += 1
    return count

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
# space in the office
def contested_space (bldg):
    count = 0
    for i in bldg:
      for j in i:
        if j > 1:
          count += 1
    return count

# Input: bldg is a 2-D array representing the whole office space
# rect is a rectangle in the form of a tuple of 4 integers
# representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
# space in the office that the employee gets
def uncontested_space (bldg, rect):
    count = 0
    for i in range(rect[1], rect[3]):
      for j in range(rect[0], rect[2]):
        if bldg[i][j] < 2:
          count += 1
    return count

# Input: office is a rectangle in the form of a tuple of 4 integers
# representing the whole office space
# cubicles is a list of tuples of 4 integers representing all
# the requested cubicles
# Output: a 2-D list of integers representing the office building and
# showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    space_list = [[0 for i in range(office[2])] for j in range(office[3])]
    for i in range(len(cubicles)):
      for k in range(cubicles[i][0], cubicles[i][2]):
        for j in range(cubicles[i][1], cubicles[i][3]):
          space_list[j][k] += 1
    return space_list

def main():
    # read the data
    a, b = sys.stdin.readline().strip().split(' ')
    office = (0, 0, int(a), int(b))
    num = sys.stdin.readline()
    num = int(num)
    my_dict = {}
    cubicles_list = []
    for i in range(num):
      name, x1, y1, x2, y2 = sys.stdin.readline().strip().split(' ')
      personal_space = (int(x1), int(y1), int(x2), int(y2))
      my_dict.update({name:personal_space})
      cubicles_list.extend([personal_space])
    # print the following results after computation
    # compute the total office space
    total_space = int(a) * int(b)
    print('Total', total_space)
    # compute the total unallocated space
    print('Unallocated', unallocated_space(request_space(office, cubicles_list)))
    # compute the total contested space
    print('Contested', contested_space(request_space(office, cubicles_list)))
    # compute the uncontested space that each employee gets
    for names, areas in my_dict.items():
      print(names, uncontested_space(request_space(office,cubicles_list), areas))

if __name__ == "__main__":
 main()