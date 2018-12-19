"""
    @: Description : 计算大于 1 的整数平方根

    @: param n - 待求的数，int 类型，deltaThreshold - 误差的阈值，maxTry - 二分法查找最大次数

    @: return double -- 平方根解

"""

def getSqureRoot(n, deltaThreshold, maxTry):

    if n <= 1:
        return  1.0

    min = 1.0
    max = float(n)

    for i in range(maxTry):

        middle = float((min + max) / 2)
        square = float(middle * middle)
        delta = float(abs((square / n) - 1))

        if delta <= deltaThreshold:
            return  middle
        else:
            if square > n:
                max = middle
            else:
                min = middle
    return 2.0

if __name__ == '__main__':

    number = int(input("pelase input a number:"))

    squareRoot = getSqureRoot(number, 0.000001, 10000)
    if squareRoot == -1.0:
        print("please input greather than 1 number")
    elif squareRoot == -2.0:
        print("No solution found !")
    else:
        print("number :{0}, square root :{1}".format(number, squareRoot))