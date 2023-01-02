import sys

"""
Input: 
    Program should read lines of text from standard input. Each linr will contain a single positive integer, n

Output:
    For each input n, print to standard output the fibonacci number, F(n), one per line.

"""

for line in sys.stdin:
    line = int(line)
    f = [0,1]
    for num in range(2,line+1):
        f.append(f[num -1]+f[num -2])
    print(f[num])
