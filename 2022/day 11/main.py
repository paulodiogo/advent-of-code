import math
file1 = open('data.txt', 'r')
monkeysData = file1.readlines()

class Operation:
    def __init__(self, operation):
        splited = operation.strip().replace('Operation: new = ', '').split(' ')
        self.kind = splited[1]
        self.left = splited[0]
        self.right = splited[2]
    
    def execute(self, level):

        valueL = int(self.left) if self.left != 'old' else level
        valueR = int(self.right) if self.right != 'old' else level

        if self.kind == '+':
            return valueL + valueR
        elif self.kind == '*':
            return valueL * valueR

    def __str__(self):
        return f'Operation: new = {self.left} {self.kind} {self.right}'


class Monkey:
    
    def __init__(self, num):
        self.num = num
        self.count = 0
    
    def addItems(self, items):
        self.items = list(map(int, list(items.strip().replace('Starting items: ', '').split(', '))))      

    def addItem(self, item):
        self.items.append(item)  
    
    def addOperation(self, operation):               
        self.operation = Operation(operation)
    
    def addTest(self, divisible, ifTrue, ifFalse):                    
        self.divisible = int(divisible.strip().replace('Test: divisible by ', ''))
        self.ifTrue = int(ifTrue.strip().replace('If true: throw to monkey ', ''))
        self.ifFalse = int(ifFalse.strip().replace('If false: throw to monkey ', ''))

    def inspectItems(self):
        self.count += len(self.items)
        throwedItems = []

        for i in range(len(self.items)):
            item = self.items[i]
            worryLevel = int(math.floor(self.operation.execute(item) / 3))

            if worryLevel % self.divisible == 0:
                throwedItems.append((self.ifTrue, worryLevel))
            else:
                throwedItems.append((self.ifFalse, worryLevel))
            
        self.items.clear()

        return throwedItems


    def __str__(self):
        
        return f'Monkey {self.num}:' + \
                f'\nStarting items: {self.items}'+ \
                f'\n{self.operation}'+ \
                f'\nTest: divisible by {self.divisible}'+ \
                f'\n\tIf true: throw to monkey {self.ifTrue}'+ \
                f'\n\tIf false: throw to monkey {self.ifFalse}'
        

beginMonkeys = [i for i, s in enumerate(monkeysData) if 'Monkey' in s]

monkeys = {}

for i in beginMonkeys:

    num = int(monkeysData[i].strip().split(' ')[1].split(':')[0])
    monkey = Monkey(num)
    monkey.addItems(monkeysData[i+1])
    monkey.addOperation(monkeysData[i+2])
    monkey.addTest(monkeysData[i+3], monkeysData[i+4], monkeysData[i+5])

    monkeys[num] = monkey

for _ in range(20):

    for m in monkeys.keys():

        inspected = monkeys[m].inspectItems()
        
        for item in inspected:        
            monkeys[item[0]].addItem(item[1])

total = 1

totals = [monkeys[x].count for x in monkeys.keys()]

totals.sort(reverse=True)
totals = totals[:2]

print(totals[0]*totals[1])