"""
Input: A B  X Y

A B = width height of first painting
X Y = width height of second painting

Examples:
3 3 3 3 -> 18 === 2(2S + S)
2 2 4 4 -> 20 === 
1 2 3 1 -> 12 === 3 + 1 + 3 + 1 + 1 + 2 + 1
"""

import sys
line = sys.stdin.readline().strip().split(" ")

A = int(line[0])
B = int(line[1])
X = int(line[2])
Y = int(line[3])

print(min(2*(B+Y+max(X,A)), 2*(A+X+max(B,Y))))