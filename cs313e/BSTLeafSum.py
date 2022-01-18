#  File: BSTLeafSum.py

#  Description: This program use python to calculate the leaf sum.

#  Student Name:Enya Liu

#  Student UT EID: el27773

#  Course Name: CS313E

#  Unique Number: 52230

#  Date Created: 5/7/2021

#  Date Last Modified: 5/7/2021

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***

  # Returns an integer representing the sum of the leaf nodes
  def get_leaf_sum(self):
      return self.sum_leaf(self.root)

  # helper function of finding the sum of leaf nodes
  def sum_leaf(self, node):
      if self.is_leaf(node):
          return node.data
      elif node is None:
          return 0
      else:
          return self.sum_leaf(node.lchild) + self.sum_leaf(node.rchild)
      
  # helper function of checking if is leaf
  def is_leaf(self, node):
      if node is None:
          return False
      return node.lchild is None and node.rchild is None



# ***There is no reason to change anything below this line***

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_leaf_sum())

if __name__ == "__main__":
  main()