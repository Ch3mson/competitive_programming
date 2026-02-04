import sys

line = sys.stdin.readline().strip()

"""
Sample Input 1:
zepelepenapa papapripikapa

Sample Output 1:
zelena paprika

"""

output = ""
i = 0
vowels = "aeiou"

while i < len(line):
  if line[i] in vowels:
    output += line[i]
    i += 3
  else:
    output += line[i]
    i += 1

print(output)