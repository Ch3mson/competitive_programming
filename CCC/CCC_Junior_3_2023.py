days = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
}

N = int(input("How many ppl?"))

repeat = int(0)

schedule = str(input("days available:"))
placeholder = 1
for x in schedule:
    
    if x == "Y":
        days[placeholder] = days[placeholder] + 1
    placeholder = placeholder + 1

output = ""

max = 0
for x in days:
    if max < days[x]:
        max = x

print(max)

for key, value in days:
    print(key)
    print(value)
    print(str(key) + " " + str(value))

print(output)
        
