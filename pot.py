#! /usr/bin/python3

import sys

def main():
    # read the number of lines of input
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # define a place to store the sum
    sum_num = 0

    # read all lines of data
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        num = int(line)
        
        x = num % 10
        a = num // 10
        sum_num += (a ** x)
        
    #print result
    print(sum_num)

if __name__ == "__main__":
    main()
        
