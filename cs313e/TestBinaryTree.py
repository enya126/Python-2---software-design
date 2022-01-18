#  File: TestBinaryTree.py
#  Description: This program use python to test different binary trees.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 4/26/2021
#  Date Last Modified: 4/27/2021



import sys

class Node (object):
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class Tree (object):
    def __init__(self):
        self.root = Node(None)

        # insert data into the tree

    def insert(self, data):
        new_node = Node(data)

        if (self.root.data == None):
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

    # Returns true if two binary trees are similar
    # self is tree1 and pNode is tree3
    def is_similar (self, pNode):
        # check if both root are empty
        if self.root.data is None and pNode.root.data is None:
            return True
        else:
            return self.is_similar_helper(self.root, pNode.root)


    def is_similar_helper(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        # check their size
        if root1 == None and root2 != None:
            return False
        elif root1 != None and root2 == None:
            return False
        # check their data
        elif root1.data != root2.data:
            return False
        else:
            # check every lchild and rchild using recursion
            return self.is_similar_helper(root1.lchild, root2.lchild) and self.is_similar_helper(root1.rchild, root2.rchild)


    # Returns a list of nodes at a given level from left to right
    def get_level (self, level):
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
                lst.append(node)
            else:
                # recursively find the level
                self.get_level_helper(node.lchild, cur+1,level, lst)
                self.get_level_helper(node.rchild, cur+1,level, lst)



    # Returns the height of the tree
    # height is the longest root to leaf path
    def get_height (self):
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



    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        if self.root.data is None:
            return 0
        else:
            return self.num_codes_helper(self.root)

    def num_codes_helper(self, node):
        # base case
        if node is None:
            return 0
        else:
            # recursively go through all lchild and rchild
            # we do not want to count twice, so we add 1 at last to return the count
            return self.num_codes_helper(node.lchild) + self.num_codes_helper(node.rchild) + 1


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    # create all three trees
    tree1 = Tree()
    tree2 = Tree()
    tree3 = Tree()
    for i in tree1_input:
        tree1.insert(i)
    for i in tree2_input:
        tree2.insert(i)
    for i in tree3_input:
        tree3.insert(i)


    # Test your method is_similar()
    print(tree1.is_similar(tree3))
    tree3.is_similar(tree1)


    # Print the various levels of two of the trees that are different
    print(tree3.get_level(1))

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())
if __name__ == "__main__":
  main()