import copy
def get_items(totalReward, result):
    """
    :description, 一共 10 元钱，从 1、2、5、10元钱可以有多少同的组合方式。
    :param totalReward: 总钱数
    :param result: 保存当前的解
    :return: void
    """
    # 四种面额的纸币
    rewards = [1, 2, 5, 10]

    # 当满足条件的解，结束嵌套调用，返回解
    if totalReward == 0:
        print(result)
        return
    # 不满足条件，不用输出，直接放弃了。
    elif totalReward < 0:
        return
    else:

        for i in range(len(rewards)):
            # copy 当前解传入的函数中
            newReword = copy.deepcopy(result)
            # 记录当前的选择，解决一点问题
            newReword.append(rewards[i])
            # 剩下的问题交给嵌套调用去解决
            get_items(totalReward - rewards[i], newReword)

if __name__ == "__main__":

    alist = list()
    get_items(10, alist)

