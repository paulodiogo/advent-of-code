file1 = open('data.txt', 'r')
pairs = file1.readlines()

total = 0

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

for pair in pairs:

    elvesPairs = pair.strip().split(',')
    elveOneB, elveOneE = int(elvesPairs[0].split('-')[0]), int(elvesPairs[0].split('-')[1])
    elveTwoB, elveTwoE = int(elvesPairs[1].split('-')[0]), int(elvesPairs[1].split('-')[1])

    arr1 = set(range(elveOneB, elveOneE+1))
    arr2 = set(range(elveTwoB, elveTwoE+1))

    if arr1.issubset(arr2) or arr2.issubset(arr1):
        total += 1        

print(total)


