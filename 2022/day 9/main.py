import math
file1 = open('data.txt', 'r')
motions = file1.readlines()

H = [0,0]
T = [0,0]

POSITIONS = [(0,0)]

LAST = None

for motion in motions:
    D = motion.strip().split(' ')[0]
    N = int(motion.strip().split(' ')[1])

    for i in range(1, N+1):
        
        LAST = H.copy()

        if D == 'R':
            H[0] += 1
        elif D == 'L':
            H[0] -= 1
        elif D == 'U':
            H[1] += 1
        elif D == 'D':
            H[1] -= 1        

        DIS = math.sqrt(((T[0]-H[0])**2)+((T[1]-H[1])**2))
        if DIS > 1.414214:
            copyLAST = LAST.copy()
            POSITIONS.append((copyLAST[0], copyLAST[1]))
            T = copyLAST           

        

print(len(set(POSITIONS)))

