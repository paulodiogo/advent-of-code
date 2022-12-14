file1 = open('data.txt', 'r')
data = file1.readlines()

stacks = [[] for _ in range(9)]

for i in range(8):
    stack = data[i].replace('    ', ' ').replace('[', '').replace(']', ''). split(' ')

    for j in range(len(stack)):

        if stack[j].strip() != '':                                    
            stacks[j].insert(0, stack[j].strip())

print(stacks)

#move 1 from 5 to 6        
for i in range(10, len(data)):
    move = data[i].strip().split(' ')    
    num = int(move[1])
    fromStack = int(move[3]) - 1
    toStack = int(move[5]) - 1

    for j in range(num):        
        stacks[toStack].insert(len(stacks[toStack]), stacks[fromStack].pop())

final = [x[len(x)-1] for x in stacks] 

print(''.join(final))

