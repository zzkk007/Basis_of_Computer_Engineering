import copy
def get_items(totalReward, result):

    rewards = [1, 2, 5, 10]

    if totalReward == 0:
        print(result)
        return
    elif totalReward < 0:
        return
    else:
        for i in range(len(rewards)):
            newReword = copy.deepcopy(result)
            newReword.append(rewards[i])
            get_items(totalReward - rewards[i], newReword)

if __name__ == "__main__":

    alist = list()
    get_items(10, alist)

