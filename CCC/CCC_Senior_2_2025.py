import sys
import re
line = sys.stdin.readline().strip()
index = int(sys.stdin.readline().strip())

letters = re.findall(r'[a-z]+', line)
numbers = list(map(int, re.findall(r'\d+', line)))

total = sum(numbers)

k = index % total

for i in range(len(numbers)):
  if k < numbers[i]:
    print(letters[i])
    break
  else:
    k -= numbers[i]