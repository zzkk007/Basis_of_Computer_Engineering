
def mergeSort(alist):

    #当分解到列表只有一个值时，返回列表。
    if len(alist) <= 1:
        return alist

    # 二分分解
    num = len(alist) // 2

    left = mergeSort(alist[:num])
    right = mergeSort(alist[num:])

    # 合并
    return merge(left, right)

def merge(left, right):

    '''合并操作，将两个有序数列lstf,right 合并成一个更大的有序数组'''
    #left 与 right的下标指针
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

if __name__ == "__main__":

    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sortedList = mergeSort(list1)
    print(sortedList)

