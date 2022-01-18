#  File: TestLinkedList.py
#  Description: This program use python to do do single linked list.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 04/08/2021
#  Date Last Modified: 04/11/2021

class Link(object):
    def __init__(self, data):
        self.next = None
        self.data = data



class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None



    # get number of links
    def get_num_links(self):
        count = 0
        pos = self.first
        # always check if empty
        if pos is None:
            return 0
        else:
            while pos is not None:
                count += 1
                pos = pos.next
            return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_node = Link(data)
        new_node.next = self.first
        self.first = new_node

    # add an item at the end of a list
    def insert_last(self, data):
        new_node = Link(data)
        # if the list is empty
        if self.first is None:
            self.first = new_node
        else:
            # if there is elements in the list
            temp = self.first
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_node = Link(data)
        temp = self.first
        # if the list is empty
        if self.first is None:
            self.first = new_node
        else:
            while data >= temp.data:
                prev = temp
                temp = temp.next
                if temp is None:
                    break
        # inserted data's next pointer to original's next pointer
            new_node.next = temp
        # original's next pointer to inserted data
        # consider edge case here if self.first == 6 and insert 5
            prev.next = new_node

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        temp = self.first
        if temp is None:
            return None
        else:
            while data != temp.data:
                if temp.next is None:
                    return None
                else:
                    temp = temp.next
            return temp

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        temp = self.first
        if temp is None:
            return None
        else:
            # if they do not match, keep checking the list
            while data != temp.data:
                if temp.next is None:
                    return None
                else:
                    temp = temp.next
            return temp

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        list_str = ''
        # check empty
        if self.first is None:
            return list_str
        while current is not None:
            count = 0
            # use count to check the number of strings in a line
            while count < 10:
                if current is None:
                    # eliminate the space after all strs
                    break
                else:
                    # eliminate the space after 10 strs
                    if count == 9:
                        list_str += str(current.data)
                        current = current.next
                        count += 1
                    else:
                        list_str += str(current.data) + '  '
                        current = current.next
                        count += 1
            list_str += '\n'
        return list_str.rstrip()


    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        temp = None
        new_lst = LinkedList()
        if self.is_empty() is False:
            temp = self.first
        if temp is None:
            # return new_lst rather than None to avoid pointer point on Nonetype
            return new_lst
        else:
            while temp is not None:
                # append data
                if temp.data is not None:
                    new_lst.insert_last(temp.data)
                    temp = temp.next
                else:
                    break
            return new_lst

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_lst = LinkedList()
        temp = self.first
        # if it is empty:
        if temp is None:
            return None
        # insert at first
        while temp is not None:
            new_lst.insert_first(temp.data)
            temp = temp.next
        return new_lst

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_lst = LinkedList()
        temp_lst = []
        temp = self.first
        # append the first one
        while temp is not None:
            temp_lst.append(temp.data)
            temp = temp.next
        # use functions of normal list
        temp_lst.sort()
        for data in temp_lst:
            new_lst.insert_last(data)
        return new_lst


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if self.is_empty():
            return True
        else:
            temp = self.first
            while temp.next is not None:
                if temp.data > temp.next.data:
                    return False
                else:
                    # keep going
                    temp = temp.next
            return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        self_lst = self.sort_list()
        other_lst = other.sort_list()
        # create a new linked lst
        merged_lst = LinkedList()
        temp_self = self_lst.first
        temp_other = other_lst.first
        # check some situations like both empty or one is empty
        if temp_self is None and temp_other is None:
            return None
        while temp_self is not None and temp_other is not None:
            # merge in order, comparing betw data
            if temp_self.data < temp_other.data:
                merged_lst.insert_last(temp_self.data)
                temp_self = temp_self.next
            else:
                merged_lst.insert_last(temp_other.data)
                temp_other = temp_other.next
        while temp_self is not None:
            merged_lst.insert_last(temp_self.data)
            temp_self = temp_self.next
        while temp_other is not None:
            merged_lst.insert_last(temp_other.data)
            temp_other = temp_other.next
        return merged_lst


    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        # eliminate some situation where must not equal
        if self.first is None and other.first is None:
            return True
        elif self.first is None or other.first is None:
            return False
        elif self.get_num_links() != other.get_num_links():
            return False
        else:
            temp_self = self.first
            temp_other = other.first
            while temp_self is not None and temp_other is not None:
                # check the data one by one
                if temp_self.data != temp_other.data:
                    return False
                temp_self = temp_self.next
                temp_other = temp_other.next
            return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        temp = self.first
        # check if empty
        if temp is None:
            return None
        else:
            linked_list = self.copy_list()
            # use a normal lst to count for the occurance of a data
            data_list = []
            while temp is not None:
                data_list.append(temp.data)
                temp = temp.next
            # reverse it to keep the first occurance, not the last
            data_list.reverse()
            cur = linked_list.first
            while cur is not None:
                if data_list.count(cur.data) > 1:
                    linked_list.delete_link(cur.data)
                    # pop the data
                    data_list.pop(data_list.index(cur.data))
                cur = cur.next
            # reverse it back to normal
            data_list.reverse()
            new_lst = LinkedList()
            # append the deleted lst back to a linked lst
            for i in data_list:
                new_lst.insert_last(i)
            return new_lst



