file1 = open('data.txt', 'r')
marker = file1.readlines()[0].strip()

diff = []

index = -1

for i in range(len(marker)):
    char = marker[i]

    if char not in diff:
        diff.append(char)        
    else:
        diff = diff[diff.index(char)+1:]
        diff.append(char)        
    
    index = i

    if len(diff) == 4:
        break

print(diff)
print(index+1)
        
    




