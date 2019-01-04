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

        例子:

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
                        # python 中多变量赋值，先算好等会右边的所有值，然后一次性赋值给左边。
                        cur.next, prev, cur = prev, cur, cur.next
                    return prev

                def swapPairs(self):
                    pre, pre.next = self, self.head
                    while pre.next and pre.next.next:
                        a = pre.next
                        b = a.next

                        pre.next, b.next, a.next = b, a, b.next
                        pre = a
                    return self.next

            if __name__ == "__main__":

                listNode = [1, 2, 3, 4]
                SingleList = SingleLinkList()
                for i in listNode:
                    SingleList.SingleAdd(i)

                SingleList.SinglePrint(None)

                print("--------------------------")

                list1 = SingleList.swapPairs()


                SingleList.SinglePrint(list1)

    3、判断一个链表，判断是否有环

        一个链表只能有一个环，因为一个节点只能有一个 next

        （1）硬做法，单位时间的（0.5S）,判断是否为空

        （2）每走一步，把节点存起来(set), 每到一个节点去set判重。
            时间复杂度 O(n*1)

        （3）快慢指针, 慢指针走一步，快指针走两步，快慢是否相遇。

            def hasCycle(self, head):
                fast = slow = head
                while slow and fast and fast.next:
                    slow = slow.next
                    fast = fast.next.next

                    if slow is fast:
                        return True
                return False


""" 07 理论讲解：堆栈 和 队列"""

    1、堆栈(Stack)和堆（Heap）是两个完全不同的东西
        堆栈也就是栈-- First In Last Out（FILO）
        push
        pop

    2、队列 Queue - First In First Out (FiFO)


"""08 面试题：判断括号字符串是否合法 """"

    1、例如下面字符串

        "()"      合法
        "()[]"    合法
        "([)]"    不合法
        "((([]))" 不合法
        "]][["    不合法

        用栈进行经典的解法：
            a、左括号压栈
            b、右括号和栈顶进行匹配，匹配成功是 pop 栈顶元素，不匹配不合法
            c、如果最后栈为空，则合法。

        时间复杂度 O(1) * n = O(n)

    2、 代码如下：

        def isValid(s):
            """
            :description : 判断字符串的合法性
            :param s: 一个字符串
            :return: 返回 boolean ,True 合法，False 不合法
            """
            stack = []
            paren_map = {')': '(', ']': '[', '}': '{'}
            for c in s:
                # 不是 key 值
                if c not in paren_map:
                    stack.append(c)
                elif not stack or paren_map[c] != stack.pop():
                    return False
            return not stack
        if __name__ == "__main__":
            str1 = "()()()(][){}{}[][[()]]"
            print(isValid(str1))


"""09 面试题：用队列实现栈 & 用栈实现队列 """

    1、用栈实现队列

        使用两个栈来完成实现队列的操作，
        一个栈名是：inputs,一个栈是：outputs,
        用到三个函数 push, pop, peek,
        每个进来的元素首先放到 inputs 栈中，如果出去，把inputs栈中的元素
        push 到 outputs 栈中，从 outpusts 栈中 peek 元素，如果 outputs
        栈不为空，新来的元素到放到 inputs 栈中，等到 outputs 为空，再 push
        到 outputs 栈中。

    2、用队列实现栈:
    
        用两个队列实现栈，假设有两个队列，queue1 和 queue2, 我们一次吧 a, b, c
        入队列 queue1 中，因为我们现实栈操作，所以，我们先出 c 元素。
        我们把 a, b 出 queue1 进 queue2 中, 此时目标 c 跑到 queue1 队头。
        把 c 从 queue1 中输出，此时 queue1 为空，下一个是 b, 我们把 a 从
        queue2 出队进入 queue1 中，b 从queue2 中输出。
        
        即：把非空队列的n-1个压入空对列，剩的第n个出队...即总有一个队列为空。
        
"""10: 理论讲解，优先队列（PriorityQueue） """  

    1、实现方式：
        正常入, 按照优先级出。
        
        1. Heap (Binary, Binomial, Fibonacci)
        
        2. Binary Search Tree
    
    2、概念：
    
        堆(Heap) 是计算机科学中的一种特别的树状数据结构，若满足以下条件即可称为堆。
        "给定堆中任意节点 P 和 C，若 P 是 C 的母节点，那么 P 的值会小于等于（或大于等于） C 的值”。
        若母节点的值恒小于等于子节点的值，此堆称为最小堆（英语：min heap）；
        反之，若母节点的值恒大于等于子节点的值，此堆称为最大堆（英语：max heap）。
        在堆中最顶端的那一个节点，称作根节点（英语：root node），
        根节点本身没有母节点（英语：parent node）"
        
        堆始于 J._W._J._Williams在 1964 年发表的堆排序（英语：heap sort），
        当时他提出了二叉堆树作为此算法的数据结构。堆在戴克斯特拉算法（英语：Dijkstra's algorithm）
        中亦为重要的关键。
        
        在队列中，调度程序反复提取队列中第一个作业并运行，因为实际情况中某些时间较短的任务将等待很长时间才能结束，
        或者某些不短小，但具有重要性的作业，同样应当具有优先权。堆即为解决此类问题设计的一种数据结构。
        一般的优先队列都是用堆实现的。
    
    3、 Python
    
        Python 中没有纯原生的，但是有公认几个不错的 heap 和 collection 库
        
        
"""11: 面试题 返回数据流中的第 k 大元素"""
    
        
    class KthLargest{
        
        final PriorityQueue<Integer> q;
        final int k;
        public KthLargest(int k, int [] a){
            this.k = k
            q = new priorityQueue<>(k);
            for (int n : a)
                add(n);
        }
        
        public int add(int n){
            
            if (q.size() < k)
                q.offer(n);
            else if (q.peek() < n){
                q.poll();
                q.offer();
            }
            return q.peek();
        }
    }     
        
"""12: 面试题 返回滑动窗口中的最大值 """
    
    题目：给一个数组，给一个窗口 k, 窗口在数组中移动的时候，返回最窗口中最大的值。
        示例：
            输入： nums = [1, 3, -1, -3, 5, 3, 6]
                   k = 3
            输出：[3, 3, 5, 5, 6]
            
    
    1、第一个方案是(PriorityQueue)，维护一个大顶堆（MaxHeap），堆顶元素是最大值。
       时间复杂度 O(N * logK)
    
    2、双端对列（deque） 入队列，维护队列。
        时间复杂度 O(N * 1)
        
        # Sliding Window Maxunum
    
        def maxSlidingWindow(nums, k):
            if not nums:
                return []
        
            window, res = [], []
        
            for i, x in enumerate(nums):
                if i >= k and window[0] <= i - k:
                    window.pop(0)
        
                while window and nums[window[-1]] <= x:
                    window.pop()
                window.append(i)
        
                if i >= k - 1:
                    res.append(nums[window[0]])
            return res
        
        if __name__ == "__main__":
        
            nums = [1, 3, -1, -3, 5, 3, 6]
            k = 3
            print(maxSlidingWindow(nums, k))
        
        
             
"""13: 理论讲解 哈希表"""

    1、映射（Map） & 集合（Set）:
    
        映射（Map）: 是一种键值对（key/value）结构。所有值都可以通过键来获取。
        Map 中的键都是唯一的，Map 也叫哈希表(Hash tables)
         
        集合： 就是一种 map 中的键的集合，数据不可重复。
        
    2、HashTable（散列表） & Hash Function（哈希函数） & Collisions (哈希碰撞)
    
        根据键（key）而直接访问在内存存储位置的数据结构。
        也就是说，它通过计算一个关于键值的函数，将所需的数据映射到表中一个位置来访问记录，
        这加快了查询速度。这个映射函数称作散列函数。存放记录的数组称为散列表。
        
        基本概念：
        
            （1）若关键字为 k, 则其值存放在 f(k) 的存储位置上。由此，不需要比较便可以取得所查记录。
                 称这种对应关系 f 为散列函数，按这个思维建立起的数组为散列表。
          
            (2) 对不同的关键字可能得到同一散列地址，即 k1 != k2, 而 f(k1) = f(k2), 这种现象称为冲突（Collision）
                 具有相同函数值的关键字对该散列函数来说称做同义词。
                 综上所述，根据散列函数 f(k)和处理冲突的方法将一组关键字映射到一个有限的连续的地址集
                （区间）上，并以关键字在地址集中的“像”作为记录在表中的存储位置，这种表便称为散列表，
                 这一映射过程称为散列造表或散列，所得的存储位置称散列地址。
             
            (3) 若对于关键字集合中的任一个关键字，经散列函数映象到地址集合中任何一个地址的概率是相等的，
                 则称此类散列函数为均匀散列函数（Uniform Hash function），
                 这就使关键字经过散列函数得到一个“随机的地址”，从而减少冲突。
        
        构造散列函数:
            散列函数能使对一个数据序列的访问过程更加迅速有效，通过散列函数，数据元素将被更快定位。
            
             (1) 直接定址法:取关键字或关键字的某个线性函数值为散列地址。即 hash(k) = k 或 hash(k) = a *k + b(a,b为常数)
                 这种散列函数叫做自身函数。
                 
             (2) 数字分析法: 假设关键字是以r为基的数，并且哈希表中可能出现的关键字都是事先知道的，则可取关键字的若干数位组成哈希地址。
         
             (3) 折叠法：将关键字分割成位数相同的几部分（最后一部分的位数可以不同），然后取这几部分的叠加和（舍去进位）作为哈希地址。
              
             (4) 除留余数法：取关键字被某个不大于散列表表长m的数p除后所得的余数为散列地址。即 hash(k) = k mod p, p <= m
        
        处理冲突：
            
            为了知道冲突产生的相同散列函数地址所对应的关键字，必须选用另外的散列函数，
            或者对冲突结果进行处理。而不发生冲突的可能性是非常之小的，所以通常对冲突进行处理。
            常用方法有以下几种：
     
             (1) 开放定址法
             (2) 单独链表法: 将散列到同一个存储位置的所有元素保存在一个链表中。
                            实现时，一种策略是散列表同一位置的所有冲突结果都是用栈存放的，
                            新元素被插入到表的前端还是后端完全取决于怎样方便。
             (3) 双散列
             (4) 再散列

 
    4、HashMap VS TreeMap、 HashSet VS TreeSet
    
        Map 和 Set 的实现一般由两种方式(HashMap，TreeMap)、(HashSet，TreeSet)
        
        两种实现方式的功能是一样的，不同的是底层数据的存储方式，一种是用Hash Table
        存储，一种使用 binary tree 存储。HashTable 查询时 O(1) 的时间复杂度，
        后者是 Log2N 的时间复杂度。有 TreeMap，TreeSet 是相对有序存储的。
   
    5、 python dict 使用（HashMap实现的）orderdict 是用（TreeMap） 实现的。
    

"""14: 有效字母异位词"""

    即两个单词有相同的字母组成。如 'rat' 和 'tar'
    
    第一种解法是：
        
        对两个字母进行排序，然后比较是否相等。
        这种时间复杂度是 NlogN
        
                    
        def lesson12_1(a, b):
            return sorted(a) == sorted(b)
    
    第二种解法：
        
        使用 map 格式，把字符串,key:value 格式，key 为字母的，value 为个数，比较两个map是否相等。
        这种时间复杂度是 N，但是空间复杂度多了一个map。
        # dict.get(key, default=None)
        # key -- 字典中要查找的键。
        # default -- 如果指定键的值不存在时，返回该默认值值。
        # 
        # 返回值 : 返回指定键的值，如果值不在字典中返回默认值None。
        
        def lesson12_2(a, b):
            dict1, dict2 = {}, {}
        
            for item in a:
                dict1[item] = dict1.get(item, 0) + 1
        
            for item in b:
                dict2[item] = dict2.get(item, 0) + 1
        
            return dict1 == dict2
        
        
        def lesson12_3(a, b):
            dict1, dict2 = [0]*26, [0]*26
            for item in a:
                dict1[ord(item) - ord('a')] += 1
            for item in b:
                dict2[ord(item) - ord('a')] += 1
                
            print(dict1)
            print(dict2)
            # [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
            # [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
        
            return dict1 == dict2
        
        
        if __name__ == "__main__":
        
            #print(lesson12_1(a = 'rat', b = 'adr'))
            print(lesson12_2(a = 'rat', b = 'tar'))    

"""15 两数之和 """

    第一种方法：暴力破解法
    
    第二种方法：使用两遍哈希表
    
    第三种方法：使用一遍哈希表    
             

"""16 三数之和 """

    
"""17：理论讲解，树，二叉树，搜索二叉树"""    

            
         
        
                
    
    
    
    
    





"-----------------------------------------------------------------"