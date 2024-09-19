peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano":15500,
    "Cayenne": 40000,
    "Thai":75000,
    "Habanero": 125000
}

T = 0
N = int(input())
repeat = int(0)
while repeat < N:
    x = input()
    T += peppers.get(x)
    repeat += 1
    
print(T)
