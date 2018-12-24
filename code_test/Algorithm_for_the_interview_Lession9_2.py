
class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


queue1 = Queue()
queue2 = Queue()

def stack_push(item):

    if queue1.is_empty():
        queue1.enqueue(item)

def stack_pop():

    if queue2.length() == 0:

        for i in range(queue1.length() - 1):
            queue2.enqueue(queue1.dequeue())

        print(queue1.dequeue())

    elif queue1.length() == 0:

        for i in range(queue2.length() - 1):
            queue1.enqueue(queue2.dequeue())

        print(queue2.dequeue())

    else:
        print("error!!")


if __name__ == "__main__":

    for i in range(10):
        stack_push(i)
        
    stack_pop()








