
def processWord(input: str) -> str:
    charArr = list(input)
    if len(charArr) <= 10:
        return input
    else:
        middle = str(len(charArr) - 2)
        return charArr[0] + middle + charArr[-1]

num_lines = int(input())  # number of lines we will process
word_list = []

while num_lines > 0:
    output = input()
    word_list.append(output)
    num_lines-= 1

for word in word_list:
    print(processWord(word))
