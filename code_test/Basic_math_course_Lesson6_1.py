
import copy

class Lession6_1(object):

    def merge_sort(self, items):

        if items is None:
            return None

        if len(items) == 1:
            return items

        mid = len(items) / 2

        left = copy.deepcopy(self.merge_sort(items[0:mid]))
        right = copy.deepcopy(self.merge_sort(items[mid:len(items)]))

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        self.merge(left, right)

    def merge(self, alist, blist):
        if alist is None:
            alist = list()
        if blist is None:
            blist = list()

        merged_one = list()

        mi = 0
        ai = 0
        bi = 0

        # 轮流从两个数组中取出较小的值，放入到合并的数组中
        while ai < len(alist) and bi < len(blist):

            if alist[ai] <= blist[bi]:
                merged_one[mi] = alist[ai]
                ai += 1
            else:
                merged_one[mi] = blist[bi]
                bi += 1
            mi += 1


        # 将某个数组的剩余的数字放入合并后的数组中
        if ai < len(alist):
            for i in range(ai, len(alist)):
                merged_one[mi] = alist[i]
                mi += 1
        else:
            for i in range(bi, len(blist)):
                merged_one[mi] = blist[bi]
                mi += 1

        return merged_one

if __name__ == "__main__":

    clist = [4, 22, 2, 11, 67, 32, 90, 39, 43, 2]

    dlist = Lession6_1()
    elist = dlist.merge_sort(clist)
    print(elist)

