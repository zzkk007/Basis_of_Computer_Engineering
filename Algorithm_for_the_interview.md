"-----------------------------------------------------------------"

       本篇笔记是学习极客学院 覃超老师《算法面试通过40讲》学习笔记
        
"-----------------------------------------------------------------"

"""01 合格程序员的第一个步：算法和数据结构"""

    1、算法和数据结构是一个程序员内功修炼。

"""02 如何事半功倍的学习算法和数据结构"""

       1、课程目标内容细分模块

       2、刻意联系

       3、时时反馈 （github 看别人的源码、LeetCode）
""""""

"""03 如何计算算法的复杂度"""

    1、算法复杂度指算法在编写成可执行程序后，运行时所需要的资源，
        资源时间资源和内存资源

        时间复杂度是指执行算法所需要的计算工作量；
        而空间复杂度是指执行这个算法所需要的内存空间。

    2、时间复杂度：

        在计算机科学中，算法的时间复杂度是一个函数，
        它定性描述了该算法的运行时间。
        时间复杂度常用大O符号表述。

        大O符号（英语：Big O notation），又称为渐进符号，是用于描述函数渐近行为的数学符号。
        更确切地说，它是用另一个（通常更简单的）函数来描述一个函数数量级的渐近上界。

        常见的时间复杂度：

             阶        非正式术语          执行次数函数举例
            O(1)      常数复杂度               12

            O(log n)  对数复杂度               5log2n+20

            O(n)      线性时间复杂度            2n + 3

            O(nlogn)   nlogn阶                 2n+3nlog2n+19

            O(n^2)    平方                   3n^2 + 2n + 1

            O(n^3)     立方                  6n3+2n2+3n+4

            O(2^n)     指数                  2^n

            O(n!)      阶乘

        注意，经常将log2n（以2为底的对数）简写成logn

        所消耗的时间从小到大

        O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)

        递归时间时间复杂度：

            Master Theorem
            是有递归进行下面的运算的时间复杂度：

            Binary search (二分法查找)              O(logn)
            Binary tree traersal（二叉树遍历）       O(n)
            Optimal sorted matrix search（排序）    O(n)
            Merge sort  （归并排序）                 O(nlog(n))

    3、空间复杂度：

        与时间复杂度类似，空间复杂度是指算法在计算机内执行时所需存储空间的度量。
        记作:
            S(n)=O(f(n))
        算法执行期间所需要的存储空间包括3个部分：
            算法程序所占的空间；
            输入的初始数据所占的存储空间；
            算法执行过程中所需要的额外空间。
        在许多实际问题中，为了减少算法所占的存储空间，通常采用压缩存储技术。

"""04 如何通过 LeetCode 来进行算法题目练习"""

    1、刻意练习，不舒服、不爽、枯燥。

    2、一道题，不要急于下手，要看考的知识点，哪里是坑。
        有多少种方法考虑到算法复杂度的问题。
    3、天天刷题，天天练习

"-----------------------------------------------------"

"""005 理论讲解：数组 & 链表 """


    1、Array:

        时间复杂度：
            Access : O(1)
            Insert : 平均 O(n)
            Delete : 平均 O(n)

    2、链表：

        时间复杂度：
            Access : O(n)
            Insert : O(1)
            Delete : O(1)

"""006 面试题:反转一个单链表&判断链表是否有环"""

    1、反转一个链表，
        例如：
         Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
        output: 5 -> 4 -> 3 -> 2 -> 1 -> null

        例子：

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
                    cur, prev = self.head, None
                    while cur is not None:
                        # python 中多变量赋值，先算好等会右边的所有值，
                        # 然后一次性赋值给左边。
                        cur.next, prev, cur = prev, cur, cur.next
                    return prev
            if __name__ == "__main__":

                listNode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                SingleList = SingleLinkList()
                for i in listNode:
                    SingleList.SingleAdd(i)

                SingleList.SinglePrint(None)

                print("--------------------------")

                list1 = SingleList.reverseList()

                SingleList.SinglePrint(list1)

    2、 给一个链表，反转他们相邻的节点

        Example:

          input : 1 -> 2 -> 3 -> 4
         output : 2 -> 1 -> 4 -> 3



















"-----------------------------------------------------------------"