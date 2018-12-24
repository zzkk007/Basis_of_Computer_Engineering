class Stock(object):

    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.insert(0,node)

    def pop(self):
        if self.queueA==[]:
            return None

        while len(self.queueA) != 1:
            self.queueB.insert(0,self.queueA.pop())

        self.queueA,self.queueB=self.queueB,self.queueA

        return self.queueB.pop()


stack1 = Stock()
stack1.push(1)
stack1.push(2)
print(stack1.pop())
print(stack1.pop())







