import sys

"""
Given a positive integer, the program determines if the number is an exact power of two

Input:
     Read lines from standard input. Each line contains a positive integer

Output:
    For each line of input, print to standard input 'true' if the number is an exact power of two and 'false' if not. Each result is printed on a new line.
"""


for line in sys.stdin:
    line = int(line)
    if (line == 0):
        print('False')

        ##Keep dividing the number by 2 iteratively until line becomes 1. 
        #In any iteration, if line % 2 becomes non-zero and line is not 1 
        #then line is not a power of 2. If line becomes 1 then it is a power of 2.
    while line != 1:
        if line % 2 != 0:
            print('False')
        line = line // 2
    print('True')


