#  File: Josephus.py
#  Description: This program use python to do circular linked lst.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/12/2021
#  Date Last Modified: 04/12/2021

import sys


class Link(object):
    def __init__(self, data):
        self.next = None
        self.data = data



class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_node = Link(data)
        temp = self.first
        # check empty
        if temp is None:
            self.first = new_node
            new_node.next = self.first
            self.first = new_node
        else:
            # insert at last
            while temp.next is not self.first:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.first
            temp.next = new_node


    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        # check if empty
        temp = self.first
        if temp is None:
            return None
        else:
            while temp.data != data:
                if temp.next == self.first:
                    return None
                else:
                    temp = temp.next
            return temp

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        origin_first = self.first
        temp = self.first
        # initiate prev here
        previous = self.first

        # checks if empty
        if temp is None:
            return None

        # make the prev link before the next previous link in a lst
        # if not fully circled the lst|
        # it's importance to keep track of prev
        # otherwise order will be chaos
        while previous.next != temp:
            previous = previous.next

        # goes through the list until the data position
        while temp.data != data:
            if temp.next == self.first:
                return None
            else:
                previous = temp
                temp = temp.next

        if self.first != self.first.next:
            # circular list|
            self.first = temp.next
        # if there is only a head in the lst
        else:
            # store the value of temp
            temp = Link(self.first)
            self.first = None
            return temp

        previous.next = temp.next

        # try to sort the lst
        if self.lst_length() == 3:
            self.first = origin_first
        return temp


    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        temp = self.first
        # check if empty
        if self.first is None:
            return None

        while temp.data != start:
            temp = temp.next

        count = 1
        # search untill the nth postion
        while count != n:
            temp = temp.next
            count += 1

        self.delete(temp.data)
        # print the deleted data
        print(temp.data)
        # return the next data for next round
        return temp.next

    def lst_length(self):
        temp = self.first
        if self.first is None:
            return 0
        else:
            count = 0
            while temp.next != self.first:
                count += 1
                temp = temp.next
            return count
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        temp = self.first
        # check empty
        if self.first is None:
            return "[]"
        else:
            str_lst = "["
            while temp.next != self.first:
                str_lst += (str(temp.data) + ", ")
                temp = temp.next

            str_lst += (str(temp.data) + "]")
            return str_lst


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    # number the soldiers and make a single Linked list
    soldier_lst = CircularList()
    for i in range(1, num_soldiers+1):
        soldier_lst.insert(i)

    # use start count as start, elim_num as n, use delete after
    for i in range(num_soldiers):
        start_count = soldier_lst.delete_after(start_count,elim_num)
        start_count = start_count.data

    # print out that each is on a new line





if __name__ == "__main__":
    main()