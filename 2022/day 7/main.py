file1 = open('data.txt', 'r')
commands = file1.readlines()

class Node:
    def __init__(self, parent, command):
        self.parent = parent
        self.kind = 'dir' if command.strip().split(' ')[0] == 'dir' else 'file'
        self.name = command.strip().split(' ')[1]
        self.size = 0 if command.strip().split(' ')[0] == 'dir' else int(command.strip().split(' ')[0])
        self.children = {}

    def addChild(self, child):
        self.children[child.name] = child

        if child.kind == 'file':
            self.size += child.size
            if self.parent != None:
                self.parent.size += self.size

    def findChild(self, name):
        return self.children[name]
    
    def printar(self, tabs):
        if self.kind == 'file':
            antes = ''.join(['\t']*tabs)
            return f'{antes}- {self.name} ({self.kind}) ({self.size})' 
        else:

            childStr = []

            for key in self.children.keys():
                childStr.append(self.children[key].printar(tabs+1))
            
            nom = '\n'.join(childStr)

            antes = ''.join(['\t']*tabs)
            
            return f'{antes}- {self.name}({self.kind})({self.size})\n{nom}' 

    def directoriesAtMost(self, maxSize, dirs):
        
        if self.kind == 'dir' and self.size <= maxSize:
            dirs.append(self.size)

        for key in self.children.keys():
            self.children[key].directoriesAtMost(maxSize, dirs)


root = Node(None, 'dir /')
actual = root

for i in range(1, len(commands)):
    if commands[i].strip() == '$ ls':
        continue
    elif commands[i].strip().startswith('$') and commands[i].strip().endswith('..'):
        actual = actual.parent        
    elif commands[i].strip().startswith('$') and not commands[i].strip().endswith('..'):
        actual = actual.findChild(commands[i].strip().split(' ')[2])        
    else:
        child = Node(actual, commands[i])
        actual.addChild(child)
        
dirs = []

root.directoriesAtMost(100000, dirs)
      
print(sum(dirs))
    


    