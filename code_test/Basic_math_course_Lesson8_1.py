
def Lesson8_1(teams, result, m):
    """
    :description: 使用函数的递归调用，找出所有可能的队列组合。
    :param teams: 目前还剩多少队伍没有参与组合，
    :param result: 保存当前已经组合的队伍
    :param m: 几个对一个组合
    :return: vid
    """

    # 当挑选完 m 个元素，输出结果
    if len(result) == m:
        print(result)
        return

    for i in range(len(teams)):