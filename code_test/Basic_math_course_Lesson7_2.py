import copy

classes = ['a', 'b', 'c', 'd', 'e']
password = 'bacd'


def get_password(n, result = ''):
    if n == 0:
        if result == password:
            print(result)
        else:
            print(result)
    else:

        for i in classes:
            new_result = copy.deepcopy(result)
            new_result = new_result + i
            get_password(n - 1, new_result)


if __name__ == "__main__":

    get_password(4)
