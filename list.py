# n =  input("Enter the number: ")
#
# list = n.split()
# sum = 0
#
# for x in list:
#     sum = sum + int (x)
# print(sum)

numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0

text = input("Enter the line: ")

for x in text:
    if x>='a' and x<='z':
        numberOfLetters = numberOfLetters + 1
    elif x>='0' and x<='9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 1
print("Number of words: ", numberOfWords + 1)
print("Number of digits: ", numberOfDigits)
print("Number of letters: ", numberOfLetters)



