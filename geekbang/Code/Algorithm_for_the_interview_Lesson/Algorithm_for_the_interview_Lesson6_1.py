'''
    反转一个链表
        Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
        output: 5 -> 4 -> 3 -> 2 -> 1 -> null
'''

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

    def SinglePrint(self,cur):
        if cur is None:
            cur = self.head

        while cur is not None:
            print('{0}'.format(cur.value))
            cur = cur.next

    def reverseList(self):
        cur, prev = self.head, None
        while cur is not None:
            # python 中多变量赋值，先算好等会右边的所有值，
            # 然后一次性赋值给左边。
            cur.next, prev, cur = prev, cur, cur.next
        return prev

if __name__ == "__main__":

    listNode = [1, 2, 3, 4, 5]

    slist = SingleLinkList()
    for i in listNode:
        slist.SingleAdd(i)

    slist.SinglePrint(None)

    print('---------')
    blist = slist.reverseList()
    slist.SinglePrint(blist)




