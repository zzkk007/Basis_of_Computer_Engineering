class Queue:
    def __init__(self):
        self.stockA=[]
        self.stockB=[]

    def push(self, node):
        self.stockA.append(node)

    def pop(self):

        if self.stockB==[]:
            for i in range(len(self.stockA)):
                self.stockB.append(self.stockA.pop())
        return self.stockB.pop()

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())
print(queue.pop())
print(queue.pop())

queue.push(4)
print(queue.pop())




