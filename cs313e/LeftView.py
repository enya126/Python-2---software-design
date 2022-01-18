#  File: LeftView.py

#  Description: This program use python to find the most left nodes.

#  Student Name:Enya Liu

#  Student UT EID: el27773

#  Course Name: CS313E

#  Unique Number: 52230

#  Date Created: 5/7/2021

#  Date Last Modified: 5/7/2021

import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

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

  # Returns a list containing the left view of the BST
  def get_left_view(self):
      if self.root is None:
          return []
      else:
          left_lst = []
          level = 0
          while level < self.get_height():
              # get all nodes at that level
              all_nodes = self.get_level(level)
              # append the most left one
              left_lst.append(all_nodes[0])
              # move to the next level
              level += 1
          return left_lst


  # Returns a list of nodes at a given level from left to right
  def get_level(self, level):
      cur = 0
      data_lst = []
      self.get_level_helper(self.root, cur, level, data_lst)
      if self.root.data is None:
          return []
      else:
          return data_lst

  def get_level_helper(self, node, cur, level, lst):
      if cur > level:
          return lst
      elif node is None:
          return
      else:
          # base case
          if cur == level:
              lst.append(node.data)
          else:
              # recursively find the level
              self.get_level_helper(node.lchild, cur + 1, level, lst)
              self.get_level_helper(node.rchild, cur + 1, level, lst)

  # Returns the height of the tree
  # height is the longest root to leaf path
  def get_height(self):
      # check if its empty
      if self.root.data is None:
          return 0
      else:
          return self.get_height_helper(self.root)

  def get_height_helper(self, node):
      # base case
      if node is None:
          return 0
      else:
          # trace the height of lchild and rchild using 2 parameters
          l_height = self.get_height_helper(node.lchild)
          r_height = self.get_height_helper(node.rchild)

          if l_height > r_height:
              return l_height + 1
          else:
              return r_height + 1
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

    print(tree.get_left_view())

if __name__ == "__main__":
  main()