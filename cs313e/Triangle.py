# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Enya Liu

# Student UT EID: el27773

# Course Name: CS 313E

# Unique Number: 52230

import sys
import math

TOL = 0.01


class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object

    def dist(self, other):
        return math.hypot (self.x - other.x, self.y - other.y)


class Triangle (object):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.PointA = PointA
        self.PointB = PointB
        self.PointC = PointC

    # print string representation of Triangle
    def __str__(self):
        return 'Point1: ({}, {}), Point2: ({}, {}), Point3: ({}, {}), Area: {}'.format(float(self.PointA.x),float(self.PointA.y), float(self.PointB.x),float(self.PointB.y), float(self.PointC.x),float(self.PointC.y), float(self.area()))

    # check congruence of Triangles with equality
    def __eq__(self, other):
        return abs(self.PointA.dist(self.PointB) - other.PointA.dist(other.PointB)) < TOL \
               and abs(self.PointB.dist(self.PointC) - other.PointB.dist(other.PointC)) < TOL \
               and abs(self.PointA.dist(self.PointC) - other.PointA.dist(other.PointC)) < TOL

    # returns whether or not the triangle is valid

    def is_triangle(self):
        if self.area() <= TOL:
            return False
        else:
            return True

    # return the area of the triangle:
    def area(self):
        area_triangle = abs((self.PointA.x * (self.PointB.y - self.PointC.y) + self.PointB.x * (self.PointC.y - self.PointA.y) + self.PointC.x * (self.PointA.y-self.PointB.y))/2)
        return float(area_triangle)

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
