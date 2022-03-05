#  File: ConnectedRooms.py

#  Description: Determine the minnimum number of keys you need to buy to complete the quest

#  Student Name: Enya Liu

#  Student UT EID: el27773

#  Course Name: CS313E

#  Unique Number: 52230

import sys

# finds the smallest number of keys needed to be bought to complete the quest
# returns an int
def solve(N, K, locks, keys):
    # always need 1 key to unlock room 1
    for i in range(1, N):
        # key matches
        if locks[i] == keys[i - 1]:
            keys[i-1] = 0
        # key don't match
        else:
            for j in range(0, i - 1):
                if locks[i] == keys[j]:
                    keys[j] = 0
    count = 0
    for j in keys:
        if j != 0:
            count += 1
    return count
                
# Here, we will read the input file and call the function to solve this problem.
# Do NOT change this
def main():
    # read in N (maze size)
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    locks = []
    keys = []
    lineSplit = sys.stdin.readline().strip().split(" ")
    for i in range(N):
        locks.append(int(lineSplit[i]))
    lineSplit = sys.stdin.readline().strip().split(" ")
    for i in range(N):
        keys.append(int(lineSplit[i]))
    
    print(solve(N, K, locks, keys))
 
if __name__ == "__main__":
    main()