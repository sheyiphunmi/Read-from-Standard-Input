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
    if line <= 0:
        print('False')
    elif line & (line - 1) == 0:   ## Bitwise operation :Bitwise AND operator Returns 1 if both the bits are 1 else 0.
        print('True')
    else:
        print('False')