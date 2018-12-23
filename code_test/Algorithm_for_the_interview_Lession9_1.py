class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items is None

    def push(self, num):
        self.items.append(num)

    def pop(self):
        if self.items is not None:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items is not None:
            return self.items[len(self.items) - 1]

    def len(self):
        return len(self.items)


if __name__ == "__main__":

    inputs = Stack()
    outputs = Stack()

    for i in range(10):
        inputs.push(i)

    while inputs.len():
        for i in range(inputs.len()):
            outputs.push(inputs.pop())

    for i in range(outputs.len()):
        print(outputs.pop())





