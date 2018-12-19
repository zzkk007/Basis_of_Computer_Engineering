
def binary2(num):
    if num == 0:
        return '0'
    else:

        return binary2(num >> 1) + str(num & 1)


if __name__ == '__main__':

    num  = int(input("please a decimal:"))

    print((binary2(num)))