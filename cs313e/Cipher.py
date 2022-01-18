#  File: Cipher.py
#  Description: This program use python to
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 02/07/2021
#  Date Last Modified: 02/08/2021

import sys
import math

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt ( strng ):
    # change str into k*k matrix
    k = math.floor(math.sqrt(len(strng)))
    m = k ** 2
    l = len(strng)
    # if the square was smaller than the length of the string
    # because of floor function
    if m < len(strng):
        k += 1
    word_matrix = [[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            if i*k+j < len(strng):
                word_matrix[i][j] = strng[i*k+j]
            else:
                word_matrix[i][j] = '*'
    # create an empty list to put the encrypted matrix.
    final_lst = []
    # transpose the matrix
    trans_str = [[word_matrix[j][i] for j in range(k)] for i in range(k)]
    for i in range(k):
        # reverse the matrix
        new_lst = list(reversed(trans_str[i]))
        final_lst.append(new_lst)
    # convert matrix into string
    encry_output = ''.join(ele for sub in final_lst for ele in sub)
    # replace all the '*' with ''.
    encry_output = encry_output.replace('*', '')
    return encry_output
# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits

# Output: function returns an encrypted string
def decrypt ( strng ):
    # change str into k*k matrix
    k = math.floor(math.sqrt(len(strng)))
    m = k ** 2
    l = len(strng)
    if m < len(strng):
        k += 1
    word_matrix = [[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            if i * k + j < len(strng):
                word_matrix[i][j] = strng[i * k + j]
            else:
                word_matrix[i][j] = '*'
    # create an empty list to put the decrypted matrix.
    reversed_matrix = []
    # reverse the matrix
    for i in range(k):
        reverse_lst = list(reversed(word_matrix[i]))
        reversed_matrix.append(reverse_lst)
    # transpose the matrix
    final_decry = [[reversed_matrix[j][i] for j in range(k)] for i in range(k)]
    decry_output = ''.join(ele for sub in final_decry for ele in sub)
    # replace all the '*' with ''.
    decry_output = decry_output.replace('*', '')
    return decry_output

def main():
    # read the two strings P and Q from standard input
    input_p = sys.stdin.readline()
    input_q = sys.stdin.readline()
    # encrypt the string P
    encrypted_line = encrypt(input_p.strip())
    # decrypt the string Q
    decrypted_line = decrypt(input_q.strip())
    # print the encrypted string of P and the
    # decrypted string of Q to standard out
    print(encrypted_line)
    print(decrypted_line)

if __name__ == "__main__":
  main()