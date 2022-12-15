import math
file1 = open('data.txt', 'r')
programLines = file1.readlines()

X = 1
CYCLE = 0

SIGNALS = [20,60,100,140,180,220]

TOTAL = 0

for line in programLines:

    line = line.strip()

    if line == 'noop':
        CYCLE += 1
        
        if CYCLE in SIGNALS:
            TOTAL += CYCLE * X

        continue
    else:        
        CYCLE += 1

        if CYCLE in SIGNALS:
            TOTAL += CYCLE * X
        
        CYCLE += 1

        if CYCLE in SIGNALS:
            TOTAL += CYCLE * X

        X += int(line.split(' ')[1])

print(TOTAL)