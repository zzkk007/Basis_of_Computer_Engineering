import copy
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
        # 从剩下的队伍中，选择一队，加入结果
        new_result = copy.deepcopy(result)
        new_result.append(teams[i])

        # 只考虑当前选择之后的所有队伍
        rest_teams = copy.deepcopy(teams[i+1:])

        # 递归调用，对于剩余的队伍继续生成组合
        Lesson8_1(rest_teams, new_result, m)

if __name__ == "__main__":
    teams = ['t1', 't2', 't3', 't4']
    Lesson8_1(teams, [], 2)
