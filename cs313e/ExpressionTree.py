#  File: ExpressionTree.py
#  Description: This program use python to create an expression tree.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 4/19/2021
#  Date Last Modified: 4/21/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = Node(None)

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        equation = expr.split()
        # make root thr starting point
        temp = self.root
        # make the input into a stack
        equa = Stack()

        for i in equation:
            if i == '(':
                equa.push(temp)
                # create the lchild to move down
                temp.lChild = Node(None)
                temp = temp.lChild
            # '.' is decimal
            elif i.isdigit() or '.' in i:
                temp.data = i
                temp = equa.pop()

            elif i in operators:
                temp.data = i
                # move down
                equa.push(temp)
                temp.rChild = Node(None)
                temp = temp.rChild
            elif i == ')':
                if not equa.is_empty():
                    # move up
                    temp = equa.pop()
                else:
                    break

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode.data == '+':
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif aNode.data == '-':
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif aNode.data == '*':
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif aNode.data == '/':
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif aNode.data == '//':
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        elif aNode.data == '%':
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif aNode.data == '**':
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        # if it is just number
        elif aNode.data.isdigit() or '.' in aNode.data:
            return float(aNode.data)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self,aNode):
        tot_str = ''
        node_str = []
        result = self.pre_order_helper(aNode, node_str)
        for i in result:
            tot_str += (i+' ')
        return tot_str

    def pre_order_helper(self, aNode, node_str):
        # base case
        if aNode is None:
            return node_str
        else:
            node_str.append(aNode.data)
            node_str = self.pre_order_helper(aNode.lChild, node_str)
            node_str = self.pre_order_helper(aNode.rChild,node_str)
            return node_str

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        tot_str = ''
        node_str = []
        result = self.post_order_helper(aNode, node_str)
        for i in result:
            tot_str += (i+' ')
        return tot_str

    def post_order_helper(self, aNode, node_str):
        # base case
        if aNode is None:
            return node_str
        else:
            # recursively move then print
            node_str = self.post_order_helper(aNode.lChild, node_str)
            node_str = self.post_order_helper(aNode.rChild, node_str)
            node_str.append(aNode.data)
            return node_str

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", tree.evaluate(tree.root))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()