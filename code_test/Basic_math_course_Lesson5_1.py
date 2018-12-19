
class Lesson5_1(object):

    # 四种面额的纸币
    def __init__(self):
        self.rewards = [1, 2, 5, 10]

    """
        :description 使用递归调用，找出所有可能的奖赏组合
        :param totalReward 奖赏总金额，result 保存当前的解
        : return void
    """
    def get(self, totalReward, result):

        #当 totalReward = 0 时，证明它是满足条件的解，结束嵌套，输出解
        if totalReward == 0:
            print(result)
            return
        # 当 totalReword < 0 时，证明它不满足条件的解，不输出。
        elif totalReward < 0:
            return
        else:
            for i in range(len(self.rewards)):
                newReword = []
                newReword.append(self.rewards[i])
                self.get(totalReward - self.rewards[i], newReword)

if __name__ == "__main__":

    totalReword = 10
    alist = list()
    lesson = Lesson5_1()
    lesson.get(totalReword, alist)

    print(alist)