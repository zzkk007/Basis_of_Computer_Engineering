
def lesson12_1(a, b):
    return sorted(a) == sorted(b)

def lesson12_2(a, b):
    dict1, dict2 = {}, {}

    for item in a:
        dict1[item] = dict1.get(item, 0) + 1

    for item in b:
        dict2[item] = dict2.get(item, 0) + 1

    return dict1 == dict2

def lesson12_3(a, b):
    dict1, dict2 = [0]*26, [0]*26
    for item in a:
        dict1[ord(item) - ord('a')] += 1
    for item in b:
        dict2[ord(item) - ord('a')] += 1

    print(dict1)
    print(dict2)
    # [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    # [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]

    return dict1 == dict2



if __name__ == "__main__":

    #print(lesson12_1(a = 'rat', b = 'adr'))
    print(lesson12_3(a = 'dddrat', b = 'dddtar'))

