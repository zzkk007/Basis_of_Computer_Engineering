"""
   1.单链表的插入、删除、查找操作；
   2.链表中存储的数据类型是Int
   3.增加了单向链表反转、检查环、删除倒数第N个节点、求链表中间节点等方法

"""

class Node(object):
    def __int__(self, data, next = None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data


    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self,next):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

class SinglyLinkedList(object):

    def __init__(self):
        '''单向列表的初始化方法.'''
        self.__head = None

    def find_by_value(self,value):
        '''按照数据值在单向列表中查找.
        参数：
            value: 查找的数据
        返回：
            Node
        '''
        node = self.__head
        if node != None and node.data != value:
            node = node.next
        else:
            return node

    def find_by_index(self, index):
        '''按照索引值在单向列表中查找.
        参数：
            index 索引值
        返回:
            None
        '''
        node = self.__head
        pos = 0
        while node != None and pos != index:
            node = node.next
            pos += 1
        return node

    def insert_to_head(self, value):
        '''在链表的头部插入一个存储value数值的Node节点.
        参数：
            value: 将要存储的数据
        '''

        node = Node(value)
        node.next = self.__head
        self.__head = node

    def insert_after(self, node, value):
        '''在链表的某个指定Node节点之后插入一个存储value数据的Node节点.
        参数：
            node : 指定的一个Node 结点
            value: 将要存储在新 Node 结点中的数据

        '''
        if node == None:
            return

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, value):
        '''在链表的某个指定Node 结点之前插入一个存储 value 数据的Node 结点
        参数：
            node：指定的node 结点
            value:将要存储新 Node 结点中的数据
        '''
        if node == None or self.__head == None:
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False
        while pro.next != node:
            if pro.next == None:
                not_found = True
                break
            else:
                pro = pro.next
        if not_found == False:
            pro.next = new_node
            new_node.next = node

    def delete_by_node(self, node):
        '''在链表中删除指定的 Node 的结点
        参数：
             node:指定的Node节点

        '''
        if self.__head == None:
            return

        if node == self.__head:
            self.__head = node.next
            return
        pro = self.__head
        not_found = False
        while pro.next != node:
            if pro.next == None:
                not_found = True
                break
            else:
                pro = pro.next

        if  not_found == False:
            pro.next = node.next

    def delete_by_value(self, value):
        '''在链表中删除指定存储数据的Node节点.
        参数:
             value:指定的存储数据
        '''
        if self.__head == None:
            return

        if self.__head.data == value:
            self.__head = self.__head.next

        pro = self.__head
        node = self.__head.next
        not_found = False
        while node.data != value:
            if node.next == None:
                not_found = True
                break
            else:
                pro = node
                node = node.next
        if not_found == False:
            pro.next = node.next


    def delete_last_N_node(self, n):
        '''删除链表中倒数第N个节点.
        主体思路：
            设置快慢两个指针，快指针先行，慢指针不动，当快指针跨了 N 步之后，快慢指针同时往链表尾部移动。
            当快指针到达链表尾部时，慢指针所指向的就是链表的倒数第 N 个节点。
        参数：
            n: 需要删除的倒数第 n 个结点
        '''

        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next
            step += 1

        while fast.next != None:
            tmp = slow
            fast = fast.next
            slow = slow.next

        tmp.next = slow.next


    def find_mid_node(self):
        '''查找链表中的中间节点.
        主体思想：
            设置快慢指针，快指针每次跨两步，慢指针每次跨一步，则当快指针达到链表尾部时，
            慢指针指向链表的中间节点

        返回：
            node: 链表的中间节点

        '''

        fast = self.__head
        slow = self.__head

        while fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def create_node(self, value):
        return Node(value)

    def print_all(self):
        pos = self.__head
        if pos == Node:
            return
        while pos.next != Node:
            print(str(pos.data) + '-->')
            pos = pos.next
        print(pos.data)

    def reversed_self(self):
        '''翻转链表自身'''

        if self.__head == Node or self.__head.next == Node:
            return

        pre = self.__head
        node = self.__head.next

        while node != None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self.__head.next = None
        self.__head = pre

    def __reversed_with_two_node(self, pre, node):
        '''翻转相邻两个节点.
        参数:
            pre：前一个节点
            node：当前节点
        '''
        tmp = node.next
        node.next = pre
        pre = node
        node = tmp

        return (pre, node)

    def has_ring(self):
        '''检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环

        '''
        fast = self.__head
        slow = self.__head
        while fast.next != None and fast != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False


def reverse(head):
    reverse_head = None
    while head:
        next = head._next
        head._next = reverse_head
        reverse_head = head
        head = next

    return reverse_head


def is_palindrome(l):
    '''check a single-linked list whether a palindrome
    '''
    l.print_all()
    slow = l.__head
    fast = l.__head
    position = 0

    while fast and fast.next:
        slow = slow._next
        fast = fast._next.next
        position += 1

    reverse_node = reverse(slow)

    head_node = l.__head
    is_palin = True
    while(head_node and reverse_node):
        if(head_node.data == reverse_node.data):
            head_node=head_node._next
            reverse_node = reverse_node._next
        else:
            is_palin = False
            break
    return True

