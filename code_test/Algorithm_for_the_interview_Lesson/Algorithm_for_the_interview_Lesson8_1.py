
def isValid(s):
    """
    :description : 判断字符串的合法性
    :param s: 一个字符串
    :return: 返回 boolean ,True 合法，False 不合法
    """
    stack = []

    paren_map = {')': '(', ']': '[', '}': '{'}

    for c in s:
        # 不是 key 值
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

def isValid1(s):
    while True:
        len1 = len(s)

        s = s.replace("()", "").replace("{}", "").replace("[]", "")
        print(s)
        if len1 != len(s):
            break
    return len(s) == 0


if __name__ == "__main__":

    str1 = "()()()([]){}{}[][[()]]"

    print(isValid1(str1))



