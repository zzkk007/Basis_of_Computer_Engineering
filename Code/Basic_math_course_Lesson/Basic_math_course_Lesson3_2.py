
def binary_search(list, world):

    """
    Description : 查找某个单词是否在列表中
    :param list: 排序后的列表
    :param world: 待查找的单词
    :return: 是否发现待查找的单词
    """
    if list is None:
        return False
    elif len(list) == 0:
        return  False

    left = 0
    right = len(list) - 1

    while(left <= right):

        middle = left + (right - left) // 2

        if list[middle] == world:
            return  True
        else:

            if list[middle] > world:
                right = middle - 1
            else:
                left = middle + 1

if __name__ == '__main__':

    list_search = ['i', 'am', 'one', 'of', 'the', 'authors', 'in', 'geekbang']
    list_search.sort()

    wordToFind = 'i'

    found = binary_search(list_search, wordToFind)

    if(found):
        print("found it")
    else:
        print("not found it")


