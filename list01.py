
class SingleNode(object):
    def __init__(self, vaule):
            self.value = vaule
            self.next = None

class SingleLinkList(object):
    """
        description : 一个单链表
    """
    def __init__(self):
        self.head = None

    def SingleAdd(self, vaule):

        node = SingleNode(vaule)

        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def SinglePrint(self, cur):
        if cur is None:
            cur = self.head
        while cur is not None:
            print('{0}'.format(cur.value))
            cur = cur.next

    def reverseList(self):
        cur, prev, next = self.head, None, None

        while cur is not None:
            # python 中多变量赋值，先算好等会右边的所有值，然后一次性赋值给左边。
            #cur.next, prev, cur = prev, cur, cur.next
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def swapPairs(self):
        pre, pre.next = self, self.head
        '''
            pre = self
            pre.next = self.head
            self.next = self.head
            
        '''
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next

            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def testSelf(self):
        '''
          pre, pre.next = self, self.head
          return self.next

        '''
        # 这个 self.next，和 self.head, self.value 没有什么区别
        # 仅仅是赋值了一个新的变量而已。
        self.next = '123456'
        print(self.next)


if __name__ == "__main__":

    listNode = [1, 2, 3, 4]
    SingleList = SingleLinkList()
    for i in listNode:
        SingleList.SingleAdd(i)

    SingleList.SinglePrint(None)

    print("--------------------------")

    list1 = SingleList.swapPairs()
    #list1 = SingleList.reverseList()

    SingleList.SinglePrint(list1)


    print("--------------------------")

    list2 = SingleList.testSelf()
    #SingleList.SinglePrint(list2)

