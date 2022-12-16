import math, ast
file1 = open('data.txt', 'r')
signalsLines = file1.readlines()

signals = []
correctOrder = []

pair = 1

for i in range(0, len(signalsLines), 3):
    leftSide = ast.literal_eval(signalsLines[i])
    rightSide = ast.literal_eval(signalsLines[i+1])

    signals.append((pair, leftSide, rightSide))
    pair += 1

def compare(left, right):

    if isinstance(left, int) and isinstance(right, int):
        return 'LW' if left < right else 'NX' if left == right else 'GT'
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, list):
        result = None        

        for i in range(len(left)):

            if i == len(right):
                break

            result = compare(left[i], right[i])
            
            if result == 'NX':
                continue            
            
            break

        if (result == 'NX' or result == None):
            return 'LW' if (len(left) == len(right) or len(left) < len(right)) else 'GT'

        return result

for item in signals:

    if compare(item[1], item[2]) == 'LW':
        correctOrder.append(item[0])



print(sum(correctOrder))