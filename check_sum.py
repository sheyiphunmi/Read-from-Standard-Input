import sys

"""

write a program that computes an integer's checksum. To compute the checksum, break the integer into its constituent digits and, working from right to left,
doubling every second digit. If the product results in a number with two digits, treat those two digits independently. 
Then, sum all the digits for the final checksum.

For example. 1496 has a checksum of 21. We compute this by first breaking it into constituents and doubling the ever second digit...
Thus, we have 6, 18, 4, 2. Then, the individual dians are summed as 6 + (1 + 8) + 4 + 2 = 21

Input:
    Program read lines from standard input. Each line contains one integer.

Output:
    For each line of input, print to standard output the integers checksum one checksum per line

e.g

Test Input:
    5678

Expected Output:
    20
"""

for line in sys.stdin:
    line = int(line)
    # total variable which returns sum
    total = 0
    # counter variable which count the even position
    c = 0
    # running a loop while n != 0
    while(line!=0):
        #breaking the number into digits
        r = int(line%10)
        # increase counter
        c=c+1
        # if counter is even positioned then double the number
        if c%2==0:                   
            r = r*2
            while(r!=0):
                # do the process
                total = total + int(r%10)
                r = int(r/10)
            line=int(line/10)    
        else:
            # if counter is odd position then simple add the digit 
            total = total + r
            # into total
            line=int(line/10)
    # in the last return the sum of digits
    print(total)                
                  