#  File: Geometry.py
#  Description: This program use python to find relationship and geometry of graphics.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 02/11/2021
#  Date Last Modified: 02/15/2021

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return '({}, {}, {})'.format(float(self.x), float(self.y), float(self.z))

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      distance_between = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
      return distance_between

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      return (abs(self.x-other.x)<tol) and (abs(self.y-other.y)<tol) and (abs(self.z-other.z)<tol)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.x = x
      self.y = y
      self.z = z
      self.center = Point(self.x, self.y, self.z)
      self.radius = radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      x = str(self.x)
      y = str(self.y)
      z = str(self.z)
      radius = str(self.radius)
      return 'Center: ({}, {}, {}), Radius: {}'.format(float(x), float(y), float(z), float(radius))
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      area_sphere = 4 * math.pi * (self.radius ** 2)
      return area_sphere

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      volume_sphere = 4 / 3 * math.pi * (self.radius ** 3)
      return volume_sphere

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      distance_inside = math.sqrt((p.x - self.center.x) ** 2 + (p.y - self.center.y) ** 2 + (p.z - self.center.z) ** 2)
      return distance_inside < self.radius
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      distance_sphere = self.center.distance(other.center) + other.radius
      if distance_sphere < self.radius:
          return True
      else:
          return False

  # determine if a Cube is strictly inside this Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      # check the distance of diagonal and the distance between center
      distance_center = self.center.distance(a_cube.center)
      diagonal_cube = math.sqrt(3) / 2 * a_cube.side
      distance_total = distance_center + diagonal_cube
      return distance_total < self.radius

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    # cylinder's radius + center y distance must be less than the sphere's radius
    # cylinder's center distance + height must be less than the diameter of the sphere
      distance_height = abs(self.center.z - a_cyl.center.z) + a_cyl.height / 2
      distance_radius = abs(self.center.y - a_cyl.center.y) + a_cyl.radius
      return distance_height < self.radius and distance_radius < self.radius


  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
  # distance between 2 centers is less than radius 1 + radius 2
  # and is_inside_sphere is False
      distance_centers = self.center.distance(other.center)
      sum_radius = self.radius + other.radius
      if distance_centers < sum_radius and not self.is_inside_sphere(other):
          return True
      else:
          return False

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      distance_center = self.center.distance(a_cube.center)
      sum_radius = self.radius + a_cube.side
      if distance_center < sum_radius and not self.is_inside_cube(a_cube):
          return True
      else:
          return False


  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      x = self.center.x
      y = self.center.y
      z = self.center.z
      side = int(2 * self.radius / math.sqrt(3))
      return Cube(x, y, z, side)


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.x = x
      self.y = y
      self.z = z
      self.center = Point(self.x, self.y, self.z)
      self.side = side

  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
      x = self.x
      y = self.y
      z = self.z
      side = self.side
      return 'Center: ({}, {}, {}), Side: {}'.format(float(x), float(y), float(z), float(side))
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      area_cube = 6 * (self.side ** 2)
      return float(area_cube)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      volume_cube = self.side ** 3
      return float(volume_cube)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      # distance between point and center is less than 1/2 side
      distance_point = math.sqrt((self.center.x - p.x) ** 2 + (self.center.y - p.y) ** 2 + \
                                 (self.center.x - p.z) ** 2)
      return distance_point < 1/2 * self.side

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      distance_center = math.sqrt((self.center.x - a_sphere.center.x) ** 2 \
                                  + (self.center.y - a_sphere.center.y) ** 2 + \
                                  (self.center.z - a_sphere.center.z) ** 2)
      return distance_center + a_sphere.radius < 1/2 * self.side

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    # x max, min, y max min should all inside another cube
    # compare each with self cube
      comparison_maximum = ((other.x+0.5*other.side) < (self.x+0.5*self.side)) \
      & ((other.y+0.5*other.side) < (self.y+0.5*self.side))\
      & ((other.z+0.5*other.side) < (self.z+0.5*self.side))
      comparison_minimum = ((other.x-0.5*other.side) > (self.x-0.5*self.side)) \
      & ((other.y-0.5*other.side) > (self.y-0.5*self.side))\
      & ((other.z-0.5*other.side) > (self.z-0.5*self.side))
      return comparison_maximum and comparison_minimum

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    # the distance between center of the cylinder to the side of the cube
    # is greater than the radius
    # find left side and right side's distance
      left_x = self.center.x - self.side * 1/2
      distance_left = math.sqrt((left_x - a_cyl.center.x) ** 2 + (self.center.y - a_cyl.center.y) ** 2)
      right_x = self.center.x + self.side * 1/2
      distance_right = math.sqrt((right_x - a_cyl.center.x) ** 2 + (self.center.y - a_cyl.center.y) ** 2)
      distance_height = abs(self.center.z - a_cyl.center.z) + 1/2 * a_cyl.height
      if distance_left > a_cyl.radius and distance_right > a_cyl.radius and distance_height < 1/2 * self.side:
          return True
      else:
          return False

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    # any one corner falls in the interval of x max, y max and z max.
    comparison_x = ((other.x + 0.5 * other.side) >= (self.x + 0.5 * self.side)) and ((other.x - 0.5 * other.side) <= (self.x + 0.5 * self.side))
    comparison_y = ((other.y + 0.5 * other.side) >= (self.y + 0.5 * self.side)) and ((other.y - 0.5 * other.side) <= (self.y + 0.5 * self.side))
    comparison_z = ((other.z + 0.5 * other.side) >= (self.z + 0.5 * self.side)) and ((other.z - 0.5 * other.side) <= (self.z + 0.5 * self.side))
    if not self.is_inside_cube(other):
        return comparison_x or comparison_y or comparison_z

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # if only one corner intersects with another
      pass


    # if two corners intersects with another



  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      distance_center = 1/2 * self.side
      x = self.center.x
      y = self.center.y
      z = self.center.z
      return Sphere(x, y, z, distance_center)

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.x = x
      self.y = y
      self.z = z
      self.radius = radius
      self.height = height
      self.center = Point(self.x, self.y, self.z)

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      x = self.x
      y = self.y
      z = self.z
      radius = self.radius
      height = self.height
      return 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(float(x), float(y), float(z), float(radius), float(height))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      area_cylinder = 2 * math.pi * self.radius * (self.height + self.radius)
      return area_cylinder

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      volume_cylinder = math.pi * (self.radius) ** 2 * self.height
      return volume_cylinder

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      distance_radius = self.x - p.x
      distance_height = abs(self.z - p.z)
      return distance_radius < self.radius and distance_height < self.height / 2
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      distance_radius = self.center.distance(a_sphere.center) + a_sphere.radius
      distance_height = self.center.distance(a_sphere.center) + a_sphere.radius
      return distance_radius < self.radius and distance_height < self.height / 2

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      # distance between z + 1/2 side must be less than 1/2 height
      distance_height = abs(self.center.z - a_cube.center.z) + 0.5 * a_cube.side
      distance_length = abs(self.center.y - a_cube.center.y) + 0.5 * a_cube.side
      return distance_height<0.5 * self.height and distance_length < self.radius

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      distance_radius = self.center.distance(other.center) + other.radius
      distance_height = self.center.distance(other.center) + other.height / 2
      return distance_radius < self.radius and distance_height < self.height / 2

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      distance_xy = math.sqrt((self.center.x-other.center.x)**2 + (self.center.y-other.center.y)**2)
      difference_z = abs(self.center.z - other.center.z)
      if not self.is_inside_cylinder(other):
          return distance_xy < self.radius + other.radius or difference_z < 0.5*(self.height+other.height)
      else:
          return False

def main():
  # read data from standard input
  # read the coordinates of the first Point p
    a, b, c = sys.stdin.readline().strip().split(' ')
  # create a Point object
    p = Point(float(a), float(b), float(c))
  # read the coordinates of the second Point q
    a, b, c = sys.stdin.readline().strip().split(' ')
  # create a Point object
    q = Point(float(a), float(b), float(c))
  # read the coordinates of the center and radius of sphereA
    a, b, c, d = sys.stdin.readline().split(' ')
  # create a Sphere object
    sphereA = Sphere(float(a), float(b), float(c), float(d))
  # read the coordinates of the center and radius of sphereB
    a, b, c, d = sys.stdin.readline().strip().split(' ')
  # create a Sphere object
    sphereB = Sphere(float(a), float(b), float(c), float(d))
  # read the coordinates of the center and side of cubeA
    a, b, c, d = sys.stdin.readline().strip().split(' ')
  # create a Cube object
    cubeA = Cube(float(a), float(b), float(c), float(d))
  # read the coordinates of the center and side of cubeB
    a, b, c, d = sys.stdin.readline().strip().split(' ')
  # create a Cube object
    cubeB = Cube(float(a), float(b), float(c), float(d))
  # read the coordinates of the center, radius and height of cylA
    a, b, c, d, h = sys.stdin.readline().strip().split(' ')
  # create a Cylinder object
    cylA = Cylinder(float(a), float(b), float(c), float(d), float(h))
  # read the coordinates of the center, radius and height of cylB
    a, b, c, d, h = sys.stdin.readline().strip().split(' ')
  # create a Cylinder object
    cylB = Cylinder(float(a), float(b), float(c), float(d), float(h))
  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
    origin = Point(0, 0, 0)
    if p.distance(origin) > q.distance(origin):
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

  # print if Point p is inside sphereA
    if sphereA.is_inside_point (p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")
  # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")
  # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")
  # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")
  # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")
  # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube (cubeB):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")
  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
    cube_new = sphereA.circumscribe_cube()
    cube_volume = cube_new.volume()
    if cube_volume > cylA.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  # print if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")
  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere (sphereA):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")
  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube (cubeB):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")
  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder (cylB):
        print("cylB is inside cubeA")
    else:
        print("cylA is not inside cubeA")
  # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube (cubeB):
      print("cubeA does intersect cubeB")
    else:
      print("cubeA does not intersect cubeB")
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
    sphere_in = cubeA.inscribe_sphere()
    if sphere_in.area() > cylA.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  # print if Point p is inside cylA
    if cylA.is_inside_point (p):
      print("Point p is inside cylA")
    else:
      print("Point p is not inside cylA")
  # print if sphereA is inside cylA
    if cylA.is_inside_sphere (sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")
  # print if cubeA is inside cylA
    if cylA.is_inside_cube (cubeA):
      print("cubeA is inside cylA")
    else:
      print("cubeA is not inside cylA")
  # print if cylB is inside cylA
    if cylA.is_inside_cylinder (cylB):
      print("cylB is inside cylA")
    else:
      print("cylB is not inside cylA")
  # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder (cylB):
        print("cylB does not intersect cylA")
    else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()