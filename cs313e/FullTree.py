#  File: FullTree.py

#  Description: This program use python to check if binary tree is full tree.

#  Student Name: Enya Liu

#  Student UT EID: el27773

#  Course Name: CS313E

#  Unique Number: 52230

#  Date Created: 5/8/2021

#  Date Last Modified: 5/8/2021


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the only parameter for the Tree class is self.root, which is a Node object
  # a printlevelorder method has been provided to help with debugging

  # complete the isFull method below and return a boolean
  def isFull(self):
    # self.printlevelorder()
    self.flag = True
    self.is_full_helper(self.root)
    return self.flag

  # helper function for checking isFull
  def is_full_helper(self, root):
    if not self.flag:
      return
    if not root:
      return None
    left = self.is_full_helper(root.lchild)
    right = self.is_full_helper(root.rchild)
    if not left and right or not right and left:
      self.flag = False
    return root


  # **there is no reason to change anything below this line**
    
  # prints each level in the tree separately
  # a _ character indicates that there is no node there
  def printlevelorder(self):
    def get_height_helper (aNode):
      if aNode == None:
        return 0
      else:
        return max(get_height_helper(aNode.lchild), get_height_helper(aNode.rchild)) + 1

    def printGivenLevel(root, level):
      if level == 1:
        if root is None:
          print('_', end = ' ')
        else:
          print(root.data, end = ' ')
      elif root is None:
        return root
      elif level > 1:
        printGivenLevel(root.lchild, level - 1)
        printGivenLevel(root.rchild, level - 1)

    h = get_height_helper(self.root)
    for i in range(1, h + 1):
        printGivenLevel(self.root, i)
        print()

  # creates a tree from a list input
  def __init__ (self, tree_list):
    if len(tree_list) == 0 or tree_list[0] == None:
      self.root = None
      return
    self.root = Node(tree_list[0])
    node_objs = [None]
    tree_list.insert(0, None)
    node_objs.append(self.root)
    for i in range(2, len(tree_list)):
      if tree_list[i] != None:
        parent_ind = i // 2
        parent_node = node_objs[parent_ind]
        new_node = Node(tree_list[i])
        # for error checking
        if parent_node != None:
          if i == parent_ind * 2:
            parent_node.lchild = new_node
          else:
            parent_node.rchild = new_node
          node_objs.append(new_node)
        else:
          node_objs.append(None)
      else:
        node_objs.append(None)

import sys
def main():
  # create the tree
  tree_list = sys.stdin.readlines()
  for i in range(len(tree_list)):
    tree_list[i] = tree_list[i].strip()
    if tree_list[i] == "None":
      tree_list[i] = None
    
  tree = Tree(tree_list)

  print (tree.isFull())

if __name__ == "__main__":
  main()
