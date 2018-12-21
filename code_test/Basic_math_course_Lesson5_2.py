"""
    课程思考题：
        一个整数可以分解为多个整数的乘积，例如， 6 可以分解为 2 * 3，请使用递归
        编程的方法，为给定的 n , 找到所有可能的分解，例如 输入 8 ，输出是可以是
            1 * 8；
            8 * 1；
            2 * 4；
            4 * 2；
            1 * 2 * 2 * 2；
            1 * 2 * 4

"""
import copy
import math

def get_product_factors(n):
    """ get product factors of n
    """
    if n <= 0 or not isinstance(n, int):
        return []
    else:
        product_factors = []
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                product_factors.append(i)
                product_factors.append(int(n / i))

        return sorted(list(set(product_factors)))

def print_multiply_combo(result_list):
    """ add 1 to result_list and print multiply combo
    Args:
        result_list (list): 乘积列表
    Returns: None
    """
    for i in range(len(result_list) + 1):
        new_result_list = copy.copy(result_list)
        new_result_list.insert(i, 1)
        print(new_result_list)

def get_multiply_combo(product, result=[]):
    """ 使用函数的递归（嵌套）调用，找出所有可能的乘积组合
    Args:
        product: 乘积结果
        result: 保存当前的解
    Returns: None
    """
    product_factors = get_product_factors(product)
    for i in product_factors:

        # 先把 1 排除掉
        if i == 1:
            continue

        new_result = copy.copy(result)
        new_result.append(i)

        if i == product:
            #print_multiply_combo(new_result)
            print(new_result)

        divisor = product // i
        if divisor != 1:
            get_multiply_combo(divisor, new_result)


if __name__ == "__main__":

    get_multiply_combo(8)
    # [1, 2, 3]
    # [2, 1, 3]
    # [2, 3, 1]
    # [1, 3, 2]
    # [3, 1, 2]
    # [3, 2, 1]
    # [1, 6]
    # [6, 1]

