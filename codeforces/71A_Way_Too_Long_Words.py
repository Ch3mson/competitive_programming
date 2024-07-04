
# the logic to process the word
def processWord(input: str) -> str: 
    charArr = list(input)
    if len(charArr) <= 10:
        return input
    else:
        middle = str(len(charArr) - 2)
        return charArr[0] + middle + charArr[-1]

num_lines = int(input())  # number of lines we will process
word_list = [] #put each input so we can print at the end


while num_lines > 0: # input each word
    output = input()
    word_list.append(output)
    num_lines-= 1

for word in word_list: # process and print each word
    print(processWord(word))
