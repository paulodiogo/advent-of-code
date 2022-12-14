file1 = open('data.txt', 'r')
items = file1.readlines()

def getLetterValue(letter):

    if str(letter).islower():
        return ord(letter)-96
    else:
        return ord(letter)-38

total = 0

for item in items:

    mid = len(item) // 2

    firstHalf = item[:mid]
    secondHalf = item[mid:]

    for letter in firstHalf:
        if letter in secondHalf:
            total += getLetterValue(letter)
            break


print(total)