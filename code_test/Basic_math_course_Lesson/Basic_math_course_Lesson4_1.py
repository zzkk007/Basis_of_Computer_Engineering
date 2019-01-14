
class Result(object):
    def __init__(self):
        self.wheatNum = 0          # 当前格的麦粒数
        self.wheatTotalNum = 0     # 从 1 格到当前格的麦粒总数

class Lession4_2(object):
    """
        :Description: 使用函数的递归（嵌套）调用，进行数学归纳证明
        :param k - 放到底几个格， result -保存当前格子的麦粒数和麦粒总数
        :return boolean - 放到第 K 格时是否成立
    """

    def prove(self, k, result):

        #证明 n = 1 时， 命题是否成立
        if k == 1:
            if (pow(2, 1) - 1) == 1:
                result.wheatNum = 1
                result.wheatTotalNum = 1
                return True
            else:
                return False

        # 如果 n = (k - 1) 时命题成立，证明 n = k 时命题是否成立
        else:

            proveOfPreviousOne = self.prove(k - 1, result)
            result.wheatNum *= 2
            result.wheatTotalNum += result.wheatNum
            proveOfCurrentOne = False

            if result.wheatTotalNum == pow(2, k) -1:
                proveOfCurrentOne = True
            if proveOfPreviousOne and proveOfCurrentOne:
                return True
            else:
                return False

if __name__ == "__main__":
    grid = 63
    result = Result()
    lesion = Lession4_2()

    print(lesion.prove(grid, result))
