#  File: Rocks.py
#  Description: Determines the rocks collide or not

#  Student Name: Enya Liu

#  Student UT EID: el27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/2/2021

#  Date Last Modified: 4/2/2021

'''
John has a row of rocks, represented by an array of nonzero integers.
Each rock moves to the right if its integer is positive, and left otherwise.
The power of each rock is its integer squared. Assuming that each rock moves
at the same speed, some rocks will meet. If two rocks meet, the one with less
power disappears. If both rocks have the same power, both rocks disappear.
Return the arary after all such meetings have occurred. Two rocks moving in the
same direction will not meet.
'''

import sys

# Input:  rocks is a list of nonzero integers
# Output: return a list representing rocks after all meetings have occurred
def get_rock_list(rocks):
    if len(rocks) == 2:
        if (rocks[0])**2 >= (rocks[1])**2:
            return []
        else:
            return rocks
    ''' Ex. get_rock_list([-8, 9, 3, -8]) -> [-8, 9] '''
    rocks = rocks[::-1]
    for i in range(0, len(rocks)):
        if rocks[i] < 0:
            for j in range(i+1, len(rocks)):
                if rocks[j]>0:
                   if (rocks[i])**2 > (rocks[j])**2:
                      rocks[j] = 0
                   else:
                      rocks[i] = 0
    rocks = [i for i in rocks if i !=0]
    return rocks[::-1]




# ***There is no reason to change anything below this line***

def main():
	rocks = [int(r) for r in sys.stdin.readline().strip().split(" ")]
	result = get_rock_list(rocks)
	print(result)

if __name__ == "__main__":
	main()
