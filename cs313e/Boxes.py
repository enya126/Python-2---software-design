#  File: Boxes.py
#  Description: This program use python to find the relationship between boxes.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 3/25/2021
#  Date Last Modified: 3/27/2021

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# Input:
# 	box_list is a list of boxes that have already been sorted
# 	sub_set is a list that is the current subset of boxes
# 	idx is an index in the list box_list
# 	all_box_subsets is a 3-D list that has all the subset of boxes
# Output:
#		Nothing should be returned (None)
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    # base case
    if idx == len(box_list):
        all_box_subsets.append(sub_set)
    else:
        new_sub_set = sub_set[:]
        sub_set.append(box_list[idx])
        sub_sets_boxes(box_list,sub_set, idx+1, all_box_subsets)
        sub_sets_boxes(box_list, new_sub_set, idx+1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
# Input:
#   all_box_subsets: list containing every subset of boxes
# Output:
#		return a list containing all largest nesting subsets
# 	i.e. if multiple nesting subsets are of size 4 (and 4 is the largest size),
# 	the list MUST contain both subsets
def largest_nesting_subsets (all_box_subsets):
    count = 0
    fitted_subset = []
    largest_subset = []
    # find all fitted subsets
    for i in range(0, len(all_box_subsets)):
        for j in range(0, len(all_box_subsets[i])-1):
            if len(all_box_subsets[i][j]) <= 1:
                count = 0
            elif does_fit(all_box_subsets[i][j], all_box_subsets[i][j+1]):
                count += 1
        if count == len(all_box_subsets[i]) - 1:
            fitted_subset.append(all_box_subsets[i])
            count = 0
        else:
            count = 0
    res = max(len(ele) for ele in fitted_subset)
    for set in fitted_subset:
        if len(set) == res:
            largest_subset.append(set)
    return largest_subset




# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)
  # print the largest number of boxes that fit
  if len(all_nesting_boxes[0]) <= 0:
      print(1)
  else:
      print(len(all_nesting_boxes[0]))


  # print the number of sets of such boxes
  if len(all_box_subsets) <= 0:
      print(num_boxes)
  else:
      print(len(all_nesting_boxes))


if __name__ == "__main__":
  main()