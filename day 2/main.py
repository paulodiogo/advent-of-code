file1 = open('data.txt', 'r')
guides = file1.readlines()

def normalize(value):
    if value in ['A', 'X']:
        return 1, 'A'
    elif value in ['B', 'Y']:
        return 2, 'B'
    elif value in ['C', 'Z']:
        return 3, 'C'

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 0
DRAW = 3
WIN = 6

total = 0

for guide in guides:

    _, OP = normalize(guide.strip().split(' ')[0])
    PT_ME, ME = normalize(guide.strip().split(' ')[1])

    if (ME == ROCK and OP == SCISSORS) or (ME == SCISSORS and OP == PAPER) or (ME == PAPER and OP == ROCK):
        total += WIN + PT_ME
    elif OP == ME:
        total += DRAW + PT_ME
    else:        
        total += LOSE + PT_ME

print(total)

