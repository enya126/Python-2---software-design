#  File: Geometry.py
#  Description: This program use python to create binary tree to encrypt and decrypt.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/23/2021
#  Date Last Modified: 04/24/2021

import sys

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = Node(None)
        for data in encrypt_str:
            data = data.lower()
            if data == ' ':
                self.insert(data)
            elif 'a' <= data <= 'z':
                self.insert(data)
            # drop the character
            elif data < 'a' or data > 'z':
                continue
        return


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        new_node = Node(ch)
        temp = self.root
        parent = self.root
        # check if the tree is empty
        if self.root.data is None:
            self.root = new_node
        else:
            # compare the data
            while temp is not None:
                parent = temp
                if ch == ' ' and temp.data != ' ':
                    temp = temp.lChild
                elif temp.data > ch:
                    temp = temp.lChild
                elif temp.data < ch:
                    temp = temp.rChild
                # if ch already in the tree
                else:
                    return
            # temp is None now, but parent is not None, it's the node before None
            if ch < parent.data:
                parent.lChild = new_node
            elif ch > parent.data:
                parent.rChild = new_node
            else:
                return


    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        search_str = ''
        # check if empty
        if self.root is None:
            return ''
        elif self.root.data == ch:
            return '*'
        else:
            temp = self.root
            while temp is not None:
                if temp.data > ch:
                    temp = temp.lChild
                    search_str += '<'
                elif temp.data < ch:
                    temp = temp.rChild
                    search_str += '>'
                elif temp.data == ch:
                    return search_str
            # if the character does not exist
            return ''



    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        if st == '':
            return ''
        elif st == '*':
            return self.root.data
        else:
            temp = self.root
            for str in st:
                # if temp is small and do not have the character
                if temp is None:
                    return ''

                if str == '<':
                    temp = temp.lChild
                elif str == '>':
                    temp = temp.rChild
            # character does not exist in the tree
            if temp is None:
                return ''
            else:
                return temp.data


    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    # already did it in the init part
    def encrypt(self, st):
        encrypt_str = ''
        for i in range(len(st)):
            if 'a' <= st[i] <= 'z' or st[i] == ' ':
                if encrypt_str == '':
                    encrypt_str += self.search(st[i])
                else:
                    # add with delimiter
                    encrypt_str += ('!' + self.search(st[i]))
            else:
                continue

        return encrypt_str


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        init_str = st.split('!')
        decrypt_str = ''
        for i in init_str:
            # directly go through the tree to decrypt
            decrypt_str += self.traverse(i)
        return decrypt_str


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()