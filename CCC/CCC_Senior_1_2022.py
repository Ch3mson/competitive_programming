"""
Good fours and good fives

solutions are written as N = 4a + 5b
where 

a <= n/4
b <= n/5

"""


N = int(input())
count = int(0)

for a in range (0, int(N/4) + 1):
    if (N-4*a) >= 0 and (N - 4*a) % 5 == 0:
        count += 1

print(count)
