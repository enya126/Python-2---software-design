#  File: Poly.py
#  Description: This program use python to represent a polynomial using linked list.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/15/2021
#  Date Last Modified: 04/18/2021

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    new_node = Link(coeff, exp)
    temp = self.first
    # check empty
    if self.first is None:
      self.first = new_node
    else:
      prev = self.first
      while temp.exp >= exp:
        prev = temp
        temp = temp.next
        if temp is None:
          # insert at last
          prev.next = new_node
          return
      # temp.exp < exp now
      # if first exp < exp
      if temp == self.first:
        new_node.next = temp
        self.first = new_node
      # insert the node in this position
      else:
        prev.next = new_node
        new_node.next = temp



  # add polynomial p to this polynomial and return the sum
  # to add
  def add (self, p):
    new_lst = LinkedList()
    if self.first is None and p.first is None:
      return None
    elif self.first is None:
      return p
    elif p.first is None:
      return self
    else:
      temp = self.first
      p_temp = p.first
      while temp is not None and p_temp is not None:
        if temp.exp == p_temp.exp:
          new_coeff = temp.coeff+p_temp.coeff
          # check the coeff is not 0
          if new_coeff == 0:
            temp = temp.next
            p_temp = p_temp.next
          else:
            new_lst.insert_in_order(new_coeff, temp.exp)
            temp = temp.next
            p_temp = p_temp.next
        # if p has higher exp than self
        elif temp.exp < p_temp.exp:
          new_lst.insert_in_order(p_temp.coeff, p_temp.exp)
          p_temp = p_temp.next
        # if self has higher exp than p
        elif temp.exp > p_temp.exp:
          new_lst.insert_in_order(temp.coeff, temp.exp)
          temp = temp.next
      # check for leftover in both lsts
      while temp is not None:
        new_lst.insert_in_order(temp.coeff, temp.exp)
        temp = temp.next
      while p_temp is not None:
        new_lst.insert_in_order(p_temp.coeff, p_temp.exp)
        p_temp = p_temp.next
      return new_lst


  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    mult_lst = LinkedList()
    if self.first is None and p.first is None:
      return None
    elif self.first is None:
      return p
    elif p.first is None:
      return self
    else:
      temp = self.first
      while temp is not None:
        p_temp = p.first
        while p_temp is not None:
          mult_coeff = temp.coeff*p_temp.coeff
          mult_exp = temp.exp+p_temp.exp
          mult_lst.insert_in_order(mult_coeff,mult_exp)
          p_temp = p_temp.next
        temp = temp.next
      return mult_lst

  # if there's poly with same exp left in the poly, merge them
  def merge(self):
    if self.first is not None:
      temp = self.first
      while temp is not None:
        after = temp.next
        while after is not None and after.exp == temp.exp:
          new_coeff = temp.coeff + after.coeff
          temp.coeff = new_coeff
          temp.next = after.next
          after = after.next
        temp = temp.next

  def remove_zero(self):
    if self.first is not None:
      temp = self.first
      while temp is not None:
        if temp.coeff != 0:
          prev = temp
          temp = temp.next
        else:
          after = temp.next
          prev.next = after
          temp = temp.next





  # create a string representation of the polynomial
  def __str__ (self):
    if self.first is None:
      return ''
    else:
      temp = self.first
      poly_str = f"{temp}"
      while temp.next != None:
        temp = temp.next
        poly_str += f" + {temp}"
      return poly_str

  def check_lst(self):
    if self.first is None:
      return None
    else:
      temp = self.first
      while temp is not None:
        print(temp.coeff)
        print(temp.exp)
        temp = temp.next

def main():
  # read data from file poly.in from stdin
  # read the number of elements in a poly
  line = sys.stdin.readline()
  line = line.strip()
  num_x = int(line)

  # read the rest line and put them into a linked lst
  # create polynomial p
  p_lst = LinkedList()
  for i in range(num_x):
    line = sys.stdin.readline()
    line = line.strip()
    poly = line.split()
    p_lst.insert_in_order(int(poly[0]), int(poly[1]))

  line = sys.stdin.readline()
  line = line.strip()
  line = line.rstrip()
  if line.isnumeric():
    num_q = int(line)
  else:
    line = sys.stdin.readline()
    line = line.strip()
    num_q = int(line)
  # create polynomial q
  q_lst = LinkedList()
  for i in range(num_q):
    line = sys.stdin.readline()
    line = line.strip()
    poly = line.split()
    q_lst.insert_in_order(int(poly[0]), int(poly[1]))



  # get sum of p and q and print sum
  sum_lst = p_lst.add(q_lst)
  sum_lst.merge()
  print(sum_lst)

  # get product of p and q and print product
  mult_lst = p_lst.mult(q_lst)
  mult_lst.merge()
  mult_lst.remove_zero()
  print(mult_lst)

if __name__ == "__main__":
  main()