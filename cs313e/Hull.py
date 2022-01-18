#  File: Hull.py
#  Description: This program use python to find the convex hull that enclose all the points.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 02/28/2021
#  Date Last Modified: 03/02/2021

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    # create a matrix first
    matrix = [[1 for i in range(3)] for j in range(3)]
    matrix[0][1] = p.x
    matrix[0][2] = p.y
    matrix[1][1] = q.x
    matrix[1][2] = q.y
    matrix[2][1] = r.x
    matrix[2][2] = r.y
    # find the determinant of the matrix
    determinant = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]) - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]) \
        + matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
    return determinant


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    upper_hull = []
    # append first two points into the list
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            del upper_hull[-2]
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    reverse_list = sorted_points[::-1]
    # append the rest points into the list and delete some points that are not vertices
    for i in range(2, len(reverse_list)):
        lower_hull.append(reverse_list[i])
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            del lower_hull[-2]
    del lower_hull[0]
    del lower_hull[-1]
    convex_tot = upper_hull + lower_hull
    return convex_tot


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    det_first = 0
    # add the first part of the determinant
    for i in range(0, len(convex_poly)-1):
        point_head = convex_poly[i]
        point_tail = convex_poly[i+1]
        det_first += point_head.x * point_tail.y
        det_first -= point_head.y * point_tail.x
    point_back = convex_poly[-1]
    point_first = convex_poly[0]
    det_first += point_back.x * point_first.y
    det_first -= point_back.y * point_first.x
    area_det = 1/2 * abs(det_first)
    return area_det


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))
    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)
    '''
    # print the sorted list of Point objects
    for p in sorted_points:
        print (str(p))
    '''
    # get the convex hull
    convex = convex_hull(sorted_points)
    # print the convex hull
    print('Convex Hull')
    for i in convex:
        print(i)
    print()
    # get the area of the convex hull
    area = area_poly(convex)
    # print the area of the convex hull
    print('Area of Convex Hull =', area)


if __name__ == "__main__":
  main()