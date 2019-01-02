import copy

classes = ['a', 'b', 'c', 'd', 'e']
password = 'bacd'


def get_passwor(n, result = ''):
    if n == 0:
        if result == password:
            print(password)
    else:

        for i in classes:
            new_result = copy.deepcopy(result)
            new_result = new_result + i
            get_passwor(n - 1, new_result)


if __name__ == "__main__":

    get_passwor(4)
