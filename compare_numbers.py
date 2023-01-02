import sys


"""
Input:
    Consists of two integers A and B on a line, seperated by space

Output: 
    If A < B, return <
    If A > B, return >
    If A = B, return =
"""
for line in sys.stdin:
    line = line.split()  #Creates a list of string 
    A, B = map(int, line) ##Converts the list of strings to a tuple of number

    if A == B:
        print("=")
    elif A < B:
        print("<")
    else:
        print(">")
